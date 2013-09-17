customer = json.loads(
    storage['customer_create']['response']
)

request = {
    'customer_uri': customer['uri'],
    'uri': customer['credits_uri'],
    'payload': {
        'amount': 100,
    },
}
