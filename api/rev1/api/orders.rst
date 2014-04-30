Orders
======

An ``Order`` resource is a construct that logically groups related transaction
operations for a particular seller (``Customer``). An ``Order`` allows issuing
payouts to one ``Customer`` and the marketplace bank account.

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
