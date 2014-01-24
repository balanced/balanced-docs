Working with Debits
=======================

A debit is a transaction where funds are obtained from a credit card or from a
bank account via the ACH Network. Funds obtained via credit card debits are
immediately available in escrow. Funds being obtained via ACH debits are
generally available in escrow in 3-4 business days.

Debits have a ``status`` attribute representing the current status of the debit
throughout the payout process. There are three possible ``status`` values:
``pending``, ``succeeded``, ``failed``

|

Processing methods
-------------------

Currently Balanced supports credit card debits and bank accounts via ACH.

.. note::
  :header_class: alert alert-tab
  :body_class: alert alert-green

  Bank accounts you wish to debit must first `be verified`_.


Creating a debit
--------------------

API References:

.. cssclass:: list-noindent

- `Create a Card Debit </1.1/api/debits/#create-a-card-debit>`_
- `Create a Bank Account Debit </1.1/api/debits/#create-a-bank-account-debit>`_

|

Debit a credit card example:

.. code-block:: ruby

  # bank_account_href is the stored href for the bank account
  bank_account = Balanced::BankAccount.fetch(bank_account_href)
  credit = bank_account.credit(
    :amount => 100000,
    :description => 'Payout for order #1111'
  )

.. code-block:: python

  # bank_account_href is the stored href for the bank account
  bank_account = balanced.BankAccount.fetch(bank_account_href)
  credit = bank_account.credit(
    amount=100000,
    description='Payout for order #1111'
  )


Debit a bank account example:

.. code-block:: ruby

  # bank_account_href is the stored href for the bank account
  bank_account = Balanced::BankAccount.fetch(bank_account_href)
  credit = bank_account.credit(
    :amount => 100000,
    :description => 'Payout for order #1111'
  )

.. code-block:: python

  # bank_account_href is the stored href for the bank account
  bank_account = balanced.BankAccount.fetch(bank_account_href)
  credit = bank_account.credit(
    amount=100000,
    description='Payout for order #1111'
  )


ACH Debit status flow
---------------------

Debits have a ``status`` attribute representing the current status of the debit
throughout the payout process. There are three possible ``status`` values:

.. cssclass:: dd-noindent dd-marginbottom

  ``pending``
    As soon as the debit is created through the API, the status shows
    as ``pending``. This indicates that Balanced received the information for the
    debit and will begin processing. The ACH network itself processes transactions
    in a batch format. Batch submissions are processed at 3pm PST on business days.
    If the debit is created after 3pm PST, it will not be submitted for processing
    until **3pm PST** the next business day.
  ``succeeded``
    After 3-4 days, the 
  ``failed``
    The seller's bank has up to three business days from when the money *should*
    be available to indicate a rejection along with the rejection reason.
    Unfortunately, not all banks comply with ACH network policies and may respond
    after three business days with a rejection. As soon as Balanced receives the
    rejection, the status is updated to ``failed``.

|

.. image:: https://www.balancedpayments.com/images/ach-debits/ach_debits_payment_status-01-2x-ca6bbfd6.png


.. _be verified: /1.1/api/bank-account-verifications


Reversing a credit
-------------------