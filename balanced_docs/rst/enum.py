from . import IncludeExcludeFilter, Filter


def generate(writer, name, data, includes=None, excludes=None):
    filter = IncludeExcludeFilter(
        [Filter(includes, True)] if includes else None,
        [Filter(excludes, False)] if excludes else None,
    )
    enum = data.match_enum(name)
    if not enum:
        raise ValueError('Enum "{}" not found'.format(name))
    for value, description in sorted(enum['values'].items()):
        if not filter(value):
            continue
        writer(value)
        writer('\n')
        with writer:
            writer(description)
        writer('\n')
