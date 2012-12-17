<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced::Account.new

% else:
${main.ruby_boilerplate()}
account = Balanced::Marketplace.my_marketplace.create_account

% endif
