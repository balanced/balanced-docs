reversal = json.loads(
    storage['reversal_create']['response']
)['reversals'][0]

request = {
    'uri': reversal['href']
}