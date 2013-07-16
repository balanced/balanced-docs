reversal = json.load(
    storage['reversals_create']['response']
)

request = {
    'uri': reversal['uri'],
    'payload': {
        'description': 'updating the description',
        'meta': {
            'user.notes': 'one of the best customers',
        }
    }
}
