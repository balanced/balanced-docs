#!/usr/bin/env python
"""
Backend for the scenario dcode rST directive.

For example:

    .. dcode: scenario
        ...

Maps to:

    def main():
        ...

"""
import argparse
import json
import logging
import os
import re
import sys
import time

import balanced

from balanced_docs import LogLevelAction, memoized, BlockWriter, EnvironmentVarAction


logger = logging.getLogger(__name__)


PERSON_MERCHANT = {
    'type': 'person',
    'name': 'William James',
    'tax_id': '393-48-3992',
    'street_address': '167 West 74th Street',
    'postal_code': '10023',
    'dob': '1842-01-01',
    'phone_number': '+16505551234',
    'country_code': 'USA',
    }

BUSINESS_PRINCIPAL = {
    'name': 'William James',
    'tax_id': '393483992',
    'street_address': '167 West 74th Street',
    'postal_code': '10023',
    'dob': '1842-01-01',
    'phone_number': '+16505551234',
    'country_code': 'USA',
    }

BUSINESS_MERCHANT = {
    'type': 'business',
    'name': 'Levain Bakery',
    'tax_id': '253912384',
    'street_address': '167 West 74th Street',
    'postal_code': '10023',
    'phone_number': '+16505551234',
    'country_code': 'USA',
    'person': BUSINESS_PRINCIPAL,
    }

CARD = {
    'name': 'Benny Riemann',
    'card_number': '4111111111111111',
    'expiration_month': 4,
    'expiration_year': 2014,
    'security_code': 323,
    'street_address': '167 West 74th Street',
    'postal_code': '10023',
    'country_code': 'USA',
    'phone_number': '+16509241212'
}

BANK_ACCOUNT = {
    'name': 'Homer Jay',
    'account_number': '112233a',
    'routing_number': '121042882',
    }


class Context(object):

    #: This is set via environment variable on loading
    #: and on instantiation
    ROOT_URI = 'https://api.balancedpayments.com'

    @classmethod
    def load(cls, io):
        return cls(json.load(io))

    def save(self, io):
        cache = {
            'root_uri': self.ROOT_URI,
            'secret': self.secret,
            'buyer_uri': self.buyer_uri,
            'merchant_uri': self.merchant_uri,
        }
        json.dump(cache, io, indent=4)

    class Interface(object):

        def __init__(self, parent, org):
            self.parent = parent
            self.org = org

        def __getattr__(self, *args, **kwargs):
            return self.org.__getattr__(self, *args, **kwargs)

        def _record(self, r):
            req = {}
            if getattr(r.request, 'body', None):
                req['body'] = self._munge_request(
                    json.loads(r.request.body)
                )
            resp = {
                'headers': [
                    ('Status', '{0} {1}'.format(r.status_code, r.raw.reason)),
                ],
                'body': r.content,
            }
            self.parent.last_req, self.parent.last_resp = req, resp

        def _munge_request(self, payload):
            if payload.get('id', None) is None:
                payload.pop('id', None)
            return json.dumps(payload, indent=4)

        def get(self, *args, **kwargs):
            resp = self.org.get(*args, **kwargs)
            self._record(resp)
            return resp

        def post(self, *args, **kwargs):
            resp = self.org.post(*args, **kwargs)
            self._record(resp)
            return resp

        def put(self, *args, **kwargs):
            resp = self.org.put(*args, **kwargs)
            self._record(resp)
            return resp

        def delete(self, *args, **kwargs):
            resp = self.org.delete(*args, **kwargs)
            self._record(resp)
            return resp

    def __init__(self, cache=None):
        cache = cache or {}
        self.secret = cache.get('secret')
        self.buyer_uri = cache.get('buyer_uri')
        self.merchant_uri = cache.get('merchant_uri')
        self.root_uri = cache.get('root_uri', self.ROOT_URI)

        balanced.Resource.http_client.interface = self.Interface(
            parent=self,
            org=balanced.Resource.http_client.interface,
        )

    @property
    @memoized
    def marketplace(self):
        balanced.config.root_uri = self.root_uri
        if not self.secret:
            logger.debug('creating api key')
            self.secret = balanced.APIKey().save().secret
        balanced.configure(self.secret)
        try:
            marketplace = balanced.Marketplace.mine
        except balanced.exc.NoResultFound:
            logger.debug('creating marketplace')
            marketplace = balanced.Marketplace().save()
        return marketplace

    @property
    @memoized
    def merchant(self):
        if self.merchant_uri:
            try:
                return balanced.Account.find(self.merchant_uri)
            except balanced.exc.HTTPError:
                pass
        logger.debug('creating merchant')
        bank_account = self.marketplace.create_bank_account(**BANK_ACCOUNT)
        merchant = self.marketplace.create_merchant(
            None,
            merchant=PERSON_MERCHANT,
            bank_account_uri=bank_account.uri
        )
        self.merchant_uri = merchant.uri
        return merchant

    @property
    @memoized
    def bank_account(self):
        return self.merchant.bank_accounts[0]

    @property
    @memoized
    def buyer(self):
        if self.buyer_uri:
            try:
                return balanced.Account.find(self.buyer_uri)
            except balanced.exc.HTTPError:
                pass
        logger.debug('creating buyer')
        card = self.marketplace.create_card(**CARD)
        buyer = self.marketplace.create_buyer(None, card.uri)
        self.buyer_uri = buyer.uri
        return buyer

    @property
    @memoized
    def card(self):
        return self.buyer.cards[0]


def scenario(f):
    f.scenario = f.__name__
    return f


@scenario
def credits_index(ctx):
    ctx.bank_account.credit(amount=1254)
    ctx.bank_account.credit(amount=431)
    ctx.marketplace.credits_uri += '?limit=2'
    ctx.marketplace.credits[0:2]
    return ctx.last_req, ctx.last_resp


@scenario
def credits_show(ctx):
    credit = ctx.bank_account.credit(amount=1254)
    balanced.Credit.find(credit.uri)
    return ctx.last_req, ctx.last_resp


@scenario
def credits_create(ctx):
    ctx.bank_account.credit(
        amount=1254,
        description='Something descriptive',
    )
    return ctx.last_req, ctx.last_resp


@scenario
def bank_account_credits_index(ctx):
    ctx.bank_account.credit(
        amount=1254,
        description='A description',
    )
    ctx.bank_account.credit(
        amount=431,
        description='Another description',
    )
    ctx.bank_account.credit(
        amount=1452,
        description='Yet another description',
    )
    ctx.bank_account.credits_uri += '?limit=2'
    ctx.bank_account.credits[0:2]
    return ctx.last_req, ctx.last_resp


@scenario
def bank_account_credits_show(ctx):
    credit = ctx.bank_account.credit(
        amount=1254,
        description='A description',
    )
    balanced.Credit.find(credit.uri)
    return ctx.last_req, ctx.last_resp


@scenario
def bank_account_credits_create(ctx):
    ctx.bank_account.credit(
        amount=1254,
        description='Something descriptive',
    )
    return ctx.last_req, ctx.last_resp


@scenario
def account_credits_index(ctx):
    ctx.merchant.credit(amount=1254)
    ctx.merchant.credit(amount=431)
    ctx.merchant.credits_uri += '?limit=2'
    ctx.merchant.credits[0:2]
    return ctx.last_req, ctx.last_resp


@scenario
def account_credits_show(ctx):
    credit = ctx.merchant.credit(amount=431)
    balanced.Credit.find(credit.uri)
    return ctx.last_req, ctx.last_resp


@scenario
def account_credits_create(ctx):
    ctx.merchant.credit(amount=1243)
    return ctx.last_req, ctx.last_resp


@scenario
def cards_tokenize(ctx):
    ctx.marketplace.create_card(**CARD)
    return ctx.last_req, ctx.last_resp


@scenario
def cards_show(ctx):
    card = ctx.marketplace.create_card(**CARD)
    balanced.Card.find(card.uri)
    return ctx.last_req, ctx.last_resp


@scenario
def cards_index(ctx):
    ctx.merchant.cards_uri += '?limit=2'
    ctx.merchant.cards[0:2]
    return ctx.last_req, ctx.last_resp


@scenario
def cards_update(ctx):
    card = ctx.marketplace.create_card(**CARD)
    card.meta = {'my-own-field': 'Customer request'}
    card.is_valid = 'False'
    card.save()
    return ctx.last_req, ctx.last_resp


@scenario
def cards_associate(ctx):
    card = ctx.marketplace.create_card(**CARD)
    del card.account
    card.account_uri = ctx.buyer.uri
    card.save()
    return ctx.last_req, ctx.last_resp


@scenario
def bank_accounts_create(ctx):
    ctx.marketplace.create_bank_account(**BANK_ACCOUNT)
    return ctx.last_req, ctx.last_resp


@scenario
def bank_accounts_show(ctx):
    ba = ctx.marketplace.create_bank_account(**BANK_ACCOUNT)
    balanced.BankAccount.find(ba.uri)
    return ctx.last_req, ctx.last_resp


@scenario
def bank_accounts_index(ctx):
    ctx.merchant.bank_accounts_uri += '?limit=2'
    ctx.merchant.bank_accounts[0:2]
    return ctx.last_req, ctx.last_resp


@scenario
def bank_accounts_associate(ctx):
    ba = ctx.marketplace.create_bank_account(**BANK_ACCOUNT)
    del ba.account
    ba.account_uri = ctx.merchant.uri
    ba.save()
    return ctx.last_req, ctx.last_resp


@scenario
def bank_accounts_delete(ctx):
    ba = balanced.BankAccount(**BANK_ACCOUNT).save()
    ba.delete()
    return ctx.last_req, ctx.last_resp


@scenario
def account_bank_accounts_index(ctx):
    ctx.merchant.bank_accounts_uri += '?limit=2'
    ctx.merchant.bank_accounts[0:2]
    return ctx.last_req, ctx.last_resp


@scenario
def account_cards_index(ctx):
    ctx.buyer.cards_uri += '?limit=2'
    ctx.buyer.cards[0:2]
    return ctx.last_req, ctx.last_resp


@scenario
def accounts_create_buyer(ctx):
    card = ctx.marketplace.create_card(**CARD)
    ctx.marketplace.create_buyer(
        name='Benny Riemann',
        email_address=None,
        card_uri=card.uri,
    )
    return ctx.last_req, ctx.last_resp


@scenario
def accounts_create_business_merchant(ctx):
    ctx.marketplace.create_merchant(
        None,
        merchant=BUSINESS_MERCHANT,
    )
    return ctx.last_req, ctx.last_resp


@scenario
def accounts_create_person_merchant(ctx):
    ctx.marketplace.create_merchant(
        None,
        merchant=PERSON_MERCHANT,
    )
    return ctx.last_req, ctx.last_resp


@scenario
def accounts_index(ctx):
    ctx.marketplace.accounts_uri += '?limit=2'
    ctx.marketplace.accounts[0:2]
    return ctx.last_req, ctx.last_resp


@scenario
def accounts_show(ctx):
    balanced.Account.find(ctx.buyer.uri)
    return ctx.last_req, ctx.last_resp


@scenario
def accounts_update(ctx):
    card = ctx.marketplace.create_card(**CARD)
    buyer = ctx.marketplace.create_buyer(
        name='Benny Riemann',
        email_address=None,
        card_uri=card.uri,
    )

    buyer.meta.update({
        'more-data': 'here',
    })
    buyer.name = 'my new name',
    buyer.save()

    return ctx.last_req, ctx.last_resp


@scenario
def accounts_promote_buyer(ctx):
    card = ctx.marketplace.create_card(**CARD)
    buyer = ctx.marketplace.create_buyer(
        name='Benny Riemann',
        email_address=None,
        card_uri=card.uri,
    )

    buyer.promote_to_merchant(PERSON_MERCHANT)

    return ctx.last_req, ctx.last_resp


@scenario
def api_keys_create(ctx):
    balanced.APIKey().save()
    return ctx.last_req, ctx.last_resp


@scenario
def api_keys_update(ctx):
    k = balanced.APIKey().save()
    k.meta.update({'some': 'different data'})
    k.save()
    return ctx.last_req, ctx.last_resp


@scenario
def api_keys_show(ctx):
    k = balanced.APIKey().save()
    balanced.APIKey.find(k.uri)
    return ctx.last_req, ctx.last_resp


@scenario
def api_keys_delete(ctx):
    k = balanced.APIKey().save()
    k.delete()
    return ctx.last_req, ctx.last_resp


@scenario
def api_keys_index(ctx):
    balanced.resources.Page('/v1/api_keys?limit=2')[0:2]
    return ctx.last_req, ctx.last_resp


@scenario
def debits_index(ctx):
    ctx.card.debit(amount=1254)
    ctx.card.debit(amount=431)
    ctx.marketplace.debits_uri += '?limit=2'
    ctx.marketplace.debits[0:2]
    return ctx.last_req, ctx.last_resp


@scenario
def debits_show(ctx):
    balanced.Debit.find(ctx.card.debit(amount=1254).uri)
    return ctx.last_req, ctx.last_resp


@scenario
def debits_update(ctx):
    debit = ctx.card.debit(amount=1254)
    debit.description = 'my new description'
    debit.meta.update({
        'my-id': '0987654321',
    })
    debit.save()
    return ctx.last_req, ctx.last_resp


@scenario
def debits_create(ctx):
    ctx.buyer.debit(
        amount=1254,
        on_behalf_of=ctx.merchant.uri
    )
    return ctx.last_req, ctx.last_resp


@scenario
def refunds_show(ctx):
    debit = ctx.buyer.debit(amount=1254,)
    debit.refund()
    return ctx.last_req, ctx.last_resp


@scenario
def refunds_index(ctx):
    ctx.buyer.debit(amount=1254).refund()
    ctx.buyer.debit(amount=431).refund()
    ctx.marketplace.refunds_uri += '?limit=2'
    ctx.marketplace.refunds[0:2]
    return ctx.last_req, ctx.last_resp


@scenario
def refunds_update(ctx):
    refund = ctx.buyer.debit(amount=1254).refund()
    refund.description = 'my new description'
    refund.meta = {
        'my-id': '0987654321',
    }
    refund.save()
    return ctx.last_req, ctx.last_resp


@scenario
def refunds_create(ctx):
    ctx.buyer.debit(amount=1254).refund(1234)
    return ctx.last_req, ctx.last_resp


@scenario
def debit_refunds_create(ctx):
    debit = ctx.buyer.debit(amount=1254)
    balanced.Refund(uri=debit.refunds_uri).save()
    return ctx.last_req, ctx.last_resp


@scenario
def holds_create(ctx):
    ctx.card.hold(**{
        'amount': 3421,
        'description': 'Something tasty',
        'meta': {
            'id': '#12312123123',
        }
    })
    return ctx.last_req, ctx.last_resp


@scenario
def holds_show(ctx):
    balanced.Card.find(ctx.card.hold(**{
        'amount': 3421,
        'description': 'Something tasty',
        'meta': {
            'id': '#12312123123',
        }
    }).uri)
    return ctx.last_req, ctx.last_resp


@scenario
def holds_index(ctx):
    ctx.buyer.hold(amount=1233, description='Something sweet')
    ctx.buyer.hold(amount=3344, description='Something sour')
    ctx.buyer.hold(amount=6754, description='Something spicy')
    ctx.buyer.hold(amount=1322, description='Something tangy')
    ctx.marketplace.holds_uri += '?limit=4'
    ctx.marketplace.holds[0:4]
    return ctx.last_req, ctx.last_resp


@scenario
def holds_update(ctx):
    hold = ctx.buyer.hold(amount=3344, description='Something sour')
    hold.description = 'Something really tasty'
    hold.meta = {
        'the-address': '123 Fake Street',
    }
    hold.save()
    return ctx.last_req, ctx.last_resp


@scenario
def holds_capture(ctx):
    hold = ctx.buyer.hold(amount=3344, description='Something sour')
    hold.capture()
    return ctx.last_req, ctx.last_resp


@scenario
def holds_void(ctx):
    hold = ctx.buyer.hold(amount=3344, description='Something sour')
    hold.meta.update({
        'reason': 'Customer request',
    })
    hold.void()
    return ctx.last_req, ctx.last_resp


@scenario
def marketplaces_create(ctx):
    with balanced.key_switcher(None):
        secret = balanced.APIKey().save().secret
        with balanced.key_switcher(secret):
            balanced.Marketplace(**{
                'support_email_address': 'support@example.com',
                'name': 'Seller of things',
                'domain_url': 'example.com',
                'support_phone_number': '+12125551212',
                'meta': {
                    'my-useful-data': 'abc123'
                }
            }).save()
            return ctx.last_req, ctx.last_resp


@scenario
def marketplaces_show(ctx):
    balanced.Marketplace.find(ctx.marketplace.uri)
    return ctx.last_req, ctx.last_resp


@scenario
def marketplaces_update(ctx):
    with balanced.key_switcher(None):
        secret = balanced.APIKey().save().secret
        with balanced.key_switcher(secret):
            mp = balanced.Marketplace(**{
                'support_email_address': 'support@example.com',
                'name': 'Seller of things',
                'domain_url': 'example.com',
                'support_phone_number': '+12125551212',
                'meta': {
                    'my-useful-data': 'abc123'
                }
            }).save()

            mp.support_email_address = 'faster-support@example.com'
            mp.name = 'Seller of thingz'
            mp.support_phone_number = '+18185551212'
            mp.meta.update({
                'even-more-useful-data': '321cba'
            })
            mp.save()

            return ctx.last_req, ctx.last_resp


@scenario
def marketplaces_index(ctx):
    balanced.Marketplace.mine
    return ctx.last_req, ctx.last_resp


@scenario
def transactions_index(ctx):
    ctx.merchant.credit(amount=245)
    ctx.buyer.debit(amount=5544).refund()
    ctx.buyer.hold(amount=123).capture()
    ctx.buyer.hold(amount=123).void()
    ctx.marketplace.transactions_uri += '?limit=7'
    ctx.marketplace.transactions[0:6]
    return ctx.last_req, ctx.last_resp


@scenario
def events_index(ctx):
    total = ctx.marketplace.events.total

    ctx.merchant.credit(amount=245)
    ctx.buyer.debit(amount=5544).refund()
    ctx.buyer.hold(amount=123).capture()
    ctx.buyer.hold(amount=123).void()

    while ctx.marketplace.events.total < total + 6:
        time.sleep(5)

    ctx.marketplace.events_uri += '?limit=7'
    ctx.marketplace.events[0:6]

    return ctx.last_req, ctx.last_resp


@scenario
def events_show(ctx):
    balanced.Event.find(ctx.marketplace.events[0].uri)
    return ctx.last_req, ctx.last_resp


@scenario
def event_callbacks_index(ctx):
    raise Exception('does not work')

    if ctx.marketplace.callbacks.total == 0:
        balanced.Callback(
            uri=ctx.marketplace.callbacks_uri,
            url='http://www.example.com/cb',
        ).save()
    total = ctx.marketplace.events.total
    ctx.merchant.credit(amount=245)
    while ctx.marketplace.events.total < total + 1:
        time.sleep(5)
    event = balanced.Event.find(ctx.marketplace.events[0].uri)
    event.callbacks[:]
    return ctx.last_req, ctx.last_resp


@scenario
def event_callbacks_show(ctx):
    raise Exception('does not work')

    if ctx.marketplace.callbacks.total == 0:
        balanced.Callback(
            uri=ctx.marketplace.callbacks_uri,
            url='http://www.example.com/cb',
        ).save()
    total = ctx.marketplace.events.total
    ctx.buyer.debit(amount=245)
    while ctx.marketplace.events.total < total + 1:
        time.sleep(5)
    event = balanced.Event.find(ctx.marketplace.events[0].uri)
    balanced.EventCallback.find(event.callbacks[0].uri)
    return ctx.last_req, ctx.last_resp


@scenario
def callbacks_index(ctx):
    if ctx.marketplace.callbacks.total < 2:
        balanced.Callback(
            uri=ctx.marketplace.callbacks_uri,
            url='http://www.example.com/cb1',
            method='post',
        ).save()
        balanced.Callback(
            uri=ctx.marketplace.callbacks_uri,
            url='http://www.example.com/cb2',
            method='get',
        ).save()

    ctx.marketplace.callbacks_uri += '?limit=2'
    ctx.marketplace.callbacks[0:2]

    return ctx.last_req, ctx.last_resp


@scenario
def callbacks_show(ctx):
    if ctx.marketplace.callbacks.total == 0:
        balanced.Callback(
            uri=ctx.marketplace.callbacks_uri,
            url='http://www.example.com/cb/fosho',
            method='post',
        ).save()
    balanced.Callback.find(ctx.marketplace.callbacks[0].uri)

    return ctx.last_req, ctx.last_resp


@scenario
def callbacks_create(ctx):
    with balanced.key_switcher(None):
        secret = balanced.APIKey().save().secret
        with balanced.key_switcher(secret):
            mp = balanced.Marketplace().save()
            balanced.Callback(
                uri=mp.callbacks_uri,
                url='http://www.example.com/cb/nu',
                method='post',
            ).save()
        return ctx.last_req, ctx.last_resp


@scenario
def callbacks_delete(ctx):
    cb = balanced.Callback(
        uri=ctx.marketplace.callbacks_uri,
        url='http://www.example.com/cb/del',
        method='post',
    ).save()
    cb.delete()
    return ctx.last_req, ctx.last_resp


@scenario
def bank_account_authentications_index(ctx):
    ba = ctx.marketplace.create_bank_account(**BANK_ACCOUNT)
    ba.verify()
    ba.verifications[0:2]
    return ctx.last_req, ctx.last_resp


@scenario
def bank_account_authentications_show(ctx):
    ba = ctx.marketplace.create_bank_account(**BANK_ACCOUNT)
    bav = ba.verify()
    balanced.BankAccountVerification.find(bav.uri)
    return ctx.last_req, ctx.last_resp


@scenario
def bank_account_authentications_create(ctx):
    ba = ctx.marketplace.create_bank_account(**BANK_ACCOUNT)
    ba.verify()
    return ctx.last_req, ctx.last_resp


@scenario
def bank_account_authentications_update(ctx):
    ba = ctx.marketplace.create_bank_account(**BANK_ACCOUNT)
    bav = ba.verify()
    bav.confirm(1, 1)
    return ctx.last_req, ctx.last_resp


class Customer(balanced.Resource):
    __metaclass__ = balanced.resources.resource_base(
        collection='customers', resides_under_marketplace=False)

balanced.Customer = Customer


@scenario
def customers_create(ctx):
    customer = balanced.Customer(
        email='user@example.org',
        twitter='@balanced',
        facebook='https://facebook.com/balanced',
        ssn_last4='3209',
        phone='(904) 555-1796',
        ein='123456789',
        name='John Lee Hooker',
        business_name='Balanced',
        address = {
            'line1': '965 Mission St',
            'city': 'San Francisco',
            'state': 'CA',
            'postal_code': '94103',
            'country_code': 'US',
        }, meta={
            'meta can store': 'any flat key/value data you like',
            'more_additional_data': 54.80,
            'github': 'https://github.com/balanced'
        }
    )
    customer.save()
    return ctx.last_req, ctx.last_resp

@scenario
def customers_show(ctx):
    customer = balanced.Customer(
        address = {
            'line1': '965 Mission St',
            'line2': '#425',
            'city': 'San Francisco',
            'state': 'CA',
            'postal_code': '94103',
            'country_code': 'USA',
        }
    ).save()
    customer = balanced.Customer.find(customer.uri)
    return ctx.last_req, ctx.last_resp

@scenario
def customers_index(ctx):
    balanced.Customer(
        address = {
            'line1': '965 Mission St',
            'line2': '#425',
            'city': 'San Francisco',
            'state': 'CA',
            'postal_code': '94103',
            'country_code': 'USA',
        }
    ).save()
    balanced.Customer.query.all()
    return ctx.last_req, ctx.last_resp

@scenario
def customers_update(ctx):
    customer = balanced.Customer()
    customer.save()
    customer.name = 'Richie McCaw'
    customer.email_address = 'richie@allblacks.com'
    customer.save()
    return ctx.last_req, ctx.last_resp

@scenario
def customers_delete(ctx):
    customer = balanced.Customer()
    customer.save()
    customer.delete()
    return ctx.last_req, ctx.last_resp


SCENARIOS = dict(
    (v.scenario, v)
    for k, v in globals().iteritems()
    if hasattr(v, '__call__') and hasattr(v, 'scenario')
)


# main

def create_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'scenarios',
        nargs='+',
        metavar='SCENARIO',
        help='Name of the SCENARIO to run.',
    )
    parser.add_argument(
        '-l', '--log-level',
        choices=['debug', 'info', 'warn', 'error'],
        default=logging.INFO,
        action=LogLevelAction,
    )
    parser.add_argument(
        '-c', '--cache',
        metavar='PATH',
        default=None,
        help='PATH to scenario context cache file. No caching by default.',
    )
    parser.add_argument(
        '--sections',
        metavar='CHARS',
        default='~^',
        help='String of CHARS to use for section headings.',
    )
    parser.add_argument(
        '--api-location',
        metavar='URL',
        action=EnvironmentVarAction,
        env_var='BALANCED_DOCS_API_LOC',
        default='https://api.balancedpayments.com',
        help='Uses URL as the api location.',
    )
    return parser


def generate(write, req, resp, section_chars):
    write('Request\n')
    write(section_chars[0] * len('Request'))
    write('\n\n')

    if 'body' in req:
        write('Body\n')
        write(section_chars[1] * len('Body'))
        write('\n\n')

        write('.. code:: javascript\n')
        with write:
            write('\n')
            write(req['body'])
        write('\n')

    write('Response\n')
    write(section_chars[0] * len('Response'))
    write('\n\n')

    write('Headers\n')
    write(section_chars[1] * len('Headers'))
    write('\n\n')

    write('.. code::\n')
    with write:
        write('\n')
        for k, v in resp['headers']:
            write(k)
            write(': ')
            write(v)
            write('\n')
    write('\n')

    write('Body\n')
    write(section_chars[1] * len('Body'))
    write('\n\n')

    write('.. code:: javascript\n')
    with write:
        write('\n')
        write(resp['body'])
    write('\n')


def main():
    parser = create_arg_parser()
    args = parser.parse_args()

    root = logging.getLogger()
    formatter = logging.Formatter('%(asctime)s : %(name)s : %(message)s')
    handler = logging.StreamHandler(sys.stderr)
    handler.setFormatter(formatter)
    root.addHandler(handler)
    root.setLevel(args.log_level)

    Context.ROOT_URI = args.api_location

    if args.cache and os.path.isfile(args.cache):
        logger.debug('loading context from cache "%s"', args.cache)
        ctx = Context.load(open(args.cache, 'r'))
    else:
        ctx = Context()
    try:
        thresh_h, thresh_l = 10000000, 100000
        if ctx.marketplace.in_escrow < thresh_l:
            amount = thresh_h - ctx.marketplace.in_escrow
            logger.debug('incrementing escrow balanced %s', amount)
            ctx.card.debit(amount)
        write = BlockWriter(sys.stdout)
        for name in args.scenarios:
            munged = re.sub(r'[\-\.]', '_', name.lower())
            if munged not in SCENARIOS:
                raise ValueError('Invalid scenario "{0}" (munged "{1}")'.format(name, munged))
            req, resp = SCENARIOS[munged](ctx)
            generate(write, req, resp, args.sections)
    finally:
        if args.cache:
            logger.debug('saving context to cache "%s"', args.cache)
            ctx.save(open(args.cache, 'w'))


if __name__ == '__main__':
    main()
