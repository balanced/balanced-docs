ctx.storage.pop('card_debit', None)

debit = json.loads(
    storage['card_debit']['response']
)

request = {
    'uri': debit['links']['debits.refunds'].replace('{debits.id}', debit['debits'][0]['id']),
    'payload': {
        'description': 'Refund for Order #1111',
        'meta': {
            'user.refund_reason': 'not happy with product',
            'merchant.feedback': 'positive',
            'fulfillment.item.condition': 'OK'
        },
    },
    'debit_href': debit['debits'][0]['href']
}