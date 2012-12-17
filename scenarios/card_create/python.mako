<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
balanced.Card.save()

% else:
${main.python_boilerplate()}
card = balanced.Card(
% for k, v in payload.iteritems():
    ${k}='${v}',
% endfor
).save()

% endif
