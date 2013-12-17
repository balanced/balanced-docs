card_hold = json.loads(
    storage['card_hold_create']['response']
)['card_holds'][0]

request = {
    'uri': card_hold['href'],
    'payload': {
        'description': 'update this description',
        'meta': {
            'holding.for': 'user1',
            'meaningful.key': 'some.value',
        }
    }
}
