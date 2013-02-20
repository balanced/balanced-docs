<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
    Balanced::BankAccountVerification.find()
% else:
    ${main.ruby_boilerplate()}
    bank_account = Balanced::BankAccountVerification.find('${request['uri']}')
% endif
