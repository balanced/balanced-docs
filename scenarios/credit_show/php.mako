<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced\Credit::get()

% else:
${main.php_boilerplate()}
$credit = Balanced\Credit::get("${request['uri']}");

% endif
