<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
balanced.BankAccount.find
% else:
${main.python_boilerplate()}
bank_account = balanced.BankAccount.find("${request['uri']}")
% endif
