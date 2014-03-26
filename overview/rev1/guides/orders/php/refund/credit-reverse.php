<?php
$order = Balanced\Order::get($order_href);
$credits = $order->credits;
$credit = $credits[0];
$credit->reverse();
?>