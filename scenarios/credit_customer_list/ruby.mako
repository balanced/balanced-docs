<%namespace file='/_main.mako' name='main'/>
% if mode == 'definition':
Balanced::Customer.credits

% else:
${main.ruby_boilerplate()}
customer = Balanced::Customer.find('${request['customer_uri']}')
credits = customer.credits

% endif
