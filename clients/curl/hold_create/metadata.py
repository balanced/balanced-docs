ctx.storage.pop('customer_add_card', None)

customer = json.loads(
    storage['customer_add_card']['response']
)

card_uri = storage['customer_add_card']['request']['card_uri']

request = {
    'uri': ctx.marketplace.holds_uri,
    'payload': {
        'amount': 5000,
        'description': 'Some descriptive text for the debit in the dashboard',
        'source_uri': card_uri
    },
    'customer_uri': customer['uri'],
    'debits_uri': customer['debits_uri']
}
