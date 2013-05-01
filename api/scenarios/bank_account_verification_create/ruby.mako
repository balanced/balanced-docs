<%namespace file='/_main.mako' name='main'/>
% if mode == 'definition':
    Balanced::Verification.new.save

% else:
    ${main.ruby_boilerplate()}
bank_account = Balanced::BankAccount.find("${request['bank_account_uri']}")
verification = bank_account.verify

% endif
