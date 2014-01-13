.. _customers:

Customers
=========

A ``Customer`` resource represents a business or person. ``Card``
and ``BankAccount`` resources may be associated to a ``Customer``.

|

.. container:: header3

  Available Query Filters

.. cssclass:: dl-horizontal dl-params filters

  .. dcode:: query Customers


.. _create-a-customer:

Create a Customer
-------------------

Create a new ``Customer``. When the ``business_name`` and ``ein`` parameters
are supplied, the ``Customer`` will be treated as a business.

.. cssclass:: dl-horizontal dl-params

  .. dcode:: form customers.create

.. container:: code-white

  .. dcode:: scenario customer_create


Retrieve a Customer
-------------------

Retrieve the details of a previously created ``Customer``.

.. container:: code-white

  .. dcode:: scenario customer_show


List all Customers
------------------

Retrieve a list of all previously created customers. The customers
are returned in sorted order, with the most recent customers
appearing first.

.. container:: code-white

  .. dcode:: scenario customer_list


Update a Customer
-----------------

Update the details of a previously created ``Customer``.

.. cssclass:: dl-horizontal dl-params

  .. dcode:: form customers.update

.. container:: code-white

  .. dcode:: scenario customer_update


Delete a Customer
-----------------

Permanently delete a customer.

.. note::
  :header_class: alert alert-tab-red
  :body_class: alert alert-red
  
  Only customers without transactions can be deleted.
  
  Deleting a Customer is permanent and cannot be undone.

.. container:: code-white

  .. dcode:: scenario customer_delete


Associate a Card
------------------

Add a ``Card`` to a specific ``Customer``. Multiple cards may be associated to
a customer.

.. note::
  :header_class: alert alert-tab-red
  :body_class: alert alert-red
  
  Once a card has been associated to a customer, it cannot be
  associated to another customer.

.. cssclass:: dl-horizontal dl-params

  .. dcode:: form cards.create

.. container:: code-white

  .. dcode:: scenario card_associate_to_customer


.. _adding-a-bank-account-to-a-customer:

Associate a Bank Account
--------------------------

Add a ``BankAccount`` to a specific ``Customer``. Multiple bank accounts may be
associated to a customer.

.. note::
  :header_class: alert alert-tab-red
  :body_class: alert alert-red
  
  Once a bank account has been associated to a customer, it cannot be
  associated to another customer.

.. cssclass:: dl-horizontal dl-params

  .. dcode:: form bank_accounts.create

.. container:: code-white

  .. dcode:: scenario bank_account_associate_to_customer
