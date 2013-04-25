bank_accounts = json.loads(
    storage['bank_account_list']['response']['content']
)

bank_account = bank_accounts['items'][-1]

request = {
    'uri': bank_account['uri'],
}
