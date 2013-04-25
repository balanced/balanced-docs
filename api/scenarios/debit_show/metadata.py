debit = json.loads(
    storage['debit_create']['response']['content']
)

request = {
    'uri': debit['uri'],
}
