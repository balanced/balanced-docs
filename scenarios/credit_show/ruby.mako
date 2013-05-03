<%namespace file='/_main.mako' name='main'/>
% if mode == 'definition':
Balanced::Credit.find

% else:
${main.ruby_boilerplate()}
marketplace = Balanced::Marketplace.my_marketplace

credit = Balanced::Credit.find('${request["uri"]}')

% endif
