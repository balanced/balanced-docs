.. _guides.orders:

Orders
============

.. toctree::
  :hidden:
  :glob:

  orders/create
  orders/debit-buyers
  orders/credit-merchant
  orders/credit-marketplace
  orders/refund


An ``Order`` resource is a construct that logically groups related transaction
operations for a particular merchant (``Customer``).

The ``Order`` resource facilitates transaction reconciliation in the following ways:

  - each ``Order`` maintains an individual escrow balance, which is separate from the marketplace escrow
  - prevents over crediting funds by allowing payouts up to the ``amount_escrowed`` in each ``Order``
  - Flow of funds is trackable as funds credited from an ``Order`` are mapped to the ``Debits`` that brought the funds into it


.. admonition:: Requirements
  :header_class: alert alert-tab full-width alert-tab-yellow
  :body_class: alert alert-green alert-yellow

  - Funds must be paid to merchants within 30 days of the charge.
  - For each ``Order``, only one merchant and the marketplace may be credited.


.. admonition:: References
  :header_class: alert alert-tab full-width alert-tab-persianBlue60
  :body_class: alert alert-green alert-persianBlue20 references

  .. cssclass:: mini-header

    API Reference

  - `Orders </1.1/api/orders>`_

  .. cssclass:: mini-header

    API Specification

  - `Orders Collection <https://github.com/balanced/balanced-api/blob/master/fixtures/orders.json>`_
  - `Order Resource <https://github.com/balanced/balanced-api/blob/master/fixtures/_models/order.json>`_

|


Topics
~~~~~~~~

After reviewing each of the following topics, you should understand how to do following:

- Create a ``Customer`` representing a seller (merchant) and associate a ``BankAccount`` to it
- Create a ``Customer`` representing a buyer and associate a ``BankAccount`` to it
- Create an ``Order``
- Update an ``Order``
- Debit a buyer
- Issue a credit from an ``Order`` to the merchant
- Issue a credit from an ``Order`` to the marketplace bank account
- Check an ``Order`` balance
- Retrieve all ``Debits`` for an ``Order``
- Retrieve all ``Credits`` for an ``Order``

|

.. container:: section

  .. container:: header2

    Creating an Order

  An Order groups transactions together with the merchant at the center.
  This topic explains how to create an ``Order`` for a merchant.

  .. container:: box-right

   .. read-more-widget::
     :box-classes: box box-block box-blue right
     :icon-classes: icon icon-arrow

     :doc:`Read More: Creating an Order <orders/create>`

  .. clear::


.. container:: section

  .. container:: header2

    Debiting buyers

  This topic demonstrates how to debit buyers for an ``Order``.

  .. container:: box-right

   .. read-more-widget::
     :box-classes: box box-block box-blue right
     :icon-classes: icon icon-arrow

     :doc:`Read More: Debiting buyers <orders/debit-buyers>`

  .. clear::


.. container:: section

  .. container:: header2

    Crediting the Merchant

  This topic explains how to issue credits (payouts) to merchants.

  .. container:: box-right

   .. read-more-widget::
     :box-classes: box box-block box-blue right
     :icon-classes: icon icon-arrow

     :doc:`Read More: Crediting the Merchant <orders/credit-merchant>`

  .. clear::


.. container:: section

  .. container:: header2

    Crediting the Marketplace

  Marketplaces often need to take a cut of transactions. This topic demonstrates how to
  issue credits (payouts) to the marketplace.

  .. container:: box-right

   .. read-more-widget::
     :box-classes: box box-block box-blue right
     :icon-classes: icon icon-arrow

     :doc:`Read More: Crediting the Marketplace <orders/credit-marketplace>`

  .. clear::


.. container:: section

  .. container:: header2

    Refund an Order

  Sometimes it becomes necessary to refund a transaction. This topic demonstrates how to refund an ``Order``.

  .. container:: box-right

    .. read-more-widget::
      :box-classes: box box-block box-blue right
      :icon-classes: icon icon-arrow

      :doc:`Read More: Refund an Order <orders/refund>`

    .. clear::

|
