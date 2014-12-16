customer = json.loads(
    storage['customer_create']['response']
)

customer_href = customer['links']['customers.accounts'].replace('{customers.id}', customer['customers'][0]['id'])

request = {
    'uri': customer_href
}
