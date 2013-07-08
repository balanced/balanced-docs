.. _refunds:

Refunds
=======

.. cssclass:: method-section

Issue a Refund
--------------

Issues a refund from a debit. You can either refund the full amount of the
debit or you can issue a partial refund, where the amount is less than the
charged amount.

.. cssclass:: dl-horizontal dl-params

  .. dcode:: form refunds.create
     :exclude: account_uri

.. container:: method-examples

  .. dcode:: scenario refund_create

.. todo:: partial refund

.. cssclass:: method-section

Retrieve a Refund
-----------------

Retrieves the details of a refund that you've previously created. Use the
``uri`` that was previously returned, and the corresponding refund
information will be returned.

.. container:: method-description

  .. no request

.. container:: method-examples

   .. dcode:: scenario refund_show


.. cssclass:: method-section

List All Refunds
----------------

Returns a list of refunds you've previously created. The refunds are returned
in sorted order, with the most recent refunds appearing first.

.. cssclass:: dl-horizontal dl-params

  ``limit``
      *optional* integer. Defaults to ``10``.

  ``offset``
      *optional* integer. Defaults to ``0``.

.. container:: method-examples

   .. dcode:: scenario refund_list


.. cssclass:: method-section

List All Refunds For an Account
-------------------------------

Returns a list of refunds you've previously created against a specific account.
The refunds are returned in sorted order, with the most recent refunds
appearing first.

.. container:: method-description

  ``limit``
      *optional* integer. Defaults to ``10``.

  ``offset``
      *optional* integer. Defaults to ``0``.

.. container:: method-examples

   .. dcode:: scenario refund_account_list


.. cssclass:: method-section

Update a Refund
---------------

Updates information about a refund

.. cssclass:: dl-horizontal dl-params

   .. dcode:: form refunds.update

.. container:: method-examples

   .. dcode:: scenario refund_update
