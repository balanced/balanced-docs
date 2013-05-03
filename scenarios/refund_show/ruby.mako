<%namespace file='/_main.mako' name='main'/>
% if mode == 'definition':
Balanced::Refund.find()

% else:
${main.ruby_boilerplate()}
refund = Balanced::Refund.find('${request['uri']}')

% endif
