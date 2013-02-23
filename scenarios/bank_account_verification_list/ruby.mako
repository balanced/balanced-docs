<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
    Balanced::BankAccountVerification.filter

% else:
    ${main.ruby_boilerplate()}
    verifications = Balanced::BankAccountVerification.filter

% endif
