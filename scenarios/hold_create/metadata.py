ctx.storage.pop('customer_add_card', None)

customer = json.loads(
    storage['customer_add_card']['response']
)

request = {
    'uri': customer['holds_uri'],
    'payload': {
        'amount': 5000,
        'description': 'Some descriptive text for the debit in the dashboard',
    },
    'customer_uri': customer['uri'],
}
