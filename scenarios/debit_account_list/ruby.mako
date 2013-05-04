<%namespace file='/_main.mako' name='main'/>
% if mode == 'definition':
Balanced::Account.debits

% else:
${main.ruby_boilerplate()}
account = Balanced::Account.find('${request['uri']}')
debits = account.debits

% endif
