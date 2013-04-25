<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced::Account.credit()

% else:
${main.ruby_boilerplate()}
marketplace = Balanced::Marketplace.my_marketplace

merchant = Balanced::Account.find('${request['account_uri']}')
merchant.credit(${payload['amount']})

% endif
