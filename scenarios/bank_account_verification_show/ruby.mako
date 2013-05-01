<%namespace file='/_main.mako' name='main'/>
% if mode == 'definition':
Balanced::Verification.find()
% else:
    ${main.ruby_boilerplate()}
verification = Balanced::Verification.find('${request['uri']}')
% endif
