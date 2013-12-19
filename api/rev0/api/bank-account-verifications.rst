.. _bank-account-verifications:

Bank Account Verifications
==========================

.. note::
  :header_class: alert alert-tab
  :body_class: alert alert-gray

  If you're sending money to a bank account, known as issuing a credit,
  you do **NOT** need to verify the bank account. You'll only need to
  verify a bank account if you're planning to later debit that account.

Before you can debit a bank account you need to verify that you have access to
it. Balanced allows you to do this by creating a Verification for a
Bank Account which will result in two random amounts being credited into the
bank account. The amounts of these two deposits must be sent back as
the `amount_1` and `amount_2` params when subsequently updating this
verification. These deposits will appear on the bank accounts statement as
`Balanced verification`. (see `Confirm a Bank Account Verification`_).

If you fail to verify the bank account you must create a new verification and
begin the process again. You can only create one verification at a time and the
trial deposits should show in the bank account within 2 business days.


Create a Bank Account Verification
-----------------------------------

.. note::
  :header_class: alert alert-tab
  :body_class: alert alert-gray

  If you're sending money to a bank account, known as issuing a credit,
  you do **NOT** need to verify the bank account

Creates a new bank account verification.

.. container:: method-description

  .. no request

.. container:: code-white

  .. dcode:: scenario bank_account_verification_create


Retrieve a Bank Account Verification
------------------------------------------

.. note::
  :header_class: alert alert-tab
  :body_class: alert alert-gray

  If you're sending money to a bank account, known as issuing a credit,
  you do **NOT** need to verify the bank account

Retrieves the verification for a bank account.

.. container:: method-description

  .. no request

.. container:: code-white

  .. dcode:: scenario bank_account_verification_show


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

  For the *test* environment the trial
  deposit amounts are always 1 and 1


.. container:: method-description

  .. no request

.. container:: code-white

  .. dcode:: scenario bank_account_verification_update
