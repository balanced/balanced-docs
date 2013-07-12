<%namespace file='/_main.mako' name='main'/>
% if mode == 'definition':
Balanced::Account.credit()

% else:
${main.ruby_boilerplate()}
marketplace = Balanced::Marketplace.my_marketplace

merchant = Balanced::Account.find('${request['account_uri']}')
merchant.credit(:amount => ${payload['amount']})

% endif
