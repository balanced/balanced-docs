<%namespace file='/_main.mako' name='main'/>
% if mode == 'definition':
Balanced::BankAccount.all

% else:
${main.ruby_boilerplate()}

Balanced::BankAccount.all

% endif
