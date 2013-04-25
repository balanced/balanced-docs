def generate(writer, name, data):
    enum = data.match_enum(name)
    if not enum:
        raise ValueError('Enum "{}" not found'.format(name))
    for value, description in sorted(enum['values'].items()):
        writer(value)
        writer('\n')
        with writer:
            writer(description)
        writer('\n')
