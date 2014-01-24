credit = json.loads(
    storage['bank_account_credit']['response']
)['credits'][0]

request = {
    'uri': credit['href']
}
