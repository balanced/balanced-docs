from . import IncludeExcludeFilter, Filter

def generate(writer, name, content, data, includes=None, excludes=None):
    form = data.match_query(name)
    if not form:
        raise ValueError('Query "{0}" not found'.format(name))
    for field in form['fields']:
        _generate(writer, field)

def _generate(writer, field):
    writer('``{0}``'.format(field['name']))
    writer('\n')
    with writer:
        writer('**Available Operations:** ')
        writer(", ".join(field['ops']))
        writer('\n\n')
        writer('**Default Operation:** {0}'.format(field['default_op']))
        writer('\n\n')
        writer('**Sortable:** {0}'.format(field['sortable']))
        writer('\n\n')
    writer('\n')