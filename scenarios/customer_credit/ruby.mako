<%namespace file='/_main.mako' name='main'/>
% if mode == 'definition':
Balanced::Customer.credit()

% else:
${main.ruby_boilerplate()}
marketplace = Balanced::Marketplace.my_marketplace

customer = Balanced::Customer.find('${request['customer_uri']}')
customer.credit(${payload['amount']})

% endif
