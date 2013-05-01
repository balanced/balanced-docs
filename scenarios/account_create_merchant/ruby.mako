<%namespace file='/_main.mako' name='main'/>
% if mode == 'definition':
Balanced::Account.add_bank_account

% else:
${main.ruby_boilerplate()}
account = Balanced::Account.find("${request['uri']}")
account.add_bank_account("${payload['bank_account_uri']}")

% endif
