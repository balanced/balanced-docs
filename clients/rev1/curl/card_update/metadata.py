card = json.loads(
    storage['card_create']['response']
)['cards'][0]

request = {
    'uri': card['href'],
    'payload': {
        'meta': {
            'my-own-customer-id': '12345',
            'facebook.user_id': '0192837465',
            'twitter.id': '1234987650',
        },
    }
}
