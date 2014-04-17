import requests
import time

debit = json.loads(
    storage['card_debit_dispute']['response']
)

timeout = 12 * 60
interval = 10
begin = time.time()

while True:
    debit = requests.get(ctx.storage['api_location'] + debit['debits'][0]['href'],
                         headers={'Accept-Type': ctx.storage.get('accept_type', '*/*')},
                         auth=(ctx.storage['secret'], '')).json()
    if debit['debits'][0]['links']['dispute'] != None:
        break
    time.sleep(interval)
    elapsed = time.time() - begin
    if elapsed > timeout:
        sys.exit()

request = {
    'uri': debit['links']['debits.dispute'].replace('{debits.dispute}', debit['debits'][0]['links']['dispute']),
}
