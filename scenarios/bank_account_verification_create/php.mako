<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
    \Balanced\Verification->save()

% else:
    ${main.php_boilerplate()}
$bank_account = Balanced\BankAccount::get("${request['bank_account_uri']}");
$verification = $bank_account->verify();
% endif
