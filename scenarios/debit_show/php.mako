<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced\Debit::get

% else:
${main.php_boilerplate()}
$debit = Balanced\Debit::get("${request['uri']}");

% endif
