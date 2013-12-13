#buyer = json.loads(
#    storage['create_customer']['response']
#)

#storage.pop('hold_create', None)

hold = json.loads(
    storage['hold_create']['response']
)

debits_uri = storage['hold_create']['request']['debits_uri']

request = {
    'payload': {
        'appears_on_statement_as': 'ShowsUpOnStmt',
        'description': 'Some descriptive text for the debit in the dashboard'
    },
    'debits_uri': debits_uri,
    'hold_uri': hold['uri'],
}