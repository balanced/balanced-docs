ctx.storage.pop('customer_create', None)

customer = json.loads(
    storage['customer_create']['response']
)

ctx.storage.pop('card_create', None)

card = json.loads(
    storage['card_create']['response']
)

request = {
    'uri': customer['uri'],
    'card_uri': card['uri'],
    'payload': {
        'card_uri': card['uri'],
    }
}
