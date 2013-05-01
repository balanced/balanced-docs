<%namespace file='/_main.mako' name='main'/>
% if mode == 'definition':
Balanced::Account.credits

% else:
${main.ruby_boilerplate()}
merchant = Balanced::Account.find('${request['account_uri']}')
credits = merchant.credits

% endif
