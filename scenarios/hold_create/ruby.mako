<%namespace file='/_main.mako' name='main'/>
% if mode == 'definition':
Balanced::Customer.hold(...)

% else:
${main.ruby_boilerplate()}
customer = Balanced::Customer.find('${request['customer_uri']}')
customer.hold(
% for k, v in payload.iteritems():
  :${k} => '${v}',
% endfor
)

% endif
