account = json.loads(
    storage['account_create_merchant']['response']['content']
)


request = {
    'account_uri': account['uri'],
    'uri': account['credits_uri'],
    'payload': {
        'amount': 100,
    },
}
