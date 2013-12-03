ctx.storage.pop('customer_create', None)

customer = json.loads(
    storage['customer_create']['response']
)

ctx.storage.pop('bank_account_create', None)

bank_account = json.loads(
    ctx.storage['bank_account_create']['response']
)

print bank_account

request = {
    'uri': customer['customers'][0]['href'],
    'bank_account_verifications_uri': bank_account['verifications_uri'],
    'payload': {
        'bank_account_uri': bank_account['uri'],
    }
}
