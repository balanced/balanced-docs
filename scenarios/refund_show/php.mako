<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced\Refund::get

% else:
${main.php_boilerplate()}
$refund = Balanced\Refund::get("${request['uri']}");

% endif
