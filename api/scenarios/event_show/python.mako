<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
balanced.Event.find
% else:
${main.python_boilerplate()}
event = balanced.Event.find("${request['uri']}")
% endif
