verification = json.loads(
    storage['bank_account_verification_create']['response']
)

request = {
    'uri': verification['uri'],
    'payload': {
        'amount_1': 1,
        'amount_2': 1,
    }
}
