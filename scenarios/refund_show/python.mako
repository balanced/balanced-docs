<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
balanced.Refund.find

% else:
${main.python_boilerplate()}
refund = balanced.Refund.find("${request['uri']}")

% endif
