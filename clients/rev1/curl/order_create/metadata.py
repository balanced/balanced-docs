customer = json.loads(
    storage['customer_create']['response']
)

orders_uri = customer['links']['customers.orders'].replace('{customers.id}', customer['customers'][0]['id'])

request = {
    'uri': orders_uri,
    'payload': {
        'description': 'Order #12341234'
    }
}
