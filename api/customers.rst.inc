customers
=========

Customers represent businesses or people within your marketplace. You can
associate credit cards, debit cards, bank accounts and transactions,
i.e. refunds, debits, credits.

.. cssclass:: method-section

creating a customer
-------------------

.. container:: method-description

  .. dcode:: form customers.create

.. container:: method-examples

  .. dcode:: scenario customer_create


.. cssclass:: method-section

adding a card to a customer
---------------------------

Adding a card to a customer activates the ability to debit an account, more
specifically, charging a card.

You can add multiple cards to a customer.

.. container:: method-description

  .. dcode:: form cards.create

.. container:: method-examples

  .. dcode:: scenario customer_add_card


.. cssclass:: method-section

adding a bank account to a customer
-----------------------------------

Adding a bank account to a customer activates the ability to credit a
customer, or in this case, initiate a next-day ACH payment.

.. container:: method-description

  .. dcode:: form bank_accounts.create

.. container:: method-examples

  .. dcode:: scenario customer_add_bank_account


.. cssclass:: method-section

