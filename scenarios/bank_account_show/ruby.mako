<%namespace file='/_main.mako' name='main'/>
% if mode == 'definition':
Balanced::BankAccount.find()
% else:
${main.ruby_boilerplate()}
bank_account = Balanced::BankAccount.find('${request['uri']}')
% endif
