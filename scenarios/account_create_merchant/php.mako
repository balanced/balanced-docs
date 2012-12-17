<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
\Balanced\Account->addCard();

% else:
${main.php_boilerplate()}
$account = \Balanced\Account::get("${request['uri']}");
$account->addBankAccount("${payload['bank_account_uri']}");

% endif
