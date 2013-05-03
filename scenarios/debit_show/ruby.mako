<%namespace file='/_main.mako' name='main'/>
% if mode == 'definition':
Balanced::Debit.find()

% else:
${main.ruby_boilerplate()}
debit = Balanced::Debit.find('${request['uri']}')

% endif
