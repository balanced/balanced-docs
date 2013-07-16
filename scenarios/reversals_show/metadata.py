

reversal = json.loads(
    storage['reversals_create']['response']
)


request = {
    'uri': reversal['uri'],
}
