if ctx.storage['api_rev'] == 'rev0':
    account = json.loads(
        storage['account_create_merchant']['response']
    )
else:
    account = json.loads(
        storage['customer_add_bank_account']['response']
    )


request = {
    'account_uri': account['uri'],
    'uri': account['credits_uri'],
    'payload': {
        'amount': 100,
    },
}
