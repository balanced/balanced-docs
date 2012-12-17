
refund = json.loads(
    storage['refund_create']['response']['content']
)

request = {
    'uri': refund['uri'],
}