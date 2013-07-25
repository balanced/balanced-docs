
rev = ctx.storage['api_rev']
request = {
    'uri': ctx.marketplace.cards_uri,
    'payload': {
        'card_number' if rev == 'rev0' else 'number': '5105105105105100',
        'expiration_month' if rev == 'rev0' else 'month': '12',
        'expiration_year' if rev == 'rev0' else 'year': '2020',
        'security_code' if rev == 'rev0' else 'cvv': '123',
    },
}
