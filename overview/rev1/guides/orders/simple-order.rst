Creating a Simple Order
-------------------------

.. admonition:: References
  :header_class: alert alert-tab full-width alert-tab-persianBlue60
  :body_class: alert alert-persianBlue20

  .. cssclass:: mini-header

    API Specification

  .. cssclass:: list-noindent

    - `Orders Collection <https://github.com/balanced/balanced-api/blob/master/fixtures/orders.json>`_
    - `Order Resource <https://github.com/balanced/balanced-api/blob/master/fixtures/_models/order.json>`_

  .. cssclass:: mini-header

    API Reference

  .. cssclass:: list-noindent

    - `Create a Customer </1.1/api/customers/#create-a-customer>`_
    - `Create a Bank Account (Direct) </1.1/api/bank-accounts/#create-a-bank-account-direct>`_
    - `Create an Order </1.1/api/orders/#create-an-order>`_
    - `Update an Order </1.1/api/orders/#update-an-order>`_
    - `Create a Credit </1.1/api/credits/#create-a-credit>`_


By the end of this guide, you should understand how to do following:

.. cssclass:: list-noindent

  - \* Create a ``Customer`` representing a seller (merchant) and associate a ``BankAccount`` to it.
  - \* Create a ``Customer`` representing a buyer and associate a ``BankAccount`` to it.
  - \* Create an ``Order``
  - \* Update an ``Order``
  - \* Create an order debit
  - \* Check the order ``amount``
  - \* Check the order ``amount_escrowed``
  - \* Issue a credit from an ``Order`` to a seller
  - \* Issue a credit from an ``Order`` to the marketplace bank account

|

Let's begin by creating a ``Customer`` that represents our merchant.


.. snippet:: customer-create


Next, add a bank account to the merchant. In this guide we will tokenize the
bank account directly, however, balanced.js should be used to tokenize bank
accounts in production. Refer to the balanced.js guide for more
information on implementing balanced.js in your application.

.. snippet:: order-bank-account-create


Now create a buyer and add a card to it. Again, in this guide we will tokenize
the card directly, however, balanced.js should be used to tokenize credit cards
in production. Refer to the balanced.js guide for more information on
implementing balanced.js in your application.

.. snippet:: create-buyer-and-card


Next, create an ``Order``.

.. snippet:: order-create


At this point we have a merchant ``Customer`` with a bank account, a buyer
`Customer` with a credit card, and an "empty" ``Order``.

Let's give the order a description and some meta so it's easier to remember
what it was for. Of course, this information can also be specified when creating
and Order.

.. snippet:: order-update


Let's debit the buyer for this Order. This is accomplished by debiting a
specific card, in this case, the buyer's, through the Order.

.. snippet:: order-debit


At this point, if we inspect the Order, we'll see it now has an ``amount`` of
10000 and an escrowed amount of 10000. `amount` is the total amount of the
Order. ``amount_escrowed`` is the amount available for issuing payouts.

.. snippet:: order-amount-escrowed


Let's issue a payout (credit) to our merchant.

.. snippet:: order-credit


Now when inspecting the order object we'll see it still has an ``amount`` of 10000
and ``amount_escrowed`` is now 2000.

.. snippet:: order-amount-escrowed


We can now retrieve all of the order's debits with:

.. snippet:: order-debits-fetch


Likewise, we can retrieve all of the order's credits with:

.. snippet:: order-credits-fetch


Checkpoint
~~~~~~~~~~~~

You should understand how to do following:

.. cssclass:: list-noindent

  - ✓ Create a ``Customer`` representing a seller (merchant) and associate a ``BankAccount1`` to it.
  - ✓ Create a ``Customer`` representing a buyer and associate a ``BankAccount`` to it.
  - ✓ Create an ``Order``
  - ✓ Update an ``Order``
  - ✓ Create an order debit
  - ✓ Check the order ``amount``
  - ✓ Check the order ``amount_escrowed``
  - ✓ Issue a credit from an ``Order`` to a seller
  - ✓ Issue a credit from an ``Order`` to the marketplace bank account
