customer = json.loads(
    storage['customer_create']['response']
)

card = json.loads(
    storage['card_create']['response']
)

request = {
    'uri': customer['customers'][0]['href'],
    'payload': {
        'card_href': card['cards'][0]['href'],
    }
}
