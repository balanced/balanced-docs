Credits
=======

To credit a bank account, you must create a new credit resource.

**NOTE** If you're sending money to a bank account, known as issuing a credit,
you do **NOT** need to verify the bank account

.. cssclass:: method-section

Credit a New Bank Account
-------------------------

To credit a new bank account, you simply pass the amount along with the bank
account details. We do not store this bank account when you create a credit
this way, so you can safely assume that the information has been deleted.

.. cssclass:: dl-horizontal dl-params

    .. dcode:: form credits.create
       :exclude: bank_account.0.bank_code bank_account.1

.. container:: code-white

   .. dcode:: scenario credit_create_new_bank_account

.. cssclass:: method-section

Credit An Existing Bank Account
-------------------------------

To credit an existing bank account, you simply pass the amount to the
nested credit endpoint of a bank account. The ``credits_uri`` is a convenient
uri provided so that you can simply issue a ``POST`` with the amount and a
credit shall be created.


.. cssclass:: dl-horizontal dl-params

    .. dcode:: form credits.create

.. TODO: fix the name on this

.. container:: code-white

   .. dcode:: scenario credit_create_existing_bank_account

.. cssclass:: method-section

Retrieve a Credit
-----------------

Retrieves the details of a credit that you've previously created. Use the
``uri`` that was previously returned, and the corresponding credit
information will be returned.

.. container:: method-description

  .. no request

.. container:: code-white

  .. dcode:: scenario credit_show


.. cssclass:: method-section

List All Credits
----------------

Returns a list of credits you've previously created. The credits are returned
in sorted order, with the most recent credits appearing first.

.. cssclass:: dl-horizontal dl-params

  ``limit``
      *optional* integer. Defaults to ``10``.

  ``offset``
      *optional* integer. Defaults to ``0``.

.. container:: code-white

  .. dcode:: scenario credit_list


.. cssclass:: method-section

List All Credits For a Bank Account
-----------------------------------

Returns a list of credits you've previously created to a specific bank account.
The ``credits_uri`` is a convenient uri provided so that you can simply issue
a ``GET`` to the ``credits_uri``. The credits are returned in sorted order,
with the most recent credits appearing first.

.. cssclass:: dl-horizontal dl-params

  ``limit``
      *optional* integer. Defaults to ``10``.

  ``offset``
      *optional* integer. Defaults to ``0``.

.. container:: code-white

  .. dcode:: scenario credit_bank_account_list


.. cssclass:: method-section

Creating a New Credit For an Account
------------------------------------

.. cssclass:: dl-horizontal dl-params

  .. dcode:: form account_credits.create/credits.create

.. TODO: fix this account_credits.create

.. container:: code-white

  .. dcode:: scenario credit_account_merchant_create


.. cssclass:: method-section

Listing All Credits For an Account
----------------------------------

.. cssclass:: dl-horizontal dl-params

  ``limit``
      *optional* integer. Defaults to ``10``.

  ``offset``
      *optional* integer. Defaults to ``0``.

.. container:: code-white

  .. dcode:: scenario credit_account_list
