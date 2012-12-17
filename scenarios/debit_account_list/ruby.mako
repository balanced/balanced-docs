<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced::Account.credits

% else:
${main.ruby_boilerplate()}
account = Balanced::Account.find('${request['uri']}')
debits = account.debits

% endif
