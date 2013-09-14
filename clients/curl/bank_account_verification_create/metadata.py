bank_account = json.loads(
    storage['customer_add_bank_account']['response']
)

bank_account_request = storage['customer_add_bank_account']['request']

request = {
    'uri': bank_account_request['bank_account_verifications_uri'],
    'bank_account_uri': bank_account_request['payload']['bank_account_uri']
}
