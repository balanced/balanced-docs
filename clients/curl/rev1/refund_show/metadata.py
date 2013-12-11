refund = json.loads(
    storage['refund_create']['response']
)['refunds'][0]

request = {
    'uri': refund['href']
}