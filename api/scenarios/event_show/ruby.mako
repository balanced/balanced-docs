<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
    Balanced::Event.find()
% else:
    ${main.ruby_boilerplate()}
    event = Balanced::Event.find('${request['uri']}')
% endif
