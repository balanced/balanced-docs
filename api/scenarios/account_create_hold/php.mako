<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
\Balanced\Account->debit();

% else:
${main.php_boilerplate()}
$account = \Balanced\Account::get("${request['account_uri']}");
$account->hold('${payload['amount']}');

% endif
