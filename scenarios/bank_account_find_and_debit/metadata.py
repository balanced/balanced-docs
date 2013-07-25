import balanced

balanced.configure(storage['api_key'])

bank_account = json.loads(
    storage['bank_account_create']['response']
)

ba = balanced.BankAccount.find(bank_account['uri'])
verification = ba.verify()
verification.amount_1 = 1
verification.amount_2 = 1
verification.save()
ba = balanced.BankAccount.find(ba.uri)

request = {
    'id': ba.id,
    'uri': ba.uri,
    'debits_uri': storage['api_location'] + ba.debits_uri,
    'amount': 17451,
}
