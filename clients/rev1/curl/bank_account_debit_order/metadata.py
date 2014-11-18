bav_response = json.loads(
    storage['bank_account_verification_update']['response']
)

bank_account_href = bav_response['links']['bank_account_verifications.bank_account'].replace('{bank_account_verifications.bank_account}', bav_response['bank_account_verifications'][0]['links']['bank_account'])

order = json.loads(
    storage['order_create']['response']
)['orders'][0]


request = {
    'uri': bank_account_href + '/debits',
    'payload': {
        'amount': 5000,
        'order': order['href'],
    },
    'bank_account_href': bank_account_href,
    'order_href': order['href'],
}