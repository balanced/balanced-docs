<%namespace file='/_main.mako' name='main'/>
% if mode == 'definition':
Balanced::BankAccount.destroy

% else:
${main.ruby_boilerplate()}
bank_account = Balanced::BankAccount.find('${request['uri']}')
bank_account.destroy

% endif
