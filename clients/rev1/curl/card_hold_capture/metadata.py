card_hold = json.loads(
    storage['card_hold_create']['response']
)

card_hold_debit_uri = card_hold['links']['card_holds.debits'].replace('{card_holds.id}', card_hold['card_holds'][0]['id'])

request = {
    'uri': card_hold_debit_uri,
    'payload': {
        'appears_on_statement_as': 'ShowsUpOnStmt',
        'description': 'Some descriptive text for the debit in the dashboard'
    }
}