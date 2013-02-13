<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced::Account.add_bank_account

% else:
${main.ruby_boilerplate()}
account = Balanced::Account.find("${request['uri']}")
account.add_bank_account("${payload['bank_account_uri']}")

% endif
