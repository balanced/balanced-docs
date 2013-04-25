card = json.loads(
    storage['card_create']['response']['content']
)

request = {
    'uri': card['uri'],
}
