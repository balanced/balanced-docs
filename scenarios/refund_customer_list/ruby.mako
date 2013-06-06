<%namespace file='/_main.mako' name='main'/>
% if mode == 'definition':
Balanced::Customer.refunds

% else:
${main.ruby_boilerplate()}
customer = Balanced::Customer.find('${request['customer_uri']}')
refunds = customer.refunds

% endif
