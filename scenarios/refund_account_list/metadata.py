refund = json.loads(
    storage['refund_create']['response']
)

if ctx.storage['api_rev'] == 'rev0':
    request = {
        'uri': refund['account']['refunds_uri'],
        'account_uri': refund['account']['uri']
    }
else:
    request = {
        'uri': refund['debit']['customer_uri'] + '/refunds',
        'account_uri': refund['debit']['customer_uri'],
    }
