callback = json.loads(
    storage['callback_create']['response']
)['callbacks'][0]

request = {
    'uri': callback['href'],
    }