<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced::Account.debit

% else:
${main.ruby_boilerplate()}
account = Balanced::Account.find("${request['account_uri']}")
account.debit(:amount => ${payload['amount']}, :hold_uri => '${payload['hold_uri']}')

% endif
