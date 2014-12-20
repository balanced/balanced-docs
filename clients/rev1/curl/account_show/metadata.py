accounts = json.loads(
    storage['account_list']['response']
)

account = accounts['accounts'][0]

request = {
    'uri': account['href']
}
