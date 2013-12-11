.. _refunds:

Refunds
=======


Create a Refund
----------------

Issues a refund for a debit. You can refund the full amount of the
debit or you can issue a partial refund, where the amount is less than the
charged amount.

.. cssclass:: dl-horizontal dl-params

  .. dcode:: form refunds.create

.. container:: code-white

  .. dcode:: scenario refund_create

.. todo:: partial refund


Get a Refund
-----------------

Get a previously created refund.

.. container:: method-description

  .. no request

.. container:: code-white

   .. dcode:: scenario refund_show


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


Update a Refund
---------------

Updates information about a refund

.. cssclass:: dl-horizontal dl-params

   .. dcode:: form refunds.update

.. container:: code-white

   .. dcode:: scenario refund_update
