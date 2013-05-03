<%namespace file='/_main.mako' name='main'/>
% if mode == 'definition':
Balanced::Marketplace.cards
% else:
${main.ruby_boilerplate()}
cards = Balanced::Marketplace.my_marketplace.cards
% endif
