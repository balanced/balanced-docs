Bank Accounts
=============

A ``BankAccount`` is a funding instrument resource that represents a
bank account. Bank account information is securely vaulted is
referenced by a ``href``. A ``BankAccount`` may be created multiple
times, each ``BankAccount`` represented by a unique href. Each
``BankAccount`` may be associated one time only and to only one
``Customer``. Once associated, a ``Card`` may not be disassociated
from the ``Customer``, it may only be unstored.

|

.. container:: header3

  Available Query Filters

.. cssclass:: dl-horizontal dl-params filters

  .. dcode:: query BankAccounts

.. note::
  :header_class: alert alert-tab
  :body_class: alert alert-green

  To debit a bank account you must first :ref:`verify it <bank-account-verifications>`.


Create a Bank Account (Direct)
--------------------------------

Creates a new ``BankAccount`` resource that represents a bank account funding instrument.

.. note::
  :header_class: alert alert-tab-red
  :body_class: alert alert-red
  
  This method is not recommended for production environments. Please use balanced.js for
  creating bank accounts.

.. cssclass:: dl-horizontal dl-params

  .. dcode:: form bank_accounts.create

.. container:: code-white

  .. dcode:: scenario bank_account_create


Fetch a Bank Account
-----------------------

Fetches the details of a previously created bank account.

.. container:: method-description

    .. no request

.. container:: code-white

    .. dcode:: scenario bank_account_show


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


Charge a Bank Account
---------------------

Charge a bank account.

.. note::
  :header_class: alert alert-tab-yellow
  :body_class: alert alert-yellow
  
  A bank account must be verified with micro deposits before it can be debited. See :ref:`bank-account-verifications`.

.. cssclass:: dl-horizontal dl-params

   .. dcode:: form debits.create

.. container:: code-white

   .. dcode:: scenario bank_account_debit