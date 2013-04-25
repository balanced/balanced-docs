<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced::Credit.find

% else:
${main.ruby_boilerplate()}
marketplace = Balanced::Marketplace.my_marketplace

credit = Balanced::Credit.find('${request["uri"]}')

% endif
