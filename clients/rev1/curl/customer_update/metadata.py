customer = json.loads(
    storage['customer_create']['response']
)['customers'][0]

request = {
    'uri': customer['href'],
    'payload': {
        'email': 'email@newdomain.com',
        'meta': {
          'shipping-preference': 'ground'
        },
    }
}