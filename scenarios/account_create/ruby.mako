<%namespace file='/_main.mako' name='main'/>
% if mode == 'definition':
Balanced::Account.new

% else:
${main.ruby_boilerplate()}
account = Balanced::Marketplace.my_marketplace.create_account

% endif
