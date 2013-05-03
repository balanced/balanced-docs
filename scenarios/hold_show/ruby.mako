<%namespace file='/_main.mako' name='main'/>
% if mode == 'definition':
Balanced::Hold.find()

% else:
${main.ruby_boilerplate()}
hold = Balanced::Hold.find('${request['uri']}')

% endif
