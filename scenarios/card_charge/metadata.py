request = {
    'uri': ctx.marketplace.cards_uri,
    'api': storage['api_location'],
    'url': storage['api_location'] + ctx.marketplace.cards_uri,
    'payload': {
        'card_number': '5105105105105100',
        'expiration_month': '12',
        'expiration_year': '2020',
        'security_code': '123',
        'amount': '1000',
        },
    }
