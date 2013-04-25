<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced\BankAccount->delete()

% else:
${main.php_boilerplate()}
$bank_account = Balanced\BankAccount::get("${request['uri']}");
$bank_account->delete();

% endif
