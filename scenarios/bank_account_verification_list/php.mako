<%namespace file='/_main.mako' name='main'/>
% if request is UNDEFINED:
    Balanced\Marketplace::BankAccount()->verifications

% else:
    ${main.php_boilerplate()}
    $bank_account = Balanced\Marketplace\BankAccount();
    $verifications = $bank_account->verifications->query()->all();

% endif
