bank_accounts = json.loads(
    storage['bank_account_list']['response']
)

request = {
    'uri': bank_accounts['bank_accounts'][0]['href'],
}
