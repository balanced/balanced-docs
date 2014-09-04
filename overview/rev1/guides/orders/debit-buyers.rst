Debiting Buyers
-----------------

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
  - `Create a Debit for an Order </1.1/api/debits/#create-a-debit-for-an-order>`_
  - `Fetch an Order </1.1/api/orders/#fetch-an-order>`_

  .. cssclass:: mini-header

    API Specification

  - `Orders Collection <https://github.com/balanced/balanced-api/blob/master/fixtures/orders.json>`_
  - `Order Resource <https://github.com/balanced/balanced-api/blob/master/fixtures/_models/order.json>`_

|


Topic overview
~~~~~~~~~~~~~~~~~~

By the end of this topic, you should understand how to do following:

- Create a ``Customer`` representing a buyer and associate a ``BankAccount`` to it
- Debit a buyer
- Check an ``Order`` balance
- Retrieve all ``Debits`` for an ``Order``


Prepare a buyer
~~~~~~~~~~~~~~~~~

Before we can charge our buyer we need to have a ``Customer`` resource representing them.
Let's create one now and add a card so we can charge them.

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

Let's debit the buyer for this Order. To achieve this we supply the buyer's funding instrument
as the ``source``. In this example, we'll debit the buyer's ``Card``.

.. snippet:: order-debit


Debiting the buyer's bank account works in the same manner. Supply the buyer's bank account as
the ``source``.


Check the Order balance
~~~~~~~~~~~~~~~~~~~~~~~~

We've now successfully debited a buyer. Charges to credit cards are immediate, therefore, funds will be
immediately reflected in the Order escrow. In production marketplaces, charges to bank accounts take
3-4 days to settle. Therefore, funds will be available at a later date. Marketplaces should utilize
a ``Callback`` to listen for ``Events`` from Balanced to be notified of ACH transaction state changes.
Please refer to the :doc:`Events <../events>` guide for more information.

In the case of a credit card debit, at this point, if we inspect the Order, we'll see it now has
an ``amount`` of 10000 and an escrowed amount of 10000. `amount` is the total amount of the
Order. ``amount_escrowed`` is the amount available for issuing payouts.

.. snippet:: order-amount-escrowed


Examine Debits for an Order
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We can now retrieve all of the order's debits and ensure our recent debit is there.

.. snippet:: order-debits-fetch



Checkpoint
~~~~~~~~~~~~

You should understand how to do following:

.. cssclass:: list-noindent list-style-none

  - ✓ Create a ``Customer`` representing a buyer and associate a ``BankAccount`` to it
  - ✓ Debit a buyer
  - ✓ Check the ``Order`` balance
  - ✓ Retrieve all ``Debits`` for an ``Order``

|

Ensure you have met these points before proceeding.

|

.. container:: box-left

 .. icon-box-widget::
   :box-classes: box box-block box-blue
   :icon-classes: icon icon-arrow-left

   :doc:`Create an Order <create>`

.. container:: box-right

 .. read-more-widget::
   :box-classes: box box-block box-blue right
   :icon-classes: icon icon-arrow

   :doc:`Crediting the merchant <credit-merchant>`

|
