<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced::Card.save()

% else:
${main.ruby_boilerplate()}
card = Balanced::Card.find('${request['uri']}')
card.invalidate
% endif