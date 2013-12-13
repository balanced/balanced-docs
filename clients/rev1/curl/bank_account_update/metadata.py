bank_account = json.loads(
    storage['bank_account_create']['response']
)['bank_accounts'][0]

request = {
    'uri': bank_account['href'],
    'payload': {
        'meta': {
            'my-own-customer-id': '12345',
            'facebook.user_id': '0192837465',
            'twitter.id': '1234987650'
        }
    }
}
