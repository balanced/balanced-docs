.. _guides.debits:

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


Creating a debit
--------------------

API References:

.. cssclass:: list-noindent

- `Create a Card Debit </1.1/api/debits/#create-a-card-debit>`_
- `Create a Bank Account Debit </1.1/api/debits/#create-a-bank-account-debit>`_

|

Debit a credit card example:

.. code-block:: ruby

  # bank_account_href is the stored href for the BankAccount
  bank_account = Balanced::BankAccount.fetch(bank_account_href)
  credit = bank_account.credit(
    :amount => 100000,
    :description => 'Payout for order #1111'
  )

.. code-block:: python

  # bank_account_href is the stored href for the BankAccount
  bank_account = balanced.BankAccount.fetch(bank_account_href)
  credit = bank_account.credit(
    amount=100000,
    description='Payout for order #1111'
  )


Debit a bank account example:

.. code-block:: ruby

  # bank_account_href is the stored href for the BankAccount
  bank_account = Balanced::BankAccount.fetch(bank_account_href)
  credit = bank_account.credit(
    :amount => 100000,
    :description => 'Payout for order #1111'
  )

.. code-block:: python

  # bank_account_href is the stored href for the BankAccount
  bank_account = balanced.BankAccount.fetch(bank_account_href)
  bank_account.debit(
    appears_on_statement_as='Statement text',
    amount=5000,
    description='Some descriptive text for the debit in the dashboard'
  )

.. note::
  :header_class: alert alert-tab
  :body_class: alert alert-green

  Bank accounts you wish to debit must first `be verified`_.


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
    After 3-4 days, the status will change to ``succeeded`` and the funds will be
    available in escrow.
  ``failed``
    After 3-4 days, the status will change to ``failed`` if the transaction was
    not successful due to a problem such as an incorrect bank account number
    or insufficient funds.

|

.. image:: https://www.balancedpayments.com/images/ach-debits/ach_debits_payment_status-01-2x-ca6bbfd6.png


.. _be verified: /1.1/api/bank-account-verifications


Refunding a debit
-------------------

|

API References:

.. cssclass:: list-noindent

- `Create a Refund </1.1/api/refunds/#create-a-refund>`_

|

In the event that you need to cancel a payout, e.g. a user is not satisfied with
the product, you can create a ``Refund``.

.. note::
  :header_class: alert alert-tab
  :body_class: alert alert-green

  For credit cards it typically takes one business day for refunds to
  be reflected on a card statement, but it's possible for the issuing bank to
  take as many as five business days to process a refund. ACH debit refunds
  generally take 3-5 days to process.

.. code-block:: ruby

  # debit_href is the stored href for the Debit
  debit = Balanced::Debit.fetch(debit_href)
  debit.refund(
    :amount => 3000,
    :description => 'Refund for Order #1111',
    :meta => {
      'merchant.feedback' => 'positive',
      'fulfillment.item.condition' => 'OK',
      'user.refund_reason' => 'not happy with product'
    }
  )

.. code-block:: python

  # debit_href is the stored href for the Debit
  debit = balanced.Debit.fetch(debit_href)
  refund = debit.refund(
      amount=3000,
      description="Refund for Order #1111",
      meta={
          "merchant.feedback": "positive",
          "user.refund_reason": "not happy with product",
          "fulfillment.item.condition": "OK",
      }
  )

Debit may also be refunded from the `Dashboard`_.



.. _Dashboard: https://dashboard.balancedpayments.com/