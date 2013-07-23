
bank_account = json.loads(
    storage['bank_account_create']['response']
)

request = {
    'uri': bank_account['verifications_uri'],
    'bank_account_uri': bank_account['uri'],
    'payload': { 'none': '' }
}
