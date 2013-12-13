debit = json.loads(
    storage['card_debit']['response']
)

request = {
    'uri': debit['uri'],
}
