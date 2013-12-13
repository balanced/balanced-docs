card = json.loads(
    storage['card_create']['response']
)

card_holds_uri = card['links']['cards.card_holds'].replace('{cards.id}', card['cards'][0]['id'])

request = {
    'uri': card_holds_uri,
    'payload': {
        'amount': 5000,
        'description': 'Some descriptive text for the debit in the dashboard'
    }
}
