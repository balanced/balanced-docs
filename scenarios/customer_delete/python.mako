<%namespace file='/_main.mako' name='main'/>

% if mode == 'definition':
balanced.Customer.unstore()

% else:
${main.python_boilerplate()}
customer = balanced.Customer.find("${request['uri']}")
customer.unstore()

% endif
