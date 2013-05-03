<%namespace file='/_main.mako' name='main'/>
% if mode == 'definition':
Balanced::Card.invalidate()

% else:
${main.ruby_boilerplate()}
card = Balanced::Card.find('${request['uri']}')
card.invalidate
% endif