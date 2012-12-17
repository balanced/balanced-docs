<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced\Hold::get

% else:
${main.php_boilerplate()}
$hold = Balanced\Hold::get("${request['uri']}");

% endif
