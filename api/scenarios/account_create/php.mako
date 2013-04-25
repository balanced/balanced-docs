<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced\Marketplace->createAccount();

% else:
${main.php_boilerplate()}
$account = Balanced\Marketplace::mine()->createAccount();

% endif
