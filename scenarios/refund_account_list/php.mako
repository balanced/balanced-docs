<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced\Account->refunds()

% else:
${main.php_boilerplate()}
$buyer = Balanced\Account::get("${request['account_uri']}");
$refunds = $buyer->refunds->query()->all();

% endif
