account = json.loads(
    storage['account_create_buyer']['response']['content']
)

request = {
    'uri': account['uri'],
    'debits_uri': account['debits_uri'],
}
