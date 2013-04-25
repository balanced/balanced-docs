<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced\Hold->capture()

% else:
${main.php_boilerplate()}
$hold = Balanced\Hold::get("${request['hold_uri']}");
$debit = $hold->capture();

% endif
