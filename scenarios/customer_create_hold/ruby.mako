<%namespace file='/_main.mako' name='main'/>
% if mode == 'definition':
Balanced::Customer.hold

% else:
${main.ruby_boilerplate()}
customer = Balanced::Customer.find("${request['customer_uri']}")
customer.hold(:amount => '${payload['amount']}')

% endif
