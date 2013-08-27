<%namespace file='/_main.mako' name='main'/>
% if mode == 'definition':
Balanced::Account.holds

% else:
${main.ruby_boilerplate()}
account = Balanced::Account.find('${request['account_uri']}')
holds = account.holds

% endif
