<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced\Buyer->debit()

% else:
${main.php_boilerplate()}
$buyer = Balanced\Account::get("${request['account_uri']}");
$buyer->debit(
    "${payload['amount']}",
    "${payload['appears_on_statement_as']}",
    "${payload['description']}"
);

% endif
