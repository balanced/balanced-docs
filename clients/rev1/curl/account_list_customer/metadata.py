customer = json.loads(
    storage['customer_create']['response']
)

customer_accounts_href = customer['links']['customers.accounts'].replace('{customers.id}', customer['customers'][0]['id'])

request = {
    'uri': customer_accounts_href,
    'customer_href': customer['customers'][0]['href']
}
