#!/usr/bin/env python
"""
"""
import argparse
from collections import OrderedDict
import json
import logging
import sys

logger = logging.getLogger(__name__)


class Context(object):

    @classmethod
    def load(cls):
        raise NotImplemented()

    def save(self, io):
        raise NotImplemented()

    def format(self, req, resp):
        block = OrderedDict()
        if req:
            block['Request'] = self._format_request(req)
        if resp:
            block['Response'] = self._format_response(resp)
        return json.dumps([block], indent=4)

    def url_for(self, **kwargs):
        raise NotImplemented()

    def get(self, url):
        raise NotImplemented()

    def post(self, url, data):
        raise NotImplemented()

    def put(self, url, data):
        raise NotImplemented()

    def data(self, url, data):
        raise NotImplemented()


def scenario(f):
    f.scenario = f.__name__
    return f


@scenario
def credits_index(ctx):
    ctx.bank_account.credit(amount=1254)
    ctx.bank_account.credit(amount=431)
    url = ctx.url_for('credits.index')
    return ctx.get(url)


@scenario
def credits_show(ctx):
    credit = ctx.bank_account.credit(amount=1254)
    url = ctx.url_for('credits.show', credit=credit.id)
    return ctx.get(url)


@scenario
def credits_create(ctx):
    url = ctx.url_for('credits.create')
    payload = {
        'amount': 1234,
        'description': 'Something descriptive',
        'bank_account': {
            'account_number': '12341234',
            'bank_code': '325182797',
            'name': 'Fit Finlay',
            'account_type': 'checking',
        },
    }
    return ctx.post(url, payload)


@scenario
def bank_account_credits_index(ctx, args):
    ctx.bank_account.credit()
    ctx.bank_account.credit(
        amount=1254,
        description='A description',
    )
    ctx.bank_account.credit(
        amount=431,
        description='Another description',
    )
    ctx.bank_account.credit(
        amount=5452,
        description='Yet another description',
    )
    url = ctx.url_for(
        'bank_account_credits.index',
        bank_account=ctx.bank_account.id,
    )
    return ctx.get(url)


@scenario
def bank_account_credits_show(ctx):
    credit = ctx.bank_account.credit(
        amount=1254,
        description='A description'
    )
    url = ctx.url_for(
        'bank_account_credits.show',
        bank_account=ctx.bank_account,
        credit=credit,
    )
    return ctx.get(url)


@scenario
def bank_account_credits_create(ctx):
    url = ctx.url_for(
        'bank_account_credits.create',
        bank_account=ctx.bank_account.id,
    )
    payload = {
        'amount': 1234,
        'description': 'A description',
    }
    return ctx.post(url, payload)


@scenario
def account_credits_index(ctx):
    ctx.account.credit(amount=1254)
    ctx.account.credit(amount=431)
    url = ctx.url_for(
        'account_credits.index',
        marketplace=ctx.marketplace.id,
        account=ctx.account.id,
    )
    return ctx.get(url)


def account_credits_show(ctx):
    credit = ctx.account.credit(amount=1254)
    url = ctx.url_for(
        'account_credits.show',
        marketplace=ctx.marketplace,
        account=ctx.account,
        credit=credit,
    )
    return ctx.get(url)


@scenario
def account_credits_create(ctx):
    url = ctx.url_for(
        'account_credits.create',
        marketplace=ctx.marketplace, account=ctx.account
    )
    payload = {
        'amount': 1234
    }
    return ctx.post(url, payload)


@scenario
def cards_tokenize(ctx):
    url = ctx.url_for(
        'marketplace_cards.create',
        marketplace=ctx.marketplace,
    )
    payload = {
        'name': 'Benny Riemann',
        'card_number': cards.generator().next(),
        'expiration_month': 4,
        'expiration_year': 2014,
        'security_code': 323,
        'street_address': '167 West 74th Street',
        'postal_code': '10023',
        'country_code': 'USA',
        'phone_number': '+16509241212'
    }
    return ctx.post(url, payload)


@scenario
def cards_show(ctx):
    url = ctx.url_for(
        'marketplace_cards.show',
        marketplace=ctx.marketplace,
        card=ctx.card,
    )
    return ctx.get(url)


@scenario
def cards_index(ctx):
    ctx.marketplace.create_card(**{
        'name': 'Benny Riemann',
        'number': cards.generator().next(),
        'expiration_month': 4,
        'expiration_year': 2014,
        'security_code': 323,
        'address': {
            'street_address': '167 West 74th Street',
            'postal_code': '10023',
            'country_code': 'USA',
        },
        'phone_number': '+16509241212',
    })
    ctx.marketplace.create_card(**{
        'name': 'Lonnie Riemann',
        'number': cards.generator().next(),
        'expiration_month': 5,
        'expiration_year': 2015,
        'security_code': 642,
        'address': {
            'street_address': '167 West 74th Street',
            'postal_code': '10023',
            'country_code': 'USA',
        },
        'phone_number': '+16509241211',
    })
    url = ctx.url_for(
        'marketplace_cards.index',
        marketplace=ctx.marketplace,
    )
    return ctx.get(url)


@scenario
def cards_update(ctx):
    payload = {
        'meta': {
            'my-own-field': 'Customer request',
        },
        'is_valid': 'False',
    }
    url = ctx.url_for(
        'marketplace_cards.update',
        marketplace=ctx.marketplace,
        card=ctx.card)
    return ctx.put(url, payload)


@scenario
def cards_associate(ctx):
    card = ctx.marketplace.create_card(**{
        'name': 'Benny Riemann',
        'number': cards.generator().next(),
        'expiration_month': 4,
        'expiration_year': 2014,
        'security_code': 323,
    })
    account_uri = ctx.url_for(
        'accounts.show',
        marketplace=ctx.marketplace,
        account=ctx.account,
    )
    payload = {
        'account_uri': account_uri,
    }
    url = ctx.url_for(
        'marketplace_cards.update',
        marketplace=ctx.marketplace,
        card=card,
    )
    return ctx.put(url, payload)


@scenario
def bank_account_create(self):
    url = self.url_for('bank_accounts.create')
    payload = self._bank_account_payload()
    data = self.to_json(payload)
    resp = self.client.post(
        url, user=self.mp_owner,
        content_type='application/json', data=data)
    self.assertEqual(resp.status_code, 201)
    print self._format(self.client.last_request, resp)


@scenario
def bank_account_show(self):
    bank_account = bank_accounts.create(marketplace=self.mp)
    self.session.flush()
    url = self.url_for('bank_accounts.show', bank_account=bank_account)
    resp = self.client.get(url, user=self.mp_owner)
    self.assertEqual(resp.status_code, 200)
    print self._format(self.client.last_request, resp)


@scenario
def bank_account_index(self):
    bank_accounts.create(marketplace=self.mp)
    bank_accounts.create(marketplace=self.mp)
    url = self.url_for('bank_accounts.index')
    resp = self.client.get(url, user=self.mp_owner)
    self.assertEqual(resp.status_code, 200)
    print self._format(self.client.last_request, resp)


@scenario
def bank_account_associate(self):
    bank_account = bank_accounts.create(marketplace=self.mp)
    self.session.flush()
    account_uri = self.url_for(
        'accounts.show', marketplace=self.mp, account=self.account)
    url = self.url_for(
        'marketplace_bank_accounts.update',
        marketplace=self.mp, bank_account=bank_account)
    payload = {
        'account_uri': account_uri,
    }
    data = self.to_json(payload)
    resp = self.client.put(
        url, content_type='application/json', data=data,
        user=self.mp_owner)
    print self._format(self.client.last_request, resp)


@scenario
def bank_account_delete(self):
    bank_account = bank_accounts.create(marketplace=self.mp)
    self.session.flush()
    url = self.url_for(
        'bank_accounts.delete', bank_account=bank_account)
    resp = self.client.delete(url, user=self.mp_owner)
    print self._format(self.client.last_request, resp)


@scenario
def accpint_bank_account_index(self):
    self.account.add_bank_account(
        bank_accounts.create(marketplace=self.mp))
    self.account.add_bank_account(
        bank_accounts.create(marketplace=self.mp))
    url = self.url_for(
        'account_bank_accounts.index',
        marketplace=self.mp,
        account=self.account)
    resp = self.client.get(url, user=self.mp_owner)
    self.assertEqual(resp.status_code, 200)
    print self._format(self.client.last_request, resp)


@scenario
def account_cards_index(self):
    self.account.add_card(cards.create(marketplace=self.mp))
    self.account.add_card(cards.create(marketplace=self.mp))
    url = self.url_for(
        'account_cards.index',
        marketplace=self.mp,
        account=self.account)
    resp = self.client.get(url, user=self.mp_owner)
    self.assertEqual(resp.status_code, 200)
    print self._format(self.client.last_request, resp)


@scenario
def accounts_create_buyer(self):
    card = cards.create(marketplace=self.mp)
    self.session.flush()
    card_uri = self.url_for(
        'marketplace_cards.show', marketplace=self.mp, card=card)
    url = self.url_for('accounts.create', marketplace=self.mp)
    payload = {
        'name': 'Benny Riemann',
        'email_address': 'b@m.com',
        'card_uri': card_uri,
    }
    data = self.to_json(payload)
    resp = self.client.post(
        url, user=self.mp_owner,
        content_type='application/json', data=data)
    self.assertEqual(resp.status_code, 201)
    print self._format(self.client.last_request, resp)


@scenario
def accounts_create_business_merchant(self):
    url = self.url_for('accounts.create', marketplace=self.mp)
    payload = accounts.create_payload_business_merchant()
    data = self.to_json(payload)
    resp = self.client.post(
        url, user=self.mp_owner,
        content_type='application/json', data=data)
    self.assertEqual(resp.status_code, 201)
    print self._format(self.client.last_request, resp)


@scenario
def accounts_create_person_merchant(self):
    url = self.url_for('accounts.create', marketplace=self.mp)
    payload = accounts.create_payload_person_merchant()
    data = self.to_json(payload)
    resp = self.client.post(
        url, user=self.mp_owner,
        content_type='application/json', data=data)
    self.assertEqual(resp.status_code, 201)
    print self._format(self.client.last_request, resp)


@scenario
def accounts_index(self):
    accounts.create_business_merchant_account(marketplace=self.mp)
    accounts.create_buyer(marketplace=self.mp)
    accounts.create_person_merchant(marketplace=self.mp)
    self.session.flush()
    url = self.url_for('accounts.index', marketplace=self.mp)
    resp = self.client.get(url, user=self.mp_owner)
    self.assertEqual(resp.status_code, 200)
    print self._format(self.client.last_request, resp)


@scenario
def accounts_show(self):
    buyer = accounts.create_buyer(marketplace=self.mp)
    self.session.flush()
    url = self.url_for('accounts.show', marketplace=self.mp, account=buyer)
    resp = self.client.get(url, user=self.mp_owner)
    self.assertEqual(resp.status_code, 200)
    print self._format(self.client.last_request, resp)


@scenario
def accounts_update(self):
    card = cards.create(marketplace=self.mp)
    self.session.flush()
    card_uri = self.url_for(
        'marketplace_cards.show', marketplace=self.mp, card=card)
    buyer = accounts.create_buyer(marketplace=self.mp)
    self.session.flush()
    url = self.url_for(
        'accounts.update', marketplace=self.mp, account=buyer)
    payload = {
        'meta': {
            'more-data': 'here',
    },
        'name': 'my new name',
        'email_address': 'new@email.com',
        'card_uri': card_uri,
   }
    data = self.to_json(payload)
    resp = self.client.put(
        url, user=self.mp_owner,
        content_type='application/json', data=data)
    self.assertEqual(resp.status_code, 200)
    print self._format(self.client.last_request, resp)


@scenario
def accounts_promote_buyer(self):
    buyer = accounts.create_buyer(marketplace=self.mp)
    self.session.flush()
    url = self.url_for(
        'accounts.update', marketplace=self.mp, account=buyer)
    payload = accounts.create_payload_person_merchant()
    data = self.to_json(payload)
    resp = self.client.put(
        url, user=self.mp_owner,
        content_type='application/json', data=data)
    self.assertEqual(resp.status_code, 200)
    self.assertItemsEqual(resp.json['roles'], ['buyer', 'merchant'])
    print self._format(self.client.last_request, resp)


@scenario
def api_keys_create(self):
    url = self.url_for('api_keys.create')
    payload = {
        'meta': {
            'some': 'data',
            },
        }
    data = self.to_json(payload)
    resp = self.client.post(
        url, user=self.mp_owner,
        content_type='application/json', data=data)
    self.assertEqual(resp.status_code, 201)
    print self._format(self.client.last_request, resp)


@scenario
def api_keys_update(self):
    api_key = api_keys.create(user=self.mp_owner)
    self.session.flush()
    url = self.url_for('api_keys.update', api_key=api_key)
    payload = {
        'meta': {
            'some': 'different data',
            },
        }
    data = self.to_json(payload)
    resp = self.client.put(
        url, user=self.mp_owner,
        content_type='application/json', data=data)
    self.assertEqual(resp.status_code, 200)
    print self._format(self.client.last_request, resp)


@scenario
def api_keys_show(self):
    api_key = api_keys.create(user=self.mp_owner)
    self.session.flush()
    url = self.url_for('api_keys.show', api_key=api_key)
    resp = self.client.get(url, user=self.mp_owner)
    self.assertEqual(resp.status_code, 200)
    print self._format(self.client.last_request, resp)


@scenario
def api_keys_delete(self):
    api_key = api_keys.create(user=self.mp_owner)
    self.session.flush()
    url = self.url_for('api_keys.delete', api_key=api_key)
    resp = self.client.delete(url, user=self.mp_owner)
    self.assertEqual(resp.status_code, 204)
    print self._format(self.client.last_request, resp)


@scenario
def api_keys_index(self):
    api_keys.create(user=self.mp_owner)
    api_keys.create(user=self.mp_owner)
    api_keys.create(user=self.mp_owner)
    url = self.url_for('api_keys.index')
    resp = self.client.get(url, user=self.mp_owner)
    self.assertEqual(resp.status_code, 200)
    print self._format(self.client.last_request, resp)


@scenario
def debits_index(self):
    transactions.create_debit(
        account=self.account,
        amount=1254
    )
    transactions.create_debit(
        account=self.account,
        amount=431
    )
    self.session.flush()
    url = self.url_for('debits.index', marketplace=self.mp)
    resp = self.client.get(url, user=self.mp_owner)
    self.assertEqual(resp.status_code, 200)
    print self._format(None, resp)


@scenario
def debits_show(self):
    debit = transactions.create_debit(
        account=self.account,
        amount=1254
    )
    self.session.flush()
    url = self.url_for('debits.show', marketplace=self.mp, debit=debit)
    resp = self.client.get(url, user=self.mp_owner)
    self.assertEqual(resp.status_code, 200)
    print self._format(self.client.last_request, resp)


@scenario
def debits_update(self):
    debit = transactions.create_debit(
        account=self.account,
        amount=1254
    )
    self.session.flush()
    url = self.url_for(
        'debits.update', marketplace=self.mp, debit=debit)
    payload = {
        'description': 'my new description',
        'meta': {
            'my-id': '0987654321',
        }
    }
    data = self.to_json(payload)
    resp = self.client.put(
        url,
        content_type='application/json', data=data, user=self.mp_owner)
    self.assertEqual(resp.status_code, 200)
    print self._format(self.client.last_request, resp)


@scenario
def debits_create(self):
    url = self.url_for(
        'debits.create',
        marketplace=self.mp,
        account=self.account
    )
    payload = {
        'amount': 1234,
        'on_behalf_of_uri': self.url_for('accounts.show',
                                         marketplace=self.mp,
                                         account=self.seller)
    }
    data = self.to_json(payload)
    resp = self.client.post(
        url,
        content_type='application/json', data=data, user=self.mp_owner)
    self.assertEqual(resp.status_code, 201)
    print self._format(self.client.last_request, resp)


@scenario
def refunds_show(self):
    debit = transactions.create_debit(
        account=self.account,
        amount=1254,
    )
    refund = transactions.create_refund(debit)
    self.session.flush()
    url = self.url_for('refunds.show', marketplace=self.mp, refund=refund)
    resp = self.client.get(url, user=self.mp_owner)
    self.assertEqual(resp.status_code, 200)
    print self._format(self.client.last_request, resp)


@scenario
def refunds_index(self):
    d1 = transactions.create_debit(
        account=self.account,
        amount=1254
    )
    transactions.create_refund(
        debit=d1,
    )
    d2 = transactions.create_debit(
        account=self.account,
        amount=431
    )

    transactions.create_refund(
        debit=d2,
    )
    self.session.flush()
    url = self.url_for('refunds.index', marketplace=self.mp)
    resp = self.client.get(url, user=self.mp_owner)
    self.assertEqual(resp.status_code, 200)
    print self._format(None, resp)


@scenario
def refunds_update(self):
    debit = transactions.create_debit(
        account=self.account,
        amount=1254
    )
    refund = transactions.create_refund(
        debit=debit,
    )
    self.session.flush()
    url = self.url_for(
        'refunds.update', marketplace=self.mp, refund=refund)
    payload = {
        'description': 'my new description',
        'meta': {
            'my-id': '0987654321',
        }
    }
    data = self.to_json(payload)
    resp = self.client.put(
        url,
        content_type='application/json', data=data, user=self.mp_owner)
    self.assertEqual(resp.status_code, 200)
    print self._format(self.client.last_request, resp)


@scenario
def refunds_create(self):
    debit = transactions.create_debit(
        account=self.account,
        amount=1254,
    )
    self.session.flush()
    debit_uri = self.url_for(
        'debits.show', marketplace=self.mp, debit=debit)

    url = self.url_for(
        'refunds.create',
        marketplace=self.mp, account=self.account
    )
    payload = {
        'amount': 1234,
        'debit_uri': debit_uri,
    }
    data = self.to_json(payload)
    resp = self.client.post(
        url,
        content_type='application/json', data=data, user=self.mp_owner)
    self.assertEqual(resp.status_code, 201)
    print self._format(self.client.last_request, resp)


@scenario
def debit_refunds_create(self):
    debit = transactions.create_debit(
        account=self.account,
        amount=1254,
    )
    self.session.flush()
    debit_refunds_uri = self.url_for(
        'debit_refunds.create',
        marketplace=self.mp,
        debit=debit
    )

    resp = self.client.post(
        debit_refunds_uri, content_type='application/json',
        data=self.to_json({}), user=self.mp_owner
    )
    self.assertEqual(resp.status_code, 201)
    print self._format(self.client.last_request, resp)


@scenario
def holds_create(self):
    url = self.url_for(
        'holds.create', marketplace=self.mp, account=self.buyer)
    payload = {
        'amount': 3421,
        'description': 'Something tasty',
        'meta': {
            'id': '#12312123123',
        }
    }
    data = self.to_json(payload)
    resp = self.client.post(
        url, user=self.mp_owner,
        data=data, content_type='application/json')
    self.assertEqual(resp.status_code, 201)
    print self._format(self.client.last_request, resp)


@scenario
def holds_show(self):
    hold = holds.create(
        account=self.buyer, amount=1233, description='Something sour')
    self.session.flush()
    url = self.url_for(
        'holds.show', marketplace=self.mp, hold=hold)
    resp = self.client.get(url, user=self.mp_owner)
    self.assertEqual(resp.status_code, 200)
    print self._format(self.client.last_request, resp)


@scenario
def holds_index(self):
    holds.create(
        account=self.buyer, amount=1233, description='Something sweet')
    holds.create(
        account=self.buyer, amount=3344, description='Something sour')
    holds.create(
        account=self.buyer, amount=6754, description='Something spicy')
    holds.create(
        account=self.buyer, amount=1322, description='Something tangy')
    self.session.flush()
    url = self.url_for(
        'holds.index', marketplace=self.mp, account=self.buyer)
    resp = self.client.get(url, user=self.mp_owner)
    self.assertEqual(resp.status_code, 200)
    print self._format(self.client.last_request, resp)


@scenario
def holds_update(self):
    hold = holds.create(
        account=self.buyer, amount=1233, description='Something sour')
    self.session.flush()
    url = self.url_for(
        'holds.show', marketplace=self.mp, hold=hold)
    payload = {
        'description': 'Something really tasty',
        'meta': {
            'the-address': '123 Fake Street',
        }
    }
    data = self.to_json(payload)
    resp = self.client.put(
        url, user=self.mp_owner,
        data=data, content_type='application/json')
    self.assertEqual(resp.status_code, 200)
    print self._format(self.client.last_request, resp)


@scenario
def holds_capture(self):
    hold = holds.create(
        account=self.buyer, amount=1233, description='Something sour')
    self.session.flush()
    hold_url = self.url_for(
        'holds.show', marketplace=self.mp, hold=hold)
    url = self.url_for(
        'debits.create', marketplace=self.mp, account=self.buyer)
    payload = {
        'hold_uri': hold_url,
    }
    data = self.to_json(payload)
    resp = self.client.post(
    url, user=self.mp_owner,
    data=data, content_type='application/json')
    self.assertEqual(resp.status_code, 201)
    print self._format(self.client.last_request, resp)


@scenario
def holds_void(self):
    hold = holds.create(
        account=self.buyer, amount=1233, description='Something sour')
    self.session.flush()
    url = self.url_for(
        'holds.show', marketplace=self.mp, hold=hold)
    payload = {
        'is_void': True,
        'meta': {
            'reason': 'Customer request',
        }
    }
    data = self.to_json(payload)
    resp = self.client.put(
        url, user=self.mp_owner,
        data=data, content_type='application/json')
    self.assertEqual(resp.status_code, 200)
    print self._format(self.client.last_request, resp)


@scenario
def marketplaces_create(self):
    user = users.create()
    user.create_api_key()
    merchants.create_business_merchant(user=user)
    self.session.flush()
    url = self.url_for('marketplaces.create')
    payload = {
        'support_email_address': 'support@example.com',
        'name': 'Seller of things',
        'domain_url': 'example.com',
        'support_phone_number': '+12125551212',
        'meta': {
            'my-useful-data': 'abc123'
        }
    }
    data = self.to_json(payload)
    resp = self.client.post(
        url, user=user,
        data=data, content_type='application/json')
    self.assertEqual(resp.status_code, 201)
    print self._format(self.client.last_request, resp)


@scenario
def marketplaces_show(self):
    url = self.url_for('marketplaces.show', marketplace=self.mp)
    resp = self.client.get(url, user=self.mp_owner)
    self.assertEqual(resp.status_code, 200)
    print self._format(self.client.last_request, resp)


@scenario
def marketplaces_update(self):
    url = self.url_for('marketplaces.show', marketplace=self.mp)
    payload = {
        'support_email_address': 'faster-support@example.com',
        'name': 'Seller of thingz',
        'support_phone_number': '+18185551212',
        'meta': {
            'even-more-useful-data': '321cba'
        }
    }
    data = self.to_json(payload)
    resp = self.client.put(url, user=self.mp_owner,
        data=data, content_type='application/json')
    self.assertEqual(resp.status_code, 200)
    print self._format(self.client.last_request, resp)


@scenario
def marketplaces_index(self):
    url = self.url_for('marketplaces.index')
    resp = self.client.get(url, user=self.mp_owner)
    self.assertEqual(resp.status_code, 200)
    print self._format(self.client.last_request, resp)


@scenario
def merchants_show(self):
    url = self.url_for(
        'merchants.show', merchant=self.mp.owner_account.merchant)
    resp = self.client.get(url, user=self.mp_owner)
    self.assertEqual(resp.status_code, 200)
    print self._format(self.client.last_request, resp)


@scenario
def merchants_update(self):
    url = self.url_for(
        'merchants.show', merchant=self.account.merchant)
    payload = {
        'name': 'Willie',
        'email_address': 'will@ie.com',
        'phone_number': '+16501112222',
        'meta': {
            'location': '121.121'
        },
        'bank_account': {
            'account_number': '345345345',
            'routing_number': '325182797',
            'name': 'Willie',
            'account_type': 'savings',
        }
    }
    data = self.to_json(payload)
    resp = self.client.put(
        url, user=self.mp_owner,
        data=data, content_type='application/json')
    self.assertEqual(resp.status_code, 200)
    print self._format(self.client.last_request, resp)


@scenario
def merchants_index(self):
    url = self.url_for('merchants.index')
    resp = self.client.get(url, user=self.mp_owner)
    self.assertEqual(resp.status_code, 200)
    print self._format(self.client.last_request, resp)


@scenario
def tranasctions_index(self):
    transactions.create_credit(amount=245, account=self.account)
    transactions.create_debit(amount=5544, account=self.buyer)
    holds.create(amount=123, account=self.buyer)
    hold = holds.create(amount=343, account=self.buyer)
    debit = hold.capture()
    debit.refund()
    hold = holds.create(amount=2455, account=self.buyer)
    hold.void()
    self.session.flush()
    url = self.url_for('transactions.index', marketplace=self.mp)
    resp = self.client.get(url, user=self.mp_owner)
    self.assertEqual(resp.status_code, 200)
    print self._format(self.client.last_request, resp)


@scenario
def events_index(self, enqueue):
    items = []
    enqueue.side_effect = items.append

    transactions.create_credit(amount=245, account=self.account)
    transactions.create_debit(amount=5544, account=self.buyer)
    holds.create(amount=123, account=self.buyer)
    hold = holds.create(amount=343, account=self.buyer)
    debit = hold.capture()
    debit.refund()
    hold = holds.create(amount=2455, account=self.buyer)
    hold.void()
    self.session.flush()
    self.session.commit()
    for item in items[::2]:
        payload = messages.views.serialize(item)
        audits.on_audit_message(**payload)
    url = self.url_for('events.index')
    resp = self.client.get(url, user=self.mp_owner)
    self.assertEqual(resp.status_code, 200)
    print self._format(self.client.last_request, resp)


@scenario
def events_show(self, enqueue):
    items = []
    enqueue.side_effect = items.append

    transactions.create_credit(amount=245, account=self.account)
    transactions.create_debit(amount=5544, account=self.buyer)
    holds.create(amount=123, account=self.buyer)
    hold = holds.create(amount=343, account=self.buyer)
    debit = hold.capture()
    debit.refund()
    hold = holds.create(amount=2455, account=self.buyer)
    hold.void()
    self.session.flush()
    self.session.commit()
    audit_event = None
    for item in items[::2]:
        payload = messages.views.serialize(item)
        audit_event = audits.on_audit_message(**payload)
    self.session.flush()
    self.session.commit()
    url = self.url_for('events.show', event=audit_event)
    resp = self.client.get(url, user=self.mp_owner)
    self.assertEqual(resp.status_code, 200)
    print self._format(self.client.last_request, resp)


@scenario
def event_callbacks_index(self, enqueue):
    items = []
    enqueue.side_effect = items.append

    callback = callbacks.create(self.mp)
    transactions.create_credit(amount=245, account=self.account)
    transactions.create_debit(amount=5544, account=self.buyer)
    holds.create(amount=123, account=self.buyer)
    hold = holds.create(amount=343, account=self.buyer)
    debit = hold.capture()
    debit.refund()
    hold = holds.create(amount=2455, account=self.buyer)
    hold.void()
    self.session.flush()
    self.session.commit()
    audit_event = None
    for item in items[::2]:
        payload = messages.views.serialize(item)
        audit_event = audits.on_audit_message(**payload)
    url = self.url_for('event_callbacks.index',
                       event=audit_event,
                       callback=callback)
    resp = self.client.get(url, user=self.mp_owner)
    self.assertEqual(resp.status_code, 200)
    print self._format(self.client.last_request, resp)


@scenario
def event_callbacks_show(self, enqueue):
    items = []
    enqueue.side_effect = items.append

    callback = callbacks.create(self.mp)
    transactions.create_credit(amount=245, account=self.account)
    transactions.create_debit(amount=5544, account=self.buyer)
    holds.create(amount=123, account=self.buyer)
    hold = holds.create(amount=343, account=self.buyer)
    debit = hold.capture()
    debit.refund()
    hold = holds.create(amount=2455, account=self.buyer)
    hold.void()
    self.session.flush()
    self.session.commit()
    audit_event = None
    for item in items[::2]:
        payload = messages.views.serialize(item)
        audit_event = audits.on_audit_message(**payload)
    self.session.flush()
    self.session.commit()
    url = self.url_for('event_callbacks.show',
                       event=audit_event,
                       callback=callback)
    resp = self.client.get(url, user=self.mp_owner)
    self.assertEqual(resp.status_code, 200)
    print self._format(self.client.last_request, resp)


@scenario
def callbacks_index(self):
    callbacks.create(self.mp)
    self.session.commit()
    url = self.url_for('marketplace_callbacks.index', marketplace=self.mp)
    resp = self.client.get(url, user=self.mp_owner)
    self.assertEqual(resp.status_code, 200)
    print self._format(self.client.last_request, resp)


@scenario
def callbacks_show(self):
    callback = callbacks.create(self.mp)
    self.session.commit()
    url = self.url_for('marketplace_callbacks.show',
                       marketplace=self.mp,
                       callback=callback)
    resp = self.client.get(url, user=self.mp_owner)
    self.assertEqual(resp.status_code, 200)
    print self._format(self.client.last_request, resp)


@scenario
def callbacks_create(self):
    url = self.url_for('marketplace_callbacks.create',
                       marketplace=self.mp)
    resp = self.client.post(url, user=self.mp_owner,
                            data={
                                'url': 'https://www.example.com',
                                })
    self.assertEqual(resp.status_code, 201)
    print self._format(self.client.last_request, resp)


@scenario
def callbacks_delete(self):
    callback = callbacks.create(self.mp)
    self.session.commit()
    url = self.url_for('marketplace_callbacks.delete',
                       marketplace=self.mp,
                       callback=callback)
    resp = self.client.delete(url, user=self.mp_owner)
    self.assertEqual(resp.status_code, 204)
    print self._format(self.client.last_request, resp)


@scenario
def bank_account_authentications_index(self):
    auth = bank_accounts.create_authentication(marketplace=self.mp)
    self.session.commit()
    url = self.url_for('bank_account_authentications.index',
                       bank_account=auth.bank_account)
    resp = self.client.get(url, user=self.mp_owner)
    self.assertEqual(resp.status_code, 200)
    print self._format(self.client.last_request, resp)


@scenario
def bank_account_authentications_show(self):
    auth = bank_accounts.create_authentication(marketplace=self.mp)
    self.session.commit()
    url = self.url_for('bank_account_authentications.show_current',
                       bank_account=auth.bank_account)
    resp = self.client.get(url, user=self.mp_owner)
    self.assertEqual(resp.status_code, 200)
    print self._format(self.client.last_request, resp)


@scenario
def bank_account_authentications_create(self):
    bank_account = bank_accounts.create(marketplace=self.mp)
    self.session.commit()
    url = self.url_for('bank_account_authentications.create',
                       bank_account=bank_account)
    resp = self.client.post(url, user=self.mp_owner, data={})
    self.assertEqual(resp.status_code, 201)
    print self._format(self.client.last_request, resp)


@scenario
def bank_account_authentications_update(self):
    self.mp.production = False
    auth = bank_accounts.create_authentication(marketplace=self.mp)
    payload = {'amount_1': 11, 'amount_2': 22}
    self.session.commit()
    url = self.url_for('bank_account_authentications.update_current',
                       bank_account=auth.bank_account)
    resp = self.client.put(url, user=self.mp_owner, data=payload)
    self.assertEqual(resp.status_code, 200)
    print self._format(self.client.last_request, resp)


SCENARIOS = dict(
    (v.scenario, v)
    for k, v in globals().itermitems()
    if hasattr(v, '__call__') and hasattr(v, 'scenario')
)


# main

class LogLevelAction(argparse.Action):

    def __call__(self, parser, namespace, values, option_string=None):
        level = getattr(logging, values.upper())
        setattr(namespace, self.dest, level)


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
    return parser


def main():
    parser = create_arg_parser()
    args = parser.parse_args()

    logger = logging.getLogger()
    formatter = logging.Formatter('%(asctime)s : %(name)s : %(message)s')
    handler = logging.StreamHandler(sys.stderr)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(args.log_level)

    ctx = Context.load(open(args.cache, 'r'),) if args.cache else Context()
    for name in args:
        if name not in SCENARIOS:
            raise ValueError('Invalid scenario "{}"'.format(name))
        req, resp = SCENARIOS[name](ctx)
        print ctx.format(req, resp)


if __name__ == '__main__':
    main()
