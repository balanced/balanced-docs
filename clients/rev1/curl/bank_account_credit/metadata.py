bank_accounts = json.loads(
    storage['bank_account_list']['response']
)

customer = json.loads(
    storage['customer_add_bank_account']['response']
)

bank_account_href = storage['customer_add_bank_account']['request']['payload']['bank_account_href']

print bank_accounts['links']['bank_accounts.credits']
print bank_account_href

request = {
  'uri': bank_account_href + '/credits',
  'payload': {
      'amount': 2000,
  },
  'bank_account_href': bank_account_href
}
