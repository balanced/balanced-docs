settlements = json.loads(
    storage['settlement_list']['response']
)

settlement = settlements['settlements'][0]

request = {
    'uri': settlement['href']
}
