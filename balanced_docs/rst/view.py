from . import Overrides, Context, IncludeExcludeFilter, Filter


def generate(writer, name, content, data, includes=None, excludes=None):
    ctx = Context(
        filter=IncludeExcludeFilter(
            [Filter(includes, True)] if includes else None,
            [Filter(excludes, False)] if excludes else None,
        ),
        overrides=Overrides.load(content),
        writer=writer,
    )
    view = data.match_view(name)
    if not view:
        raise ValueError('View "{0}" not found'.format(name))
    for field in view['fields']:
        with ctx(field['name']):
            if not ctx.filtered:
                continue
            ctx.writer('``{0}``'.format(field['name']))
            ctx.writer('\n')
            with ctx.writer:
                ctx.writer('**{0}**'.format(field['type']))
                ctx.writer('.')
                if ctx.overriden:
                    description = ctx.override
                else:
                    description = field['description']
                if description:
                    ctx.writer(' ')
                    ctx.writer(description)
        ctx.writer('\n')
