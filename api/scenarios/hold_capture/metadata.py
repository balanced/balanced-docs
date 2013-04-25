buyer = json.loads(
    storage['account_create_buyer']['response']['content']
)

storage.pop('hold_create', None)

hold = json.loads(
    storage['hold_create']['response']['content']
)

request = {
    'payload': {
        'appears_on_statement_as': 'ShowsUpOnStmt',
        'description': 'Some descriptive text for the debit in the dashboard',
        'hold_uri': hold['uri'],
    },
    'debits_uri': buyer['debits_uri'],
    'hold_uri': hold['uri'],
}