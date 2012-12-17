<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced::BankAccount.find()
% else:
${main.ruby_boilerplate()}
bank_account = Balanced::BankAccount.find('${request['uri']}')
% endif
