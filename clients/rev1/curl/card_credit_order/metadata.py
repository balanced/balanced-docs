card = json.loads(
    storage['card_create_creditable']['response']
)

card_credits_href = card['links']['cards.credits'].replace('{cards.id}', card['cards'][0]['id'])

order = json.loads(
    storage['order_create']['response']
)['orders'][0]


request = {
    'uri': card_credits_href,
    'payload': {
        'amount': 5000,
        'order': order['href'],
    },
    'card_href': card_credits_href,
    'order_href': order['href'],
}