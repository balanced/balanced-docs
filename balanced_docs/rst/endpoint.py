def generate(writer, name, data, exclude_methods):
    endpoint = data.match_endpoint(name)[0]
    if not endpoint:
        raise ValueError('Endpoint "{0}" not found'.format(name))
    path = endpoint['path']
    writer('.. code::\n\n')
    with writer:
        writer('\n')
        if exclude_methods:
            ms = [m for m in endpoint['methods'] if m not in exclude_methods]
        else:
            ms = endpoint['methods']
        for method in ms:
            writer(method)
            writer(' ')
            writer(path)
            writer('\n')
