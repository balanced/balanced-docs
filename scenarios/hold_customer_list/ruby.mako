<%namespace file='/_main.mako' name='main'/>
% if mode == 'definition':
Balanced::Customer.holds

% else:
${main.ruby_boilerplate()}
customer = Balanced::Customer.find('${request['customer_uri']}')
holds = customer.holds

% endif
