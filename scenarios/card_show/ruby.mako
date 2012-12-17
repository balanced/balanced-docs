<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced::Card.find()

% else:
${main.ruby_boilerplate()}
card = Balanced::Card.find('${request['uri']}')

% endif
