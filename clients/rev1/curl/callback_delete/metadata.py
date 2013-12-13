callbacks = json.loads(
    storage['callback_list']['response']
)

callback = callbacks['callbacks'][-1]

request = {
    'uri': callback['href'],
}
