<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
balanced.Account.credits

% else:
${main.python_boilerplate()}
merchant = balanced.Account.find('${request['account_uri']}')
credits = merchant.credits.all()

% endif
