.. _guides.orders:

Orders
============

.. toctree::
  :hidden:
  :glob:

  orders/simple-order
  orders/refund


An ``Order`` resource is a construct that logically groups related transaction
operations for a particular seller (``Customer``). An ``Order`` allows issuing
payouts to one ``Customer`` and the marketplace bank account.


.. admonition:: Requirements
  :header_class: alert alert-tab full-width alert-tab-yellow
  :body_class: alert alert-green alert-yellow

  .. cssclass:: list-noindent

    - Funds must be paid to merchants within 30 days of the charge.
    - For each ``Order``, only one merchant bank account and the marketplace bank account may be credited.


.. admonition:: References
  :header_class: alert alert-tab full-width alert-tab-persianBlue60
  :body_class: alert alert-green alert-persianBlue20

  .. cssclass:: mini-header

    API Reference

  .. cssclass:: list-noindent

    - `Orders </1.1/api/orders>`_

  .. cssclass:: mini-header

    API Specification

  .. cssclass:: list-noindent

    - `Orders Collection <https://github.com/balanced/balanced-api/blob/master/fixtures/orders.json>`_
    - `Order Resource <https://github.com/balanced/balanced-api/blob/master/fixtures/_models/order.json>`_

|


Topics
~~~~~~~~

After reviewing each of the following topics, you should understand how to do following:

.. cssclass:: list-noindent

  - \* Create a ``Customer`` representing a seller (merchant) and associate a ``BankAccount`` to it
  - \* Create a ``Customer`` representing a buyer and associate a ``BankAccount`` to it
  - \* Create an ``Order``
  - \* Update an ``Order``
  - \* Debit a buyer
  - \* Issue a credit from an ``Order`` to the merchant
  - \* Issue a credit from an ``Order`` to the marketplace bank account
  - \* Check an ``Order`` balance
  - \* Retrieve all ``Debits`` for an ``Order``
  - \* Retrieve all ``Credits`` for an ``Order``

|

.. container:: section

  .. container:: header2

    Creating an Order

  An Order groups transactions together with the merchant at the center.
  This section explains how to create an ``Order`` for a merchant.

  .. container:: box-right

   .. read-more-widget::
     :box-classes: box box-block box-blue right
     :icon-classes: icon icon-arrow

     :doc:`Read More: Creating an Order <orders/create>`

  .. clear::

.. container:: section

  .. container:: header2

    Refund an Order

  This section demonstrates how to refund an order.

  .. container:: box-right

    .. read-more-widget::
      :box-classes: box box-block box-blue right
      :icon-classes: icon icon-arrow

      :doc:`Read More: Refund an Order <orders/refund>`

    .. clear::

|
