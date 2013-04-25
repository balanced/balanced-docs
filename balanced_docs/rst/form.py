import json
import logging

from . import Overrides, IncludeExcludeFilter, Filter, Context


logger = logging.getLogger(__name__)


def generate(writer, name, content, data, includes=None, excludes=None):
    ctx = Context(
        filter=IncludeExcludeFilter(
            [Filter(includes, True)] if includes else None,
            [Filter(excludes, False)] if excludes else None,
        ),
        overrides=Overrides.load(content),
        writer=writer
    )
    form = data.match_form(name)
    if not form:
        raise ValueError('Form "{}" not found'.format(name))
    for field in form['fields']:
        _generate(ctx, field)


# internals

def _format_value(ctx, v):
    if isinstance(v, basestring):
        return v
    if v is None:
        return 'null'
    if isinstance(v, bool):
        return str(v).lower()
    v = json.dumps(v, indent=4)
    v = v.replace('"', '\"')
    return v


def _generate(ctx, field):
    g = _GENERATORS.get(field['type'], _generate_field)
    g(ctx, field)


def _generate_field(ctx, field):
    with ctx(field['name']):
        if not ctx.filtered:
            return

        # name
        ctx.writer('``{}``'.format(field['name']))
        ctx.writer('\n')

        with ctx.writer:
            if ctx.overriden:
                ctx.writer(ctx.override)
            else:
                # type
                ctx.writer('*required*' if field['required'] else '*optional*')
                ctx.writer(' **{}**'.format(field['type']))
                if field['nullable']:
                    ctx.writer(' or **null**')
                ctx.writer('.')

                # description
                if field['description']:
                    ctx.writer(' ')
                    ctx.writer(field['description'])

                # default
                if 'default' in field:
                    default = field['default']
                    if isinstance(default, basestring) and '\n' in default:
                        ctx.writer(' ')
                        ctx.writer(default)
                    else:
                        default = _format_value(ctx, default)
                        if '\n' in default:
                            ctx.writer(' Defaults to: ')
                            ctx.writer('\n')
                            ctx.writer('\n')
                            ctx.writer('.. code:: javascript')
                            ctx.writer('\n')
                            with ctx.writer:
                                ctx.writer('\n')
                                ctx.writer(default)
                        else:
                            ctx.writer(' ')
                            ctx.writer('Defaults to ``{}``.'.format(default))
        ctx.writer('\n')


def _generate_form(ctx, form):
    for field in form['fields']:
        _generate(ctx, field)


def _generate_form_field(ctx, form_field):
    with ctx(form_field['name']):
        if not ctx.filtered:
            return

        # name
        ctx.writer('``{}``'.format(form_field['name']))
        ctx.writer('\n')

        with ctx.writer:
            if ctx.overriden:
                ctx.writer(ctx.override)
                ctx.writer('\n')
            else:
                _generate(ctx, form_field['form'])


def _generate_select_field(ctx, select_field):
    for i, field in enumerate(select_field['fields']):
        with ctx(str(i)):
            if not ctx.filtered:
                continue
            _generate(ctx, field)


def _generate_one_field(ctx, one_field):
    for field in one_field['fields']:
        _generate(ctx, field)


_GENERATORS = {
   'form': _generate_form,
   'form_field': _generate_form_field,
   'select': _generate_select_field,
   'one': _generate_one_field,
}
