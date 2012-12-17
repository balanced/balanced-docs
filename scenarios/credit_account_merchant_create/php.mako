<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced\Account::credit()

% else:
${main.php_boilerplate()}
$merchant = Balanced\Account::get("${request['account_uri']}");
$merchant->credit(${payload['amount']});

% endif
