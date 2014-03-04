import requests
import time

while True:
    event = requests.get(ctx.storage['api_location'] + ctx.marketplace.links['marketplaces.events'],
                         headers={'Accept-Type': ctx.storage.get('accept_type', '*/*')},
                         auth=(ctx.storage['secret'], '')).json()
    if event.get('events'):
        break
    time.sleep(5)

request = {
    'uri': event['events'][0]['href'],
}
