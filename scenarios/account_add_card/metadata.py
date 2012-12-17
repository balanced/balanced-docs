storage.pop('account_create_buyer', None)

account_var = json.loads(
    storage['account_create_buyer']['response']['content']
)

storage.pop('card_create', None)

card = json.loads(
    storage['card_create']['response']['content']
)

request = {
    'uri': account_var['uri'],
    'payload': {
        'card_uri': card['uri'],
    }
}
