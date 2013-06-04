<%namespace file='/_main.mako' name='main'/>
% if mode == 'definition':
Balanced::Customer.add_bank_account

% else:
${main.ruby_boilerplate()}
customer = Balanced::Customer.find("${request['uri']}")
customer.add_bank_account("${payload['bank_account_uri']}")

% endif
