<%namespace file='/_main.mako' name='main'/>
% if mode == 'definition':
Balanced::Customer.unstore

% else:
${main.ruby_boilerplate()}
customer = Balanced::Customer.find("${request['uri']}")
customer.unstore

% endif
