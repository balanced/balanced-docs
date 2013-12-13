credit = json.loads(
    storage['credit_create_existing_bank_account']['response']
)
bank_acct = credit['bank_account']

request = {
  'uri': bank_acct['uri'],
}
