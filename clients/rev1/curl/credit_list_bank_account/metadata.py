bank_accounts = json.loads(
    storage['bank_account_credit']['response']
)

request = {
  'uri': '/bank_accounts/' + bank_accounts['credits'][0]['links']['destination'] + '/credits',
  'bank_account_href': '/bank_accounts/' + bank_accounts['credits'][0]['links']['destination']
}
