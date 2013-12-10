
storage.pop('card_debit', None)

debit = json.loads(
    storage['card_debit']['response']
)

request = {
    'payload': {
        'debit_uri': debit['uri'],
        'description': 'Refund for Order #1111',
        'meta': {
            'user.refund_reason': 'not happy with product',
            'merchant.feedback': 'positive',
            'fulfillment.item.condition': 'OK'
        },
    },
    'uri': debit['customer']['refunds_uri'],
    'debit_uri': debit['uri'],
}