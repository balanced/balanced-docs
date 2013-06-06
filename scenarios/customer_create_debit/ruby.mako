<%namespace file='/_main.mako' name='main'/>
% if mode == 'definition':
Balanced::Customer.debit

% else:
${main.ruby_boilerplate()}
customer = Balanced::Customer.find("${request['customer_uri']}")
customer.debit(:amount => '${payload['amount']}')

% endif
