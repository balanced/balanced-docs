Refunds
=======

A ``Refund`` resource represents a refund of a ``Debit`` transaction.


Create a Refund
----------------

Issues a refund for a debit. A refund can be for any amount is less or equal
to the original debit amount.

.. cssclass:: dl-horizontal dl-params

  .. dcode:: form refunds.create

.. container:: code-white

  .. dcode:: scenario refund_create


Retrieve a Refund
-----------------

Retrieve a previously created refund.

.. container:: code-white

   .. dcode:: scenario refund_show


Update a Refund
---------------

Updates information about a refund

.. cssclass:: dl-horizontal dl-params

   .. dcode:: form refunds.update

.. container:: code-white

   .. dcode:: scenario refund_update


List All Refunds
----------------

Returns a list of all previously created refunds. The refunds are returned
in sorted order, with the most recent refunds appearing first.

.. cssclass:: dl-horizontal dl-params

  ``limit``
      *optional* integer. Defaults to ``10``.

  ``offset``
      *optional* integer. Defaults to ``0``.

.. container:: code-white

   .. dcode:: scenario refund_list


Refund Filters
--------------------------------

.. cssclass:: dl-horizontal dl-params filters

  .. dcode:: query Refunds


.. List All Refunds For a Customer
.. -------------------------------
.. 
.. Returns a list of refunds you've previously created against a specific account.
.. The refunds are returned in sorted order, with the most recent refunds
.. appearing first.
.. 
.. .. cssclass:: dl-horizontal dl-params
.. 
..   ``limit``
..       *optional* integer. Defaults to ``10``.
.. 
..   ``offset``
..       *optional* integer. Defaults to ``0``.
.. 
.. .. container:: code-white
.. 
..    .. dcode:: scenario refund_customer_list

