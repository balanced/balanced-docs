.. _guides.credits:

Working with Credits
=====================

A credit (payout) is a transaction where funds are sent to a bank account with
ACH direct deposit. Funds are deposited the next business day for U.S.
bank accounts and the same business day for Wells Fargo accounts.

Credits have a ``status`` attribute representing the current status of the credit
throughout the payout process. There are three possible ``status`` values:
``pending``, ``succeeded``, ``failed``

|

Payout methods
--------------

Currently Balanced only supports payouts to bank accounts via ACH but we will
add more. All of this is publicly tracked via Github issues. For example:

.. cssclass:: list-noindent

* `Payouts via Check <https://github.com/balanced/balanced-api/issues/69>`_
* `Pushing to Cards <https://github.com/balanced/balanced-api/issues/32>`_

Feel free to chime in on an existing issue or create a new one if you'd like
to see another payment method supported.


Initiating a credit
--------------------

|

API References:

.. cssclass:: list-noindent

- `Create a Reversal </1.1/api/reversals/#create-a-reversal>`_
- `Create a Credit </1.1/api/credits/#create-a-credit>`_

|

Initiating a credit (payout) is simple. Assuming we have an existing ``BankAccount`` we can
do the following:

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

.. code-block:: bash

  # :bank_account_id is the stored id for the BankAccount
  curl https://api.balancedpayments.com/bank_accounts/:bank_account_id/credits \
          -H "Accept: application/vnd.api+json;revision=1.1" \
          -u ak-test-h7F8F3u41y6LzCK4nZeVd5BafaWOUuZL: \
          -d "amount=100000" \
          -d "description=Payout for order #1111"


Credits may also be initiated via the `Dashboard`_.


Bank statement descriptor
--------------------------

Balanced allows marketplaces to specify the text that appears on statements for
a transaction. This is referred to as the soft descriptor and is set by
specifying the ``appears_on_statement_as`` field when creating a credit.

Characters that can be used are limited to the following (any other characters
will be rejected):

.. cssclass:: list-noindent

- \- ASCII letters (a-z and A-Z)
- \- Digits (0-9)
- \- Special characters (``.<>(){}[]+&!$;-%_?:#@~='"^\`|``)

The descriptor is limited to 14 characters. ACH credits do not have a prefix.

Example usage:

.. code-block:: ruby

  # bank_account_href is the stored href for the BankAccount
  bank_account = Balanced::BankAccount.fetch(bank_account_href)
  credit = bank_account.credit(
    :amount => 100000,
    :description => 'Payout for order #1111',
    :appears_on_statement_as => 'GoodCo #1111'
  )

.. code-block:: python

  # bank_account_href is the stored href for the BankAccount
  bank_account = balanced.BankAccount.fetch(bank_account_href)
  credit = bank_account.credit(
    amount=100000,
    description='Payout for order #1111',
    appears_on_statement_as='GoodCo #1111'
  )

.. code-block:: bash

  # :bank_account_id is the stored id for the BankAccount
  curl https://api.balancedpayments.com/bank_accounts/:bank_account_id/credits \
          -H "Accept: application/vnd.api+json;revision=1.1" \
          -u ak-test-h7F8F3u41y6LzCK4nZeVd5BafaWOUuZL: \
          -d "amount=100000" \
          -d "description=Payout for order #1111" \
          -d "appears_on_statement_as=GoodCo #1111"

Payout status flow
-------------------

Credits have a ``status`` attribute representing the current status of the credit
throughout the payout process. There are three possible ``status`` values:

.. cssclass:: dd-noindent dd-marginbottom

  ``pending``
    As soon as the credit is created through the API, the status shows
    as ``pending``. This indicates that Balanced received the information for the
    credit and will begin processing. The ACH network itself processes transactions
    in a batch format. Batch submissions are processed at 3pm PST on business days.
    If the credit is created after 3pm PST, it will not be submitted for processing
    until **3pm PST** the next business day.
  ``succeeded``
    One business day after the batch submission, the status will change to
    ``succeeded``. That is the *expected* status of the credit. If the account
    number and routing number were entered correctly, the money should in fact
    be available to the seller. However, there is no immediate confirmation
    regarding the transaction showing up in the seller's account successfully.
  ``failed``
    The seller's bank has up to three business days from when the money *should*
    be available to indicate a rejection along with the rejection reason.
    Unfortunately, not all banks comply with ACH network policies and may respond
    after three business days with a rejection. As soon as Balanced receives the
    rejection, the status is updated to ``failed``.

|

.. image:: https://www.balancedpayments.com/images/payouts/payouts_status-2x-0ed0a72a.png


Reversing a credit
-------------------

|

API References:

.. cssclass:: list-noindent

- `Create a Reversal </1.1/api/reversals/#create-a-reversal>`_

|

In the event that you need to cancel a payout, e.g. a user is not
satisfied with the product, you can create a ``Reversal``.

.. code-block:: ruby

  # credit_href is the stored href for the Credit
  credit = Balanced::Credit.fetch(credit_href)
  reversal = credit.reverse(
    :amount => 100000,
    :description => 'Reversal for Order #1111',
    :meta => {
      'merchant.feedback' => 'positive',
      'fulfillment.item.condition' => 'OK',
      'user.refund_reason' => 'not happy with product'
    }
  )

.. code-block:: python

  # credit_href is the stored href for the Credit
  credit = balanced.Credit.fetch(credit_href)
  reversal = credit.reverse(
      amount=100000,
      description="Reversal for order #1111",
      meta={
          "merchant.feedback": "positive",
          "user.refund_reason": "not happy with product",
          "fulfillment.item.condition": "OK",
      }
  )

.. code-block:: bash

  # :credit_id is the stored id for the Credit
  curl https://api.balancedpayments.com/credits/:credit_id/reversals \
       -H "Accept: application/vnd.api+json;revision=1.1" \
       -u ak-test-h7F8F3u41y6LzCK4nZeVd5BafaWOUuZL: \
       -d "amount=100000" \
       -d "description=Reversal for Order #1111" \
       -d "meta[merchant.feedback]=positive" \
       -d "meta[user.refund_reason]=not happy with product" \
       -d "meta[fulfillment.item.condition]=OK"

The status flow of a reversal is as follows:

.. image:: https://www.balancedpayments.com/images/payouts/payouts_reversal_status-2x-dc135471.png

|

Credits may also be reversed from the `Dashboard`_.



.. _sample page: https://gist.github.com/2662770
.. _balanced.js: https://js.balancedpayments.com/v1/balanced.js
.. _testing documentation: /docs/testing#simulating-card-failures
.. _jQuery: http://www.jquery.com
.. _issues: https://github.com/balanced/balanced-api/issues
.. _github issue #151: https://github.com/balanced/balanced-api/issues/151
.. _github issue #70: https://github.com/balanced/balanced-api/issues/70
.. _Dashboard: https://dashboard.balancedpayments.com/