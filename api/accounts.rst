accounts
========

Accounts help facilitate managing multiple credit cards, debit cards,
and bank accounts along with different financial transaction operations, i.e.
refunds, debits, credits.

.. cssclass:: method-section

creating an account
-------------------

.. container:: method-description

  .. dcode:: form accounts.create

.. container:: code-white

  .. dcode:: scenario account_create


.. cssclass:: method-section

adding a card to an account
---------------------------

Adding a card to an account activates the ability to debit an account, more
specifically, charging a card.

You can add multiple cards to an account.

Balanced associates a ``buyer`` role to signify whether or not an account
has a valid credit card, to acquire funds from.

.. container:: method-description

  .. dcode:: form cards.create

.. container:: code-white

  .. dcode:: scenario account_add_card


.. cssclass:: method-section

adding a bank account to an account
-----------------------------------

Adding a bank account to an account activates the ability to credit an
account, or in this case, initiate a next-day ACH payment.

Balanced **does not** associate a role to signify whether or not an account
has a valid bank account to send money to.

.. container:: method-description

  .. dcode:: form bank_accounts.create

.. container:: code-white

  .. dcode:: scenario account_create_merchant


.. cssclass:: method-section

underwriting an individual
--------------------------

A person, or an individual, is a US based individual or a sole proprietor.

Balanced associates a ``merchant`` role to signify whether or not an account
has been underwritten.

.. container:: method-description

    .. dcode:: form merchant_accounts.create
       :exclude: ssn_last_4 production person

.. container:: code-white

  .. dcode:: scenario account_underwrite_person


.. cssclass:: method-section

underwriting a business
-----------------------

Balanced associates a ``merchant`` role to signify whether or not an account
has been underwritten.

.. container:: method-description

    .. dcode:: form merchants.create
       :exclude: ssn_last_4 person.ssn_last_4 production
       :required: merchant.person

.. container:: code-white

  .. dcode:: scenario account_underwrite_business
