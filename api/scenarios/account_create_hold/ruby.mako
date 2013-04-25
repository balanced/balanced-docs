<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced::Account.hold

% else:
${main.ruby_boilerplate()}
account = Balanced::Account.find("${request['account_uri']}")
account.hold(:amount => '${payload['amount']}')

% endif
