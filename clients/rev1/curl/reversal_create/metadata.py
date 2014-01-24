ctx.storage.pop('bank_account_credit', None)

credit = json.loads(
    storage['bank_account_credit']['response']
)

request = {
    'uri': credit['links']['credits.reversals'].replace('{credits.id}', credit['credits'][0]['id']),
    'payload': {
        'amount': 3000,
        'description': 'Reversal for Order #1111',
        'meta': {
            'user.refund_reason': 'not happy with product',
            'merchant.feedback': 'positive',
            'fulfillment.item.condition': 'OK'
        },
    },
    'credit_href': credit['credits'][0]['href']
}