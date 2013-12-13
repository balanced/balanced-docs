hold = json.loads(
    storage['card_hold_create']['response']
)['card_holds'][0]

request = {
    'uri': hold['href']
}
