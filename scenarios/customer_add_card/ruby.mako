<%namespace file='/_main.mako' name='main'/>
% if mode == 'definition':
Balanced::Customer.add_card

% else:
${main.ruby_boilerplate()}
customer = Balanced::Customer.find("${request['uri']}")
customer.add_card("${payload['card_uri']}")

% endif
