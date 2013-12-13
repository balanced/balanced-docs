credit = json.loads(
    storage['bank_account_credit']['response']
)['credits'][0]

request = {
    'payload': {
        'description': 'New description for credit',
        'meta': {
          'facebook.id': '1234567890',
          'anykey': 'valuegoeshere',
        },
    },
    'uri': credit['href']
}