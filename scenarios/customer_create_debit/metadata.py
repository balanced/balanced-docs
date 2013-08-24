ctx.storage.pop('customer_add_card', None)

customer = json.loads(
    storage['customer_add_card']['response']
)

request = {
    'uri': customer['debits_uri'],
    'customer_uri': customer['uri'],
    'payload': {
        'amount': 5000,
        'appears_on_statement_as': 'Statement text',
        'description': 'Some descriptive text for the debit in the dashboard',
    }
}