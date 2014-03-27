<?php
$marketplace = \Balanced\Marketplace::mine();
$merchant = $marketplace->customers->create(array(
    "dob_month" => "7",
    "dob_year" => "1963",
    "name" => "Henry Ford",
    "address" => array(
        "postal_code" => "48120",
    )
));

$order = $merchant->orders->create();
?>
