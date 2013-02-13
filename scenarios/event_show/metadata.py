import balanced
balanced.configure(storage['api_key'])

# HACK: we haven't release Event yet
# event = balanced.Event.query[0]
class Event(balanced.resources.Resource):
    __metaclass__ = balanced.resources.resource_base(
        collection='events')
balanced.Event = Event
event = balanced.Event.query[0]

request = {
    'uri': event.uri,
}
