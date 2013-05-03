credits
=======

To credit a bank account, you must create a new credit resource.


.. cssclass:: method-section

credit a new bank account
-------------------------

To credit a new bank account, you simply pass the amount along with the bank
account details. We do not store this bank account when you create a credit
this way, so you can safely assume that the information has been deleted.

.. container:: method-description

    .. dcode:: form credits.create
       :exclude: bank_account.0.bank_code bank_account.1

.. container:: method-examples

  .. dcode:: scenario credit_create_new_bank_account

.. cssclass:: method-section

credit an existing bank account
-------------------------------

To credit an existing bank account, you simply pass the amount to the
nested credit endpoint of a bank account. The ``credits_uri`` is a convenient
uri provided so that you can simply issue a ``POST`` with the amount and a
credit shall be created.


.. container:: method-description

    .. dcode:: form bank_account_credits.create

.. container:: method-examples

  .. dcode:: scenario credit_create_existing_bank_account


.. cssclass:: method-section

retrieve a credit
-----------------

Retrieves the details of a credit that you've previously created. Use the
``uri`` that was previously returned, and the corresponding credit
information will be returned.

.. container:: method-description

  .. no request

.. container:: method-examples

  .. dcode:: scenario credit_show


.. cssclass:: method-section

list all credits
----------------

Returns a list of credits you've previously created. The credits are returned
in sorted order, with the most recent credits appearing first.

.. container:: method-description

  ``limit``
      *optional* integer. Defaults to ``10``.

  ``offset``
      *optional* integer. Defaults to ``0``.

.. container:: method-examples

  .. dcode:: scenario credit_list


.. cssclass:: method-section

list all credits for a bank account
-----------------------------------

Returns a list of credits you've previously created to a specific bank account.
The ``credits_uri`` is a convenient uri provided so that you can simply issue
a ``GET`` to the ``credits_uri``. The credits are returned in sorted order,
with the most recent credits appearing first.

.. container:: method-description

  ``limit``
      *optional* integer. Defaults to ``10``.

  ``offset``
      *optional* integer. Defaults to ``0``.

.. container:: method-examples

  .. dcode:: scenario credit_bank_account_list


.. cssclass:: method-section

creating a new credit for an account
------------------------------------

.. container:: method-description

  .. dcode:: form account_credits.create

.. container:: method-examples

  .. dcode:: scenario credit_account_merchant_create


.. cssclass:: method-section

listing all credits for an account
----------------------------------

.. container:: method-description

  ``limit``
      *optional* integer. Defaults to ``10``.

  ``offset``
      *optional* integer. Defaults to ``0``.

.. container:: method-examples

  .. dcode:: scenario credit_account_list
