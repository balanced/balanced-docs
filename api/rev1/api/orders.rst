Orders
======

An ``Order`` resource is a construct that logically groups related transaction
operations for a particular seller (``Customer``). An ``Order`` allows issuing
payouts to only one ``Customer`` and the marketplace bank account. An ``Order``
is useful for reconciliation purposes, as each ``Order`` maintains its own
individual escrow balance, which is separate from the total marketplace escrow.
Attempts to credit an ``Order`` beyond the amount debited into the ``Order``
will fail.

|

.. container:: header3

  Available Query Filters

.. cssclass:: dl-horizontal dl-params filters

  .. dcode:: query Orders


Create an Order
----------------

Create a new Order.

.. cssclass:: dl-horizontal dl-params

  .. dcode:: form orders.create

.. container:: code-white

  .. dcode:: scenario order_create


Fetch an Order
-----------------

Fetch the details of a previously created order.

.. container:: code-white

  .. dcode:: scenario order_show


List All Orders
----------------

List all previously created orders.

.. cssclass:: dl-horizontal dl-params

  ``limit``
      *optional* integer. Defaults to ``10``.

  ``offset``
      *optional* integer. Defaults to ``0``.

.. container:: code-white

  .. dcode:: scenario order_list


Update an Order
----------------

Update a previously created order.

.. cssclass:: dl-horizontal dl-params

  .. dcode:: form orders.update

.. container:: code-white

  .. dcode:: scenario order_update
