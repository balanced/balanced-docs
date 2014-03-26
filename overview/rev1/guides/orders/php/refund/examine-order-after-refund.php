<?php
$order = Balanced\Order::get($order_href);
$order->amount; # original order amount
$order->amount_escrowed; # will decrease by amount of refunded debit
?>
