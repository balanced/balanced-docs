reversal = json.loads(
    storage['reversal_create']['response']
)['reversals'][0]

request = {
    'uri': reversal['href'],
    'payload': {
        'description': 'update this description',
        'meta': {
            'refund.reason': 'user not happy with product',
            'user.refund.count': '3',
            'user.notes': 'very polite on the phone',
        }
    }
}
