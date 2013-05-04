<%namespace file='/_main.mako' name='main'/>
% if mode == 'definition':
Balanced::Hold.void()

% else:
${main.ruby_boilerplate()}
hold = Balanced::Hold.find('${request['uri']}')
hold.void

% endif
