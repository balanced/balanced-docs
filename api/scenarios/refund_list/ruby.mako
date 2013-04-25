<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced::Refund.all

% else:
${main.ruby_boilerplate()}
marketplace = Balanced::Marketplace.my_marketplace

refunds = Balanced::Refund.all(:limit => 2)

% endif
