<%namespace file='/_main.mako' name='main'/>
% if mode == 'definition':
Balanced::Account.debit

% else:
${main.ruby_boilerplate()}
account = Balanced::Account.find("${request['account_uri']}")
account.debit(:amount => '${payload['amount']}')

% endif
