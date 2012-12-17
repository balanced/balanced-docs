<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
balanced.Hold.query()

% else:
${main.python_boilerplate()}
holds = balanced.Hold.query.all();

% endif
