def generate(writer, section_char, data, sorts=None):
    if sorts:

        def sort_key(x):
            return tuple(x[s] for s in sorts)

        errors = sorted(data.errors, key=sort_key)
    else:
        errors = data.errors

    for error in errors:
        writer(error['category_code'])
        writer('\n')
        writer(section_char * len(error['category_code']))
        writer('\n')
        writer('\n')
        if error['description']:
            writer(error['description'])
            writer('\n')
            writer('\n')
        writer(':status_code:')
        writer(str(error['status_code']))
        writer('\n')
        writer(':category_type:')
        writer(error['category_type'])
        writer('\n')
        writer(':category_code:')
        writer(error['category_code'])
        writer('\n')
        writer('\n')
