<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
    Balanced::Callback.find()
% else:
    ${main.ruby_boilerplate()}
    callback = Balanced::Callback.find('${request['uri']}')
% endif
