bank_accounts = json.loads(
    storage['bank_account_list']['response']
)

bank_account_credits_uri = bank_accounts['links']['bank_accounts.credits'].replace('{bank_accounts.id}', bank_accounts['bank_accounts'][0]['id'])

request = {
  'uri': bank_account_credits_uri,
  'payload': {
      'amount': 2000,
  },
}
