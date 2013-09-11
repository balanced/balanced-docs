ctx.storage.pop('customer_create', None)

customer = json.loads(
    storage['customer_create']['response']
)

request = {
    'uri': customer['uri'],
}
