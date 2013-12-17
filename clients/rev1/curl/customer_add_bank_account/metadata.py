customer = json.loads(
    storage['customer_create']['response']
)

bank_account = json.loads(
    ctx.storage['bank_account_create']['response']
)

request = {
    'uri': customer['customers'][0]['href'],
    'payload': {
        'bank_account_href': bank_account['bank_accounts'][0]['href'],
    },
    'customer_href': customer['customers'][0]['href']
}
