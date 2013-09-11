customer = json.loads(
    storage['customer_create']['response']
)

request = {
    'uri': customer['holds_uri'],
    'customer_uri': customer['uri'],
}
