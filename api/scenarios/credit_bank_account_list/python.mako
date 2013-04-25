<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
balanced.BankAccount.credits

% else:
${main.python_boilerplate()}
bank_account = balanced.BankAccount.find('${request['uri']}')
credits = bank_account.credits.all()

% endif
