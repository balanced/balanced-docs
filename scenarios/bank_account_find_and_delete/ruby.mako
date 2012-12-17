<%namespace file='/_main.mako' name='main'/>

% if request is not UNDEFINED:
${main.ruby_boilerplate()}
bank_account = Balanced::BankAccount.find('${request['uri']}')
bank_account.destroy

% endif
