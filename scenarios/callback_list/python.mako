<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
balanced.Callback.query

% else:
${main.python_boilerplate()}
callbacks = balanced.Callback.query.all();
% endif
