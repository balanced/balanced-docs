refund = json.loads(
    storage['refund_create']['response']['content']
)

request = {
    'uri': refund['account']['refunds_uri'],
    'account_uri': refund['account']['uri']
}