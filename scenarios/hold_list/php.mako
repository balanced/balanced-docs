<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced\Marketplace::mine()->holds

% else:
${main.php_boilerplate()}
$marketplace = Balanced\Marketplace::mine();
$holds = $marketplace->holds->query()->all();

% endif
