callback = json.loads(
    storage['callback_create']['response']['content']
)

request = {
    'uri': callback['uri'],
}
