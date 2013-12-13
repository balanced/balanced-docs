card_hold = json.loads(
    storage['card_hold_create']['response']
)['card_holds'][0]

#print card_hold

#card_hold_debit_uri = card_hold['links']['card_holds.debits'].replace('{card_holds.id}', card_hold['card_holds'][0]['id'])

request = {
    'uri': card_hold['href'],
    'payload': {
        'is_void': 'true'
    }
}