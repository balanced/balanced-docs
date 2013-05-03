<%namespace file='/_main.mako' name='main'/>
% if mode == 'definition':
    Balanced::Event.find()
% else:
    ${main.ruby_boilerplate()}
    event = Balanced::Event.find('${request['uri']}')
% endif
