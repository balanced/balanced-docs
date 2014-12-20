Refunding an Order
=======================

.. admonition:: References
  :header_class: alert alert-tab full-width alert-tab-persianBlue60
  :body_class: alert alert-persianBlue20 references

  .. cssclass:: mini-header

    Guides

  - `Settlements </1.1/guides/settlements>`_

  .. cssclass:: mini-header

    API Reference

  - `Create a Reversal </1.1/api/reversals/#create-a-reversal>`_
  - `Create a Refund </1.1/api/refunds/#create-a-refund>`_
  - `Fetch an Order </1.1/api/orders/#fetch-an-order>`_
  - `Create a Settlement </1.1/api/settlements/#create-a-settlement>`_

  .. cssclass:: mini-header

    API Specification

  - `Orders Collection <https://github.com/balanced/balanced-api/blob/master/fixtures/orders.json>`_
  - `Order Resource <https://github.com/balanced/balanced-api/blob/master/fixtures/_models/order.json>`_
  - `Reversals Collection <https://github.com/balanced/balanced-api/blob/master/fixtures/reversals.json>`_
  - `Reversal Resource <https://github.com/balanced/balanced-api/blob/master/fixtures/_models/reversal.json>`_
  - `Refunds Collection <https://github.com/balanced/balanced-api/blob/master/fixtures/refunds.json>`_
  - `Refund Resource <https://github.com/balanced/balanced-api/blob/master/fixtures/_models/refund.json>`_
  - `Settlements Collection <https://github.com/balanced/balanced-api/blob/master/fixtures/settlements.json>`_
  - `Settlement Resource <https://github.com/balanced/balanced-api/blob/master/fixtures/_models/settlement.json>`_
  - `Accounts Collection <https://github.com/balanced/balanced-api/blob/master/fixtures/accounts.json>`_
  - `Account Resource <https://github.com/balanced/balanced-api/blob/master/fixtures/_models/account.json>`_

  
Topic overview
~~~~~~~~~~~~~~~~~~

By the end of this topic, you should understand how to do following:

- Fetch an ``Order``
- Retrieve ``Credits`` for an ``Order``
- Reverse an ``Order`` ``Credit``
- Retrieve ``Debits`` for an ``Order``
- Refund an ``Order`` ``Debit``
- Check an ``Order`` balance
- Reverse a batched ``Credit`` to an ``Order``
- Settle a negative account balance


Reverse credits
~~~~~~~~~~~~~~~~

Before we can issue refunds to the buyers we must reverse any credits necessary to have funds
available in the Order escrow.

Begin by finding the Order you wish to refund.

.. snippet:: order-fetch


Next, retrieve all the credits for the ``Order``.

.. snippet:: order-credits-fetch


Determine which credits you wish to reverse and reverse each of them.

.. snippet:: credit-reverse


You may also issue a partial reversal. Just supply an amount parameter in the request.

Once the credit has been reversed, the Order's ``amount_escrowed`` will
increase by the amount of the credit. Note that a reversal can take several
days depending on the bank where the account resides. Marketplaces should utilize
a ``Callback`` to listen for ``Events`` from Balanced to be notified of ACH transaction
state changes. Please refer to the :doc:`Events <../events>` guide for more information.

.. snippet:: order-amount-escrowed


Reverse batched credits
~~~~~~~~~~~~~~~~~~~~~~~~

Reversing a credit that was originally to an account deducts the funds from the account
and returns them to the original order. To reverse a batched credit, a credit to the
merchant's ``payable`` ``Account``, we reverse it like a regular credit.

.. snippet:: credit-reverse


This reversal should succeed immediately. We can check the order balance and see the amount
will have increased by the amount of the reversal.

.. snippet:: order-amount-escrowed


Reversing a credit that was originally to and account may send the account balance negative.
When this occurs, the marketplace should create another settlement for the account. Funds 
will be debited from the specified bank account to settle the account balance back to 0.

.. note::
  :header_class: alert alert-tab-red
  :body_class: alert alert-red

  Marketplaces are responsible for settling negative account balances.


Retrieve the merchant's payable account.

.. snippet:: merchant-payable-account-fetch


Settle the account's negative balance.

.. snippet:: settlement-create


Refund debits
~~~~~~~~~~~~~~~~

Retrieve all the debits for the ``Order``.

.. snippet:: order-debits-fetch


Determine which debits you wish to refund and refund each of them.

.. snippet:: debit-refund


Once the debit has been refunded, the ``amount_escrowed`` will decrease by the
amount of the refund.

.. snippet:: order-amount-escrowed


Checkpoint
~~~~~~~~~~~~

You should understand how to do following:

.. cssclass:: list-noindent list-style-none

  - ✓ Fetch an ``Order``
  - ✓ Retrieve ``Credits`` for an ``Order``
  - ✓ Reverse an ``Order`` ``Credit``
  - ✓ Retrieve ``Debits`` for an ``Order``
  - ✓ Refund an ``Order`` ``Debit``
  - ✓ Check an ``Order`` balance
  - ✓ Reverse a batched ``Credit`` to an ``Order``
  - ✓ Settle a negative account balance

|

.. container:: box-left

 .. icon-box-widget::
   :box-classes: box box-block box-blue
   :icon-classes: icon icon-arrow-left

   :doc:`Crediting the Marketplace <credit-marketplace>`

|
