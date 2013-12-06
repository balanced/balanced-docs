ctx.storage.pop('customer_create', None)

customer = json.loads(
    storage['customer_create']['response']
)

ctx.storage.pop('bank_account_create', None)

bank_account = json.loads(
    ctx.storage['bank_account_create']['response']
)

verifications_uri = bank_account['links']['bank_accounts.bank_account_verifications'].replace('{customers.id}', customer['customers'][0]['id'])

request = {
    'uri': customer['customers'][0]['href'],
    'bank_account_verifications_uri': ['verifications.uri'],
    'payload': {
        'bank_account_uri': bank_account['bank_accounts'][0]['href'],
    }
}
