<?php
$bank_account = $marketplace->bank_accounts->create(array(
"account_number" => "9900000001",
"name" => "Johann Bernoulli",
"routing_number" => "121000358",
"type" => "checking",
));

$bank_account->associateToCustomer($merchant);
?>