customer = json.loads(
    storage['customer_add_card']['response']
)

request = {
    'payload': {
        'amount': 5000,
        'description': 'Some descriptive text for the debit in the dashboard',
    },
    'holds_uri': customer['holds_uri'],
    'customer_uri': customer['uri']
}
