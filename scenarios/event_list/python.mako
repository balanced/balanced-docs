<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
    balanced.Event.query()

% else:
    ${main.python_boilerplate()}
    debits = balanced.Event.query.all();

% endif
