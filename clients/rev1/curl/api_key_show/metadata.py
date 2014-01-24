api_key = json.loads(
    storage['api_key_create']['response']
)['api_keys'][0]

request = {
    'uri': api_key['href']
}