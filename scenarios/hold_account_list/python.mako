<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
balanced.Account.holds

% else:
${main.python_boilerplate()}
account = balanced.Account.find('${request['account_uri']}')
holds = account.holds.all()

% endif
