hold = json.loads(
    storage['hold_create']['response']
)['card_holds'][0]

request = {
    'uri': hold['href']
}
