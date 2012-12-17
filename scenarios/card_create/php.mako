<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced\Marketplace::mine()->createCard()

% else:
${main.php_boilerplate()}
$card = Balanced\Marketplace::mine()->createCard(
    null, null, null, null, null,
    "${payload['card_number']}",
    "${payload['security_code']}",
    "${payload['expiration_month']}",
    "${payload['expiration_year']}"
);
% endif