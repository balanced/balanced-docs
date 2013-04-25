<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
    Balanced\Callback->delete()

% else:
    ${main.php_boilerplate()}
    $callback = Balanced\Callback::get("${request['uri']}");
    $callback->delete();

% endif
