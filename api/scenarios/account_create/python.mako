<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
balanced.Account(...).save()

% else:
${main.python_boilerplate()}
account = balanced.Account().save()

% endif
