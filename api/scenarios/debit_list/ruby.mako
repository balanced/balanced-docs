<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced::Debit.all

% else:
${main.ruby_boilerplate()}
marketplace = Balanced::Marketplace.my_marketplace

debits = Balanced::Debit.all(:limit => 2)

% endif
