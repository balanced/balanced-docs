<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
Balanced\BankAccount::get
% else:
${main.php_boilerplate()}
$bank_account = Balanced\BankAccount::get("${request['uri']}");
% endif
