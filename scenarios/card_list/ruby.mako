<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced::Marketplace.cards
% else:
${main.ruby_boilerplate()}
cards = Balanced::Marketplace.my_marketplace.cards
% endif
