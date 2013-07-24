card = json.loads(
    storage['card_charge']['response']
)

request = {
    'uri': card['uri'],
}
