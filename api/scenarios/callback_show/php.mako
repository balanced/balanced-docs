<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
    Balanced\Callback::get
% else:
    ${main.php_boilerplate()}
    $bank_account = Balanced\Callback::get("${request['uri']}");
% endif
