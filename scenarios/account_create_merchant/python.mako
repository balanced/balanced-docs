<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
balanced.Account.add_bank_account

% else:
${main.python_boilerplate()}
account = balanced.Account.find('${request['uri']}')
account.add_bank_account('${payload['bank_account_uri']}')

% endif
