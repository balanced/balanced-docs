ctx.storage.pop('customer_create', None)

customer = json.loads(
    storage['customer_create']['response']
)

ctx.storage.pop('card_create', None)

card = json.loads(
    storage['card_create']['response']
)

print card

request = {
    'uri': customer['customers'][0]['href'],
    'card_uri': card['cards'][0]['href'],
    'payload': {
        'card_uri': card['cards'][0]['href'],
    }
}
