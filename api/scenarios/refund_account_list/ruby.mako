<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced::Account.refunds

% else:
${main.ruby_boilerplate()}
buyer = Balanced::Account.find('${request['account_uri']}')
refunds = buyer.refunds

% endif
