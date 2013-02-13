<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
    Balanced::Callback.save

% else:
    ${main.ruby_boilerplate()}
    callback = Balanced::Callback.new(
    % for k, v in payload.iteritems():
        :${k} => '${v}',
    % endfor
    ).save

% endif
