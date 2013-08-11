ctx.storage.pop('customer_create', None)

customer_var = json.loads(
    storage['customer_create']['response']
)

request = {
    'uri': customer_var['uri'],
}
