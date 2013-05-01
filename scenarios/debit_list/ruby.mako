<%namespace file='/_main.mako' name='main'/>
% if mode == 'definition':
Balanced::Debit.all

% else:
${main.ruby_boilerplate()}
marketplace = Balanced::Marketplace.my_marketplace

debits = Balanced::Debit.all(:limit => 2)

% endif
