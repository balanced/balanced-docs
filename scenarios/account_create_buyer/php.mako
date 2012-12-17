<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced\Marketplace->createAccount();

% else:
${main.php_boilerplate()}
$buyer = Balanced\Marketplace::mine()->createBuyer(
    "${payload['card_uri']}"
);

% endif
