customer = json.loads(
    storage['customer_create']['response']
)

request = {
    'uri': customer['uri'],
    'debits_uri': customer['debits_uri'],
}
