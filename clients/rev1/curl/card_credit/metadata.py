card = json.loads(
    storage['card_create_creditable']['response']
)

card_credits_href = card['links']['cards.credits'].replace('{cards.id}', card['cards'][0]['id'])

request = {
    'uri': card_credits_href,
    'payload': {
        'amount': 5000,
        'description': 'Some descriptive text for the debit in the dashboard',
    },
    'card_href': card['cards'][0]['href']
}