storage.pop('card_debit')

debit = json.loads(
    storage['card_debit']['response']
)

request = {
    'refunds_uri': debit['refunds_uri'],
    'debit_uri': debit['uri'],
}