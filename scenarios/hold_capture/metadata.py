customer = json.loads(
    storage['customer_add_card']['response']
)

storage.pop('hold_create', None)

hold = json.loads(
    storage['hold_create']['response']
)

request = {
    'payload': {
        'appears_on_statement_as': 'ShowsUpOnStmt',
        'description': 'Some descriptive text for the debit in the dashboard',
        'hold_uri': hold['uri'],
    },
    'debits_uri': customer['debits_uri'],
    'hold_uri': hold['uri'],
}
