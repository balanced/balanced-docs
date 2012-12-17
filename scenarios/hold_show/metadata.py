hold = json.loads(
    storage['hold_create']['response']['content']
)

request = {
    'uri': hold['uri']
}
