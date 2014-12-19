settlement = json.loads(
    storage['settlement_list']['response']
)

account_id = settlement['settlements'][0]['links']['source']

request = {
    'uri': '/accounts/' + account_id + '/settlements',
    'href': '/accounts/' + account_id,
    'account_href': '/accounts/' + account_id
}
