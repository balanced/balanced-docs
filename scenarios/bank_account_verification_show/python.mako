<%namespace file='/_main.mako' name='main'/>
% if mode == 'definition':
balanced.Verification.find
% else:
    ${main.python_boilerplate()}

bank_account = balanced.BankAccount.find("${request['bank_account_uri']}")
verification = bank_account.verification
% endif
