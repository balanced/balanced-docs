Debiting Buyers
-----------------

.. admonition:: References
  :header_class: alert alert-tab full-width alert-tab-persianBlue60
  :body_class: alert alert-persianBlue20

  .. cssclass:: mini-header

    Guides

  .. cssclass:: list-noindent

    - `balanced.js </1.1/guides/balanced-js>`_

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
    - `Create a Debit for an Order </1.1/api/debits/#create-a-debit-for-an-order>`_


Topic Overview
~~~~~~~~~~~~~~~~~~

By the end of this topic, you should understand how to do following:

.. cssclass:: list-noindent

  - \* Create a ``Customer`` representing a seller (merchant) and associate a ``BankAccount`` to it.
  - \* Create an ``Order``
  - \* Update an ``Order``


Prepare a buyer
~~~~~~~~~~~~~~~~~

Before we can charge our buyer we need to have a ``Customer`` resource representing them
on which we can operate. Let's create one now and add a card so we can charge them.

.. note::
  :header_class: alert alert-tab-yellow
  :body_class: alert alert-yellow

  In this guide we will tokenize the bank account directly, however, balanced.js should be used
  to tokenize bank accounts in production marketplaces. Refer to the
  `balanced.js guide </1.1/guides/balanced-js>`_ for more information on implementing balanced.js
  in your application.

|

.. snippet:: create-buyer-and-card



Debit a buyer
~~~~~~~~~~~~~~~

Let's debit the buyer for this Order. To achieve this we debit the buyer's funding instrument.
In this example, we'll debit the buyer's ``Card``.

.. snippet:: order-debit


Debiting the buyer's bank account works in the same manner.

.. snippet:: order-debit-bank-account


We've now successfully debited a buyer. Charges to credit cards are immediate, therefore, funds will be
immediately reflected in the Order escrow.    and the funds are immediately available in the Order escrow.
At this point, if we inspect the Order, we'll see it now has an ``amount`` of
10000 and an escrowed amount of 10000. `amount` is the total amount of the
Order. ``amount_escrowed`` is the amount available for issuing payouts.

.. snippet:: order-amount-escrowed