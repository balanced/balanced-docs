import requests

event = requests.get(ctx.storage['api_location'] + ctx.marketplace.links['marketplaces.events'],
                                 headers={'Accept-Type': ctx.storage.get('accept_type', '*/*')},
                                 auth=(ctx.storage['secret'], '')).json()

request = {
    'uri': event['events'][0]['href'],
}
