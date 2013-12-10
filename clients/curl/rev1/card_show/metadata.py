card = json.loads(
    storage['card_create']['response']
)['cards'][0]

request = {
    'uri': card['href'],
}
