<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced::Verification.find()
% else:
    ${main.ruby_boilerplate()}
verification = Balanced::Verification.find('${request['uri']}')
% endif
