Creating an Order
-------------------------

.. admonition:: References
  :header_class: alert alert-tab full-width alert-tab-persianBlue60
  :body_class: alert alert-persianBlue20 references

  .. cssclass:: mini-header

    Guides

  - `balanced.js </1.1/guides/balanced-js>`_

  .. cssclass:: mini-header

    API Reference

  - `Create a Customer </1.1/api/customers/#create-a-customer>`_
  - `Create a Bank Account (Direct) </1.1/api/bank-accounts/#create-a-bank-account-direct>`_
  - `Associate a Bank Account to a Customer </1.1/api/bank-accounts/#associate-a-bank-account-to-a-customer>`_
  - `Create an Order </1.1/api/orders/#create-an-order>`_
  - `Update an Order </1.1/api/orders/#update-an-order>`_
  - `Fetch an Order </1.1/api/orders/#fetch-an-order>`_

  .. cssclass:: mini-header

    API Specification

  - `Orders Collection <https://github.com/balanced/balanced-api/blob/master/fixtures/orders.json>`_
  - `Order Resource <https://github.com/balanced/balanced-api/blob/master/fixtures/_models/order.json>`_

|


Topic overview
~~~~~~~~~~~~~~~~~~

By the end of this topic, you should understand how to do following:

- Create a ``Customer`` representing a merchant (seller) and associate a ``BankAccount`` to it.
- Create an ``Order``
- Update an ``Order``
- Fetch an ``Order``
- Check an ``Order`` balance


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


Check the Order balance
~~~~~~~~~~~~~~~~~~~~~~~~

When inspecting the order object we'll see it has an ``amount`` of 0
and ``amount_escrowed`` of now 0.

.. snippet:: order-amount-escrowed

- ``amount`` is the total amount of all funds obtained into the Order since its creation.
- ``amount_escrowed`` is the total amount of funds that have not yet been paid out.


Fetch an Order
~~~~~~~~~~~~~~~~~

You'll want to store ``Order`` hrefs in your database for quick retrieval at a later date. When that
time arrives, fetch the ``Order`` resource with the href.

.. snippet:: order-fetch



Checkpoint
~~~~~~~~~~~~

You should understand how to do following:

.. cssclass:: list-noindent list-style-none

  - ✓ Create a ``Customer`` representing a merchant (seller) and associate a ``BankAccount`` to it.
  - ✓ Create an ``Order``
  - ✓ Update an ``Order``
  - ✓ Fetch an ``Order``
  - ✓ Check an ``Order`` balance

|

Ensure you have met these points before proceeding.


.. container:: box-right

 .. read-more-widget::
   :box-classes: box box-block box-blue right
   :icon-classes: icon icon-arrow

   :doc:`Debiting buyers <debit-buyers>`

|

