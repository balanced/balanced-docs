<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
balanced.Account.debits

% else:
${main.python_boilerplate()}
account = balanced.Account.find('${request['uri']}')
debits = account.debits.all()

% endif
