.. _customers:

Customers
=========

Customers represent businesses or people within your marketplace. You can
associate credit cards, debit cards, bank accounts and transactions,
i.e. refunds, debits, credits.


.. _create-a-customer:

Create a Customer
-------------------

.. cssclass:: dl-horizontal dl-params

  .. dcode:: form customers.create

.. container:: code-white

  .. dcode:: scenario customer_create


Get a Customer
---------------

.. container:: code-white

  .. dcode:: scenario customer_show


List Customers
---------------

.. container:: code-white

  .. dcode:: scenario customer_list


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
---------------------------

Adding a card to a customer activates the ability to debit an account, more
specifically, charging a card.

You can add multiple cards to a customer.

.. cssclass:: dl-horizontal dl-params

  .. dcode:: form cards.create

.. container:: code-white

  .. dcode:: scenario customer_add_card



.. _adding-a-bank-account-to-a-customer:

Associate a Bank Account
-----------------------------------

Adding a bank account to a customer activates the ability to credit a
customer, or in this case, initiate a next-day ACH payment.

.. cssclass:: dl-horizontal dl-params

  .. dcode:: form bank_accounts.create

.. container:: code-white

  .. dcode:: scenario customer_add_bank_account
