storage.pop('card_create', None)

card = json.loads(
    storage['card_create']['response']
)

request = {
    'uri': ctx.marketplace.accounts_uri,
    'payload': {
        'card_uri': card['uri'],
    },
}
