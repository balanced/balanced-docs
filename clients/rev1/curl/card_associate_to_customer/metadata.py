ctx.storage.pop('card_create_creditable', None)

customer = json.loads(
    storage['customer_create']['response']
)

card = json.loads(
    storage['card_create_creditable']['response']
)

request = {
    'uri': card['cards'][0]['href'],
    'payload': {
        'customer': customer['customers'][0]['href'],
    }
}
