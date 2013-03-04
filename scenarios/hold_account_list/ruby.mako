<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced::Account.holds

% else:
${main.ruby_boilerplate()}
account = Balanced::Account.find('${request['account_uri']}')
holds = account.holds

% endif
