import requests

credit = json.loads(
    storage['account_credit']['response']
)
account_id = credit['credits'][0]['links']['destination']
account = requests.get(ctx.storage['api_location'] + "/accounts/" + account_id,
                       headers={'Accept-Type': ctx.storage.get('accept_type', '*/*')},
                       auth=(ctx.storage['secret'], '')).json()
customer_id = account['accounts'][0]['links']['customer']
bank_accounts = requests.get(ctx.storage['api_location'] + "/customers/" + customer_id + "/bank_accounts",
                             headers={'Accept-Type': ctx.storage.get('accept_type', '*/*')},
                             auth=(ctx.storage['secret'], '')).json()
account_settlements_href = "/accounts/" + account_id + "/settlements"

request = {
    'uri': account_settlements_href,
    'payload': {
        'funding_instrument': bank_accounts['bank_accounts'][0]['href'],
        'description': 'Payout A',
        'appears_on_statement_as': 'ThingsCo',
        "meta": {
            "group": "alpha"
        }
    },
    'account_href': "/accounts/" + account_id
}