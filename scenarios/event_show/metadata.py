index = 0
while True:
    ctx.storage.pop('debit_create', None)
    dd = ctx.storage['debit_create']
    index += 1
    if index > 50:
        raise Exception('No events being generated')
    try:
        ctx.storage.pop('event_list', None)
        ee = json.loads(ctx.storage['event_list']['response'])
        if len(ee['items']) > 0:
            event_uri = ee['items'][0]['uri']
            break
    except IndexError:
        pass


request = {
    'uri': event_uri,
}
