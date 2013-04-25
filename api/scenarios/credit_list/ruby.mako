<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced::Credit.all

% else:
${main.ruby_boilerplate()}
marketplace = Balanced::Marketplace.my_marketplace

Balanced::Credit.all(:limit => 2)

% endif
