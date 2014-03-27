<?php
# $order_href is the stored href for the Order
$order = Balanced\Order::get($order_href); # get the order object to get recent changes

$order->amount;
$order->amount_escrowed;
?>
