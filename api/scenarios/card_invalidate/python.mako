<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
balanced.Card.save()

% else:
${main.python_boilerplate()}
card = balanced.Card.find('${request['uri']}')
card.is_valid = False
card.save()
% endif
