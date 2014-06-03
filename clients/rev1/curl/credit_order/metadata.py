order_debit = json.loads(
    storage['debit_order']['response']
)

bank_accounts = json.loads(
    storage['bank_account_associate_to_customer']['response']
)

bank_account_href = bank_accounts['links']['bank_accounts.credits'].replace('{bank_accounts.id}', bank_accounts['bank_accounts'][0]['id'])


order = json.loads(
    storage['order_create']['response']
)['orders'][0]


request = {
    'uri': bank_account_href,
    'payload': {
        'amount': 5000,
        'order': order['href'],
    },
    'bank_account_href': bank_account_href,
    'order_href': order['href'],
}
