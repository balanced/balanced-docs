<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
    Balanced\Verification::get
% else:
    ${main.php_boilerplate()}
    $verification = Balanced\Verification::get("${request['uri']}");
% endif
