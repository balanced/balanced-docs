order = json.loads(
    storage['order_create']['response']
)['orders'][0]

request = {
    'uri': order['href'],
    'payload': {
        'description': 'New description for order',
        'meta': {
          'product.id': '1234567890',
          'anykey': 'valuegoeshere'
        },
    }
}