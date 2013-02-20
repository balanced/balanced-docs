<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
    Balanced\BankAccountVerification::get
% else:
    ${main.php_boilerplate()}
    $verification = Balanced\BankAccountVerification::get("${request['uri']}");
% endif
