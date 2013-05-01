<%namespace file='/_main.mako' name='main'/>
% if mode == 'definition':
Balanced::BankAccount.credit

% else:
${main.ruby_boilerplate()}
marketplace = Balanced::Marketplace.my_marketplace

bank_account = Balanced::BankAccount.find("${request['uri']}")
bank_account.credit(${payload['amount']})

% endif
