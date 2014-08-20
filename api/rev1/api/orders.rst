Orders
======

An ``Order`` resource is a construct that logically groups related transaction
operations for a particular merchant (``Customer``).

The ``Order`` resource facilitates transaction reconciliation in the following ways:

  - \* each ``Order`` maintains an individual escrow balance, which is separate from the marketplace escrow
  - \* prevents over crediting funds by allowing payouts up to the ``amount_escrowed`` in each ``Order``
  - \* Flow of funds is trackable as funds credited from an ``Order`` are mapped to the ``Debits`` that brought the funds into it


|

.. admonition:: Requirements
  :header_class: alert alert-tab full-width alert-tab-yellow
  :body_class: alert alert-green alert-yellow

  .. cssclass:: list-noindent

    - Funds must be paid to merchants within 30 days of the charge.
    - For each ``Order``, only one merchant bank account and the marketplace bank account may be credited.

|

.. admonition:: References
  :header_class: alert alert-tab full-width alert-tab-persianBlue60
  :body_class: alert alert-green alert-persianBlue20

  .. cssclass:: mini-header

    Guides

  .. cssclass:: list-noindent

    - `Orders </1.1/guides/orders>`_

  .. cssclass:: mini-header

    API Specification

  .. cssclass:: list-noindent

    - `Orders Collection <https://github.com/balanced/balanced-api/blob/master/fixtures/orders.json>`_
    - `Order Resource <https://github.com/balanced/balanced-api/blob/master/fixtures/_models/order.json>`_

|

.. container:: header3

  Available Query Filters

.. cssclass:: dl-horizontal dl-params filters

  .. dcode:: query Orders


Create an Order
----------------

Create a new Order.

.. cssclass:: dl-horizontal dl-params

  .. dcode:: form orders.create

.. container:: code-white

  .. dcode:: scenario order_create


Fetch an Order
-----------------

Fetch the details of a previously created order.

.. container:: code-white

  .. dcode:: scenario order_show


List All Orders
----------------

List all previously created orders.

.. cssclass:: dl-horizontal dl-params

  ``limit``
      *optional* integer. Defaults to ``10``.

  ``offset``
      *optional* integer. Defaults to ``0``.

.. container:: code-white

  .. dcode:: scenario order_list


Update an Order
----------------

Update a previously created order.

.. cssclass:: dl-horizontal dl-params

  .. dcode:: form orders.update

.. container:: code-white

  .. dcode:: scenario order_update
