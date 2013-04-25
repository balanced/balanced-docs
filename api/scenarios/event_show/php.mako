<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
    Balanced\Event::get
% else:
    ${main.php_boilerplate()}
    $event = Balanced\Event::get("${request['uri']}");
% endif
