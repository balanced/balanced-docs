<%namespace file='/_main.mako' name='main'/>
% if mode == 'definition':
Balanced::Customer.new

% else:
${main.ruby_boilerplate()}
customer = Balanced::Customer.new.save

% endif
