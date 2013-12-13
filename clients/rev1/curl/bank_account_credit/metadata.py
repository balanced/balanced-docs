bank_accounts = json.loads(
    storage['bank_account_list']['response']
)

bank_account_credits_href = bank_accounts['links']['bank_accounts.credits'].replace('{bank_accounts.id}', bank_accounts['bank_accounts'][0]['id'])

request = {
  'uri': bank_account_credits_href,
  'payload': {
      'amount': 2000,
  },
  'bank_account_href': bank_accounts['bank_accounts'][0]['href']
}
