<%namespace file='/_main.mako' name='main'/>
% if mode == 'definition':
Balanced::Hold.all

% else:
${main.ruby_boilerplate()}
marketplace = Balanced::Marketplace.my_marketplace

holds = Balanced::Hold.all(:limit => 2)

% endif
