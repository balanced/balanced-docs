order = json.loads(
    storage['order_create']['response']
)['orders'][0]

request = {
    'uri': order['href']
}
