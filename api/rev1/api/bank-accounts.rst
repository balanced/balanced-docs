Bank Accounts
=============

You'll eventually want to be able to credit bank accounts without having to
ask your users for their information over and over again. To do this, you'll
need to create a bank account object.

.. note::
  :header_class: alert alert-tab
  :body_class: alert alert-gray

  To debit a bank account you must first :ref:`verify it <bank-account-verifications>`.


Tokenize a Bank Account (Direct)
--------------------------------

Creates a new bank account.

.. note::
  :header_class: alert alert-tab-red
  :body_class: alert alert-red
  
  This method is not recommended for production environments. Please use balanced.js for
  bank account tokenization.

.. cssclass:: dl-horizontal dl-params

  .. dcode:: form bank_accounts.create

.. container:: code-white

  .. dcode:: scenario bank_account_create


Retrieve a Bank Account
-----------------------

Retrieves the details of a bank account that has previously been created.
Supply the ``uri`` that was returned from your previous request, and
the corresponding bank account information will be returned. The same
information is returned when creating the bank account.

.. container:: method-description

    .. no request

.. container:: code-white

    .. dcode:: scenario bank_account_show


Update a Bank Account
---------------------

Update information in a card.

.. note::
  :header_class: alert alert-tab-red
  :body_class: alert alert-red
  
  Once a bank account has been associated to a customer, it cannot be
  associated to another customer.

.. cssclass:: dl-horizontal dl-params

  .. dcode:: form bank_accounts.update

.. container:: code-white

  .. dcode:: scenario bank_account_update


Delete a Bank Account
---------------------

Permanently delete a bank account. It cannot be undone. All associated credits
with a deleted bank account will not be affected.

.. container:: method-description

   .. no request

.. container:: code-white

   .. dcode:: scenario bank_account_delete


List Bank Accounts
----------------------

Returns a list of bank accounts that you've created but haven't deleted.


.. cssclass:: dl-horizontal dl-params

  ``limit``
      *optional* integer. Defaults to ``10``.

  ``offset``
      *optional* integer. Defaults to ``0``.

.. container:: code-white

    .. dcode:: scenario bank_account_list


Charge a Bank Account
---------------------

Charge a bank account.

.. note::
  :header_class: alert alert-tab-red
  :body_class: alert alert-gray
  
  A bank account must be verified with micro deposits before it can be debited. See :ref:`bank-account-verifications`.

.. cssclass:: dl-horizontal dl-params

   .. dcode:: form debits.create

.. container:: code-white

   .. dcode:: scenario bank_account_debit