.. _customers:

Customers
=========

Customers represent businesses or people within your marketplace. You can
associate credit cards, debit cards, bank accounts and transactions,
i.e. refunds, debits, credits.

.. cssclass:: method-section


.. _creating-a-customer:

Creating a Customer
-------------------

.. cssclass:: dl-horizontal dl-params

  .. dcode:: form customers.create

.. container:: code-white

  .. dcode:: scenario customer_create


.. cssclass:: method-section


.. _adding-a-card-to-a-customer:

Adding a Card to a Customer
---------------------------

Adding a card to a customer activates the ability to debit an account, more
specifically, charging a card.

You can add multiple cards to a customer.

.. cssclass:: dl-horizontal dl-params

  .. dcode:: form cards.create

.. container:: code-white

  .. dcode:: scenario customer_add_card


.. cssclass:: method-section


.. _adding-a-bank-account-to-a-customer:

Adding a Bank Account to a Customer
-----------------------------------

Adding a bank account to a customer activates the ability to credit a
customer, or in this case, initiate a next-day ACH payment.

.. cssclass:: dl-horizontal dl-params

  .. dcode:: form bank_accounts.create

.. container:: code-white

  .. dcode:: scenario customer_add_bank_account


.. cssclass:: method-section


Delete a Customer
-----------------

Permanently delete a customer. It cannot be undone. Only customers
without transactions can be deleted.

.. container:: code-white

  .. dcode:: scenario customer_delete
