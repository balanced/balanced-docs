Crediting the Merchant
=========================

.. admonition:: Requirements
  :header_class: alert alert-tab full-width alert-tab-yellow
  :body_class: alert alert-green alert-yellow

  - Funds must be paid to merchants within 30 days of the charge.
  - For each ``Order``, only one merchant and the marketplace may be credited.

|

.. admonition:: References
  :header_class: alert alert-tab full-width alert-tab-persianBlue60
  :body_class: alert alert-persianBlue20 references

  .. cssclass:: mini-header

    Guides

  - `balanced.js </1.1/guides/balanced-js>`_

  .. cssclass:: mini-header

    API Reference

  - `Create a Credit for an Order </1.1/api/debits/#create-a-credit-for-an-order>`_
  - `Fetch an Order </1.1/api/orders/#fetch-an-order>`_
  
  .. cssclass:: mini-header

    API Specification

  - `Orders Collection <https://github.com/balanced/balanced-api/blob/master/fixtures/orders.json>`_
  - `Order Resource <https://github.com/balanced/balanced-api/blob/master/fixtures/_models/order.json>`_
  - `Customer Resource <https://github.com/balanced/balanced-api/blob/master/fixtures/_models/customer.json>`_

|


Topic overview
~~~~~~~~~~~~~~~

In the previous topics for this guide, we created an ``Order`` for a merchant and debited
a buyer for the order. This topic demonstrates how to issue a payout from an ``Order`` to the merchant.

By the end of this topic, you should understand how to do following:

- Issue a credit from an ``Order`` to the merchant
- Check an ``Order`` balance
- Retrieve all ``Credits`` for an ``Order``


Credit the merchant
~~~~~~~~~~~~~~~~~~~~~~~

Let's issue a payout (credit) to our merchant so they can receive funds from the order.

.. snippet:: order-credit


Check the Order balance
~~~~~~~~~~~~~~~~~~~~~~~~

Now when inspecting the order object we'll see it still has an ``amount`` of 10000
and ``amount_escrowed`` is now 2000.

.. snippet:: order-amount-escrowed



Examine Credits for an Order
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We can now retrieve all of the order's credits and ensure the credit to the merchant is there.

.. snippet:: order-credits-fetch


Checkpoint
~~~~~~~~~~~~

You should understand how to do following:

.. cssclass:: list-noindent list-style-none

  - ✓ Issue a credit from an ``Order`` to the merchant
  - ✓ Check an ``Order`` balance
  - ✓ Retrieve all ``Credits`` for an ``Order``

|

Ensure you have met these points before proceeding.

|

.. container:: box-left

 .. icon-box-widget::
   :box-classes: box box-block box-blue
   :icon-classes: icon icon-arrow-left

   :doc:`Debiting buyers <debit-buyers>`

.. container:: box-right

 .. read-more-widget::
   :box-classes: box box-block box-blue right
   :icon-classes: icon icon-arrow

   :doc:`Crediting the marketplace <credit-marketplace>`

|