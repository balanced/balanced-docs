<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
    balanced.Callback.find
% else:
    ${main.python_boilerplate()}
callback = balanced.Callback.find("${request['uri']}")
% endif
