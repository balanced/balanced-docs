<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
balanced.Credit.find()

% else:
${main.python_boilerplate()}
credit = balanced.Credit.find('${request['uri']}')

% endif
