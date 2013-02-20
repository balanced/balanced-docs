<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
    balanced.BankAccountVerification.query

% else:
    ${main.python_boilerplate()}
verifications = balanced.BankAccountVerification.query.all()
% endif
