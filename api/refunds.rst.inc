.. _refunds:

refunds
=======

Refunds typically take one business day to reflect on a card statement, but it's possible for the issuing bank to take five business days to process the refund.


.. cssclass:: method-section

issue a refund
--------------

Issues a refund from a debit. You can either refund the full amount of the
debit or you can issue a partial refund, where the amount is less than the
charged amount.

.. container:: method-description

  .. dcode:: form refunds.create
     :exclude: account_uri

.. container:: method-examples

  .. dcode:: scenario refund_create

.. todo:: partial refund

.. cssclass:: method-section

retrieve a refund
-----------------

Retrieves the details of a refund that you've previously created. Use the
``uri`` that was previously returned, and the corresponding refund
information will be returned.

.. container:: method-description

  .. no request

.. container:: method-examples

   .. dcode:: scenario refund_show


.. cssclass:: method-section

list all refunds
----------------

Returns a list of refunds you've previously created. The refunds are returned
in sorted order, with the most recent refunds appearing first.

.. container:: method-description

  ``limit``
      *optional* integer. Defaults to ``10``.

  ``offset``
      *optional* integer. Defaults to ``0``.

.. container:: method-examples

   .. dcode:: scenario refund_list


.. cssclass:: method-section

list all refunds for an account
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

update a refund
---------------

Updates information about a refund

.. container:: method-description

   .. dcode:: form refunds.update

.. container:: method-examples

   .. dcode:: scenario refund_update
