<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced\Account->credits()

% else:
${main.php_boilerplate()}
$merchant = Balanced\Account::get("${request['account_uri']}");
$credits = $merchant->credits->query()->all();

% endif
