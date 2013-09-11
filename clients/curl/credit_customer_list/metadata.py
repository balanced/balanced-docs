customer = json.loads(
    storage['customer_create']['response']
)

request = {
    'account_uri': customer['uri'],
    'uri': customer['credits_uri'],
    'payload': {
        'amount': 100,
    },
}
