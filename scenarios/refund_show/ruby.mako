<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced::Refund.find()

% else:
${main.ruby_boilerplate()}
refund = Balanced::Refund.find('${request['uri']}')

% endif
