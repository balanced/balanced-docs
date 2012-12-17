<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
balanced.Card.find

% else:
${main.python_boilerplate()}
card = balanced.Card.find("${request['uri']}")

% endif
