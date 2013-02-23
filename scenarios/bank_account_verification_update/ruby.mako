<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
    Balanced::BankAccountVerification.save()

% else:
    ${main.ruby_boilerplate()}
verification = Balanced::BankAccountVerification.find('${request['uri']}')
% for k, v in payload.iteritems():
verification.${k} = '${v}'
% endfor
verification.save

% endif
