.. _bank-account-verifications:

bank account verifications
==========================

.. note::
   :class: alert alert-info
   
   You'll only need to verify a bank account if you're planning to later debit that account,
   which is a functionality only available through our ACH Debits private beta. 
   Email support@balancedpayments.com to request access.

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


.. cssclass:: method-section

Verifying a Bank Account
------------------------

Creates a new bank account verification.

.. container:: method-description

  .. no request

.. container:: method-examples

  .. dcode:: scenario bank_account_verification_create


.. cssclass:: method-section

Retrieve a Verification for a Bank Account
------------------------------------------

Gets the verification for a bank account.

.. container:: method-description

  .. no request

.. container:: method-examples

  .. dcode:: scenario bank_account_verification_show


.. cssclass:: method-section

Confirm a Bank Account Verification
-----------------------------------

Confirms the trial deposit amounts. For the *test* environment the trial
deposit amounts are always 1 and 1.

.. container:: method-description

  .. no request

.. container:: method-examples

  .. dcode:: scenario bank_account_verification_update
