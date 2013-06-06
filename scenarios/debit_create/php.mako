<%namespace file='/_main.mako' name='main'/>
% if mode == 'definition':
Balanced\Customer->debit()

% else:
${main.php_boilerplate()}
$customer = Balanced\customer::get("${request['customer_uri']}");
$customer->debit(
    "${payload['amount']}",
    "${payload['appears_on_statement_as']}",
    "${payload['description']}"
);

% endif
