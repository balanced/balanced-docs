<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced\Marketplace::mine()->bank_accounts

% else:
${main.php_boilerplate()}
$marketplace = Balanced\Marketplace::mine();
$bank_accounts = $marketplace->bank_accounts->query()->all();

% endif
