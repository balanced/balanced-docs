
refund = json.loads(
    storage['refund_create']['response']
)

request = {
    'uri': refund.get('uri', 'TODO: fix reversals to work while pending'),
}
