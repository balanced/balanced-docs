<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
    \Balanced\Callback->save()

% else:
    ${main.php_boilerplate()}
    $callback = new \Balanced\Callback(array(
    % for k, v in payload.iteritems():
        "${k}" => "${v}",
    % endfor
    ));

    $callback->save();

% endif
