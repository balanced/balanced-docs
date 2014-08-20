Creating an Order
-------------------------

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
    - `Create an Order </1.1/api/orders/#create-an-order>`_
    - `Update an Order </1.1/api/orders/#update-an-order>`_
    - `Create a Credit </1.1/api/credits/#create-a-credit>`_

|

Topic Overview
~~~~~~~~~~~~~~~~~~

By the end of this topic, you should understand how to do following:

.. cssclass:: list-noindent

  - \* Create a ``Customer`` representing a seller (merchant) and associate a ``BankAccount`` to it.
  - \* Create an ``Order``
  - \* Update an ``Order``

|

Prepare a merchant
~~~~~~~~~~~~~~~~~~~

Orders are based around merchants, which are instances of ``Customer`` resources. Let's begin by
creating a ``Customer`` that represents our merchant.


.. snippet:: customer-create


This merchant will eventually want to receive payouts, therefore, they're going to need a
bank account. Let's go ahead and add a bank account to the merchant.

.. note::
  :header_class: alert alert-tab-yellow
  :body_class: alert alert-yellow

  In this guide we will tokenize the bank account directly, however, balanced.js should be used
  to tokenize bank accounts in production marketplaces. Refer to the
  `balanced.js guide </1.1/guides/balanced-js>`_ for more information on implementing balanced.js
  in your application.


.. snippet:: order-bank-account-create


Create the Order
~~~~~~~~~~~~~~~~~~~

Next, create an ``Order`` for the merchant.

.. snippet:: order-create




Update the Order
~~~~~~~~~~~~~~~~~

If you need to alter an ``Order`` description or wish to annotate it with meta,
you can update the Order. Let's give the order a different description and
some meta so it's easier to remember what it was for. This information
can also be specified when creating and Order.

.. snippet:: order-update



Checkpoint
~~~~~~~~~~~~

You should understand how to do following:

.. cssclass:: list-noindent

  - ✓ Create a ``Customer`` representing a seller (merchant) and associate a ``BankAccount`` to it.
  - ✓ Create an ``Order``
  - ✓ Update an ``Order``

|

Ensure you have met these points before proceeding.


.. container:: box-right

 .. read-more-widget::
   :box-classes: box box-block box-blue right
   :icon-classes: icon icon-arrow

   :doc:`Debiting buyers <debit-buyers>`

|


Sort
~~~~~~~~~~





Let's issue a payout (credit) to our merchant.

.. snippet:: order-credit


Now when inspecting the order object we'll see it still has an ``amount`` of 10000
and ``amount_escrowed`` is now 2000.

.. snippet:: order-amount-escrowed


We can now retrieve all of the order's debits with:

.. snippet:: order-debits-fetch


Likewise, we can retrieve all of the order's credits with:

.. snippet:: order-credits-fetch
