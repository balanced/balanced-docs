ctx.storage.pop('card_hold_create', None)

card_hold = json.loads(
    storage['card_hold_create']['response']
)['card_holds'][0]

request = {
    'uri': card_hold['href'],
    'payload': {
        'is_void': 'true'
    }
}