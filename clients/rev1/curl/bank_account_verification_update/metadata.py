bav_response = json.loads(
    storage['bank_account_verification_create']['response']
)['bank_account_verifications'][0]

request = {
    'uri': bav_response['href'],
    'payload': {
        'amount_1': 1,
        'amount_2': 1
    }
}