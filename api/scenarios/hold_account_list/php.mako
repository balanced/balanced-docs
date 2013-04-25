<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced\Account->holds()

% else:
${main.php_boilerplate()}
$account = Balanced\Account::get("${request['account_uri']}");
$holds = $account->holds->query()->all();

% endif
