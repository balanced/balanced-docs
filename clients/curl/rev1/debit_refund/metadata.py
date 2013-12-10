debit = json.loads(
    storage['card_debit']['response']
)

refund_uri = debit['links']['debits.refunds'].replace('{debits.id}', debit['debits'][0]['id'])

request = {
    'uri': refund_uri
}