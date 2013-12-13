customer = json.loads(
    storage['customer_create']['response']
)

order = json.loads(
    storage['order_create']['response']
)

orders_uri = customer['links']['customers.orders'].replace('{customers.id}', order['orders'][0]['links']['merchant'])

request = {
    'uri': orders_uri
}
