<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
balanced.Hold.void()

% else:
${main.python_boilerplate()}
hold = balanced.Hold.find('${request['uri']}')
hold.void()

% endif
