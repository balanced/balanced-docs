<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
    balanced.Verification().save()

% else:
    ${main.python_boilerplate()}
bank_account = balanced.BankAccount.find("${request['bank_account_uri']}")
verification = bank_account.verify()
% endif
