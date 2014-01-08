customer = json.loads(
    storage['customer_create']['response']
)

card = json.loads(
    storage['card_create']['response']
)

request = {
    'uri': card['cards'][0]['href'],
    'payload': {
        'customer': customer['customers'][0]['href'],
    }
}
