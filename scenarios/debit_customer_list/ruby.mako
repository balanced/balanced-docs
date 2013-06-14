<%namespace file='/_main.mako' name='main'/>
% if mode == 'definition':
Balanced::Customer.debits

% else:
${main.ruby_boilerplate()}
customer = Balanced::Customer.find('${request['uri']}')
debits = customer.debits

% endif
