import requests

debit = json.loads(
    storage['debit_order']['response']
)

order_href = debit['links']['debits.order'].replace('{debits.order}', debit['debits'][0]['links']['order'])

order = requests.get(ctx.storage['api_location'] + order_href,
                     headers={'Accept-Type': ctx.storage.get('accept_type', '*/*')},
                     auth=(ctx.storage['secret'], '')).json()

order_merchant_accounts_href = "/customers/" + order['orders'][0]['links']['merchant'] \
     + "/accounts?type%5Bcontains%5D=payable"


accounts = requests.get(ctx.storage['api_location'] + order_merchant_accounts_href,
                     headers={'Accept-Type': ctx.storage.get('accept_type', '*/*')},
                     auth=(ctx.storage['secret'], '')).json()

href = accounts['accounts'][0]['href']
account_credits_href = accounts['links']['accounts.credits'].replace('{accounts.id}', accounts['accounts'][0]['id'])

request = {
    'uri': account_credits_href,
    'payload': {
        'amount': 1000,
        'description': 'A simple credit',
        'appears_on_statement_as': 'ThingsCo',
        'order': order['orders'][0]['href'],
        "meta": {
            "rating": 8
        }
    },
    'href': href,
    'account_href': accounts['accounts'][0]['href']
}
