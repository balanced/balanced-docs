cards = json.loads(
    storage['card_list']['response']
)

card = cards['items'][-1]

request = {
    'uri': card['uri'],
}
