<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced\Marketplace::mine()->cards

% else:
${main.php_boilerplate()}
$marketplace = Balanced\Marketplace::mine();
$cards = $marketplace->cards->query()->all();

% endif