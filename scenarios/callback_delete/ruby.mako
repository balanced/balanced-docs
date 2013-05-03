<%namespace file='/_main.mako' name='main'/>
% if mode == 'definition':
    Balanced::Callback.destroy

% else:
    ${main.ruby_boilerplate()}
    callback = Balanced::Callback.find('${request['uri']}')
    callback.destroy

% endif
