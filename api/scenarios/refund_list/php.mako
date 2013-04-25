<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced\Marketplace::mine()->refunds

% else:
${main.php_boilerplate()}
$marketplace = Balanced\Marketplace::mine();
$refunds = $marketplace->refunds->query()->all();

% endif
