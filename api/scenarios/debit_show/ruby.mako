<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced::Debit.find()

% else:
${main.ruby_boilerplate()}
debit = Balanced::Debit.find('${request['uri']}')

% endif
