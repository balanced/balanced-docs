#storage.pop('credit_create', None)

credit = json.loads(
    #storage['credit_create']['response']
    storage['credit_create_new_bank_account']['response']
)

request = {
    'payload': {
        'description': 'no money for you',
        'meta': {
            'merchant.feedback': 'positive',
        }
    },
    'uri': credit['reversals_uri'],
    'credit_uri': credit['uri'],
}
