<%namespace file='/_main.mako' name='main'/>
% if mode == 'definition':
Balanced\Customer->unstore();

% else:
${main.php_boilerplate()}
$customer = Balanced\Customer::mine()->unstore();

% endif

