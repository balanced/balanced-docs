<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
balanced.Account.credit()

% else:
${main.python_boilerplate()}
merchant =  balanced.Account.find('${request['account_uri']}')
merchant.credit(${payload['amount']})

% endif
