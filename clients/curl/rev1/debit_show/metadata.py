debit = json.loads(
    storage['card_debit']['response']
)['debits'][0]

request = {
    'uri': debit['href'],
}
