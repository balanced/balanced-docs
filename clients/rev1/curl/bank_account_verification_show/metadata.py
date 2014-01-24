bank_account_verification = json.loads(
    storage['bank_account_verification_create']['response']
)['bank_account_verifications'][0]

request = {
    'uri': bank_account_verification['href']
}