.. _bank-account-verifications:

Bank Account Verifications
==========================

The Bank Account Verification resource is used for verifying ownership of a bank account. When a
``BankAccountVerification`` is created, two micro deposits of random amounts less than $1 are 
deposited into the target bank account. Verification amounts normally show on the bank account
owner's statement as "Balanced verification" within 2 business days.

After obtaining the verification amounts from their bank statement, the owner of the bank account
should return to a form to submit them to the Balanced API to confirm ownership of the bank account.
See `Confirm a Bank Account Verification`_.

Each ``BankAccountVerification`` allows 3 attempts to enter the correct verification amounts. After
3 failed attempts, a new verification must be created and the process must begin anew. Only one
``BankAccountVerification`` at a time may exist for a bank account.

.. note::
  :header_class: alert alert-tab
  :body_class: alert alert-gray

  Verification is **not required** for bank accounts to which only credits will be issued.
  
  Verification is **required** before a bank account can be debited.


.. container:: header3

  Available Query Filters

.. cssclass:: dl-horizontal dl-params filters

  .. dcode:: query BankAccounts


Create a Bank Account Verification
-----------------------------------

Create a new bank account verification. This initiates the process of sending
micro deposits to the bank account which will be used to verify bank account
ownership when supplied during `Confirm a Bank Account Verification`_.

.. note::
  :header_class: alert alert-tab
  :body_class: alert alert-gray

  If you're sending money to a bank account, known as issuing a credit,
  you do **NOT** need to verify the bank account


.. container:: method-description

  .. no request

.. container:: code-white

  .. dcode:: scenario bank_account_verification_create


Fetch a Bank Account Verification
------------------------------------------

.. note::
  :header_class: alert alert-tab
  :body_class: alert alert-gray

  If you're sending money to a bank account, known as issuing a credit,
  you do **NOT** need to verify the bank account

Fetches the verification for a bank account.

.. container:: method-description

  .. no request

.. container:: code-white

  .. dcode:: scenario bank_account_verification_show


.. _bank-account-verification-confirm:

Confirm a Bank Account Verification
-----------------------------------

Confirm the trial deposit amounts that were sent to the bank account.
Upon seeing the verification amounts on their bank account statement,
the customer should return to a web form and enter the amounts.
The amounts entered are compared to the amounts sent to assert valid
ownership of the bank account.

.. note::
  :header_class: alert alert-tab
  :body_class: alert alert-gray

  If you're sending money to a bank account, known as issuing a credit,
  you do **NOT** need to verify the bank account

.. note::
  :header_class: alert alert-tab
  :body_class: alert alert-gray

  For *test marketplaces*, the trial deposit amounts are always 1 and 1.


.. container:: method-description

  .. no request

.. container:: code-white

  .. dcode:: scenario bank_account_verification_update
