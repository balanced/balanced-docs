<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced\Marketplace::mine()->debits

% else:
${main.php_boilerplate()}
$marketplace = Balanced\Marketplace::mine();
$debits = $marketplace->debits->query()->all();

% endif
