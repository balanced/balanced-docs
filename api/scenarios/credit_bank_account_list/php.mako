<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced\BankAccount->credits()

% else:
${main.php_boilerplate()}
$bank_account = Balanced\BankAccount::get("${request['uri']}");
$credits = $bank_account->credits->query()->all();

% endif
