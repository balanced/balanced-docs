bav_response = json.loads(
    storage['bank_account_verification_update']['response']
)

bank_account_href = bav_response['links']['bank_account_verifications.bank_account'].replace('{bank_account_verifications.bank_account}', bav_response['bank_account_verifications'][0]['links']['bank_account']) + '/debits'

request = {
    'uri': bank_account_href,
    'payload': {
        'amount': 5000,
        'appears_on_statement_as': 'Statement text',
        'description': 'Some descriptive text for the debit in the dashboard',
    },
    'bank_account_href': bank_account_href
}