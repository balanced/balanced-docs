<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced::BankAccount.destroy

% else:
${main.ruby_boilerplate()}
bank_account = Balanced::BankAccount.find('${request['uri']}')
bank_account.destroy

% endif
