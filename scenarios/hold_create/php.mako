<%namespace file='/_main.mako' name='main'/>
% if mode == 'definition':
Balanced\Customer->hold()

% else:
${main.php_boilerplate()}
$customer = Balanced\Customer::get("${request['customer_uri']}");
$customer->hold(
    "${payload['amount']}",
    "${payload['description']}"
);

% endif
