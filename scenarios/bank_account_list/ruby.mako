<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced::BankAccount.all

% else:
${main.ruby_boilerplate()}

Balanced::BankAccount.all

% endif
