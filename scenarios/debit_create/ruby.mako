<%namespace file='/_main.mako' name='main'/>
% if mode == 'definition':
Balanced::Account.debit(...)

% else:
${main.ruby_boilerplate()}
buyer = Balanced::Account.find('${request['account_uri']}')
buyer.debit(
% for k, v in payload.iteritems():
  :${k} => '${v}',
% endfor
)

% endif
