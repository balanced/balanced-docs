bank_account = json.loads(
    storage['bank_account_create']['response']['content']
)

request = {
    'uri': bank_account['uri'],
}
