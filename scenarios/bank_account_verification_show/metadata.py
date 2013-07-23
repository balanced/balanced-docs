
verification = json.loads(
    storage['bank_account_verification_create']['response']
)

request = {
    'uri': verification['uri'],
}
