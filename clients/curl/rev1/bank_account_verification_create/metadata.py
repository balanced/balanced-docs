bank_account = json.loads(
    storage['bank_account_create']['response']
)

uri = bank_account['links']['bank_accounts.bank_account_verifications'].replace('{bank_accounts.id}',
                                                                            bank_account['bank_accounts'][0]['id'])

request = {
    'uri': uri,
    'bank_account_uri': bank_account['bank_accounts'][0]['href']
}
