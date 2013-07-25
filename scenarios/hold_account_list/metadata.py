if ctx.storage['api_rev'] == 'rev0':
    account = json.loads(
        storage['account_create_buyer']['response']
    )
else:
    account = json.loads(
        storage['customer_add_card']['response']
    )


request = {
    'uri': account['holds_uri'],
    'account_uri': account['uri'],
}
