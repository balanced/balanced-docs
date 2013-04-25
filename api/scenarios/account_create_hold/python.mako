<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
balanced.Account.debit()

% else:
${main.python_boilerplate()}
account = balanced.Account.find('${request['account_uri']}')
account.hold(amount='${payload['amount']}')

% endif