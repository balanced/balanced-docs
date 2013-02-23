<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
balanced.BankAccountVerification.find
% else:
    ${main.python_boilerplate()}

bank_account = balanced.BankAccount.find("${request['bank_account_uri']}")
bank_account.verification
% endif
