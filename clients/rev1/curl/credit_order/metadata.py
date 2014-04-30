bank_accounts = json.loads(
    storage['bank_account_list']['response']
)

bank_account_href = storage['bank_account_associate_to_customer']['request']['uri']


order = json.loads(
    storage['order_create']['response']
)['orders'][0]


request = {
    'uri': bank_account_href + '/credits',
    'payload': {
        'amount': 5000,
        'order': order['href'],
        },
    'bank_account_href': bank_account_href
}
