.. _debits:

Debits
======

A ``Debit`` resource represents a transaction consisting of obtaining
(charging) money from a funding instrument, i.e, a ``Card`` or ``BankAccount``.

A debit can be created by debiting a ``Card`` or ``BankAccount`` directly.

|

.. container:: header3

  Available Query Filters

.. cssclass:: dl-horizontal dl-params filters

  .. dcode:: query Debits


.. _debits.debit-card:

Create a Card Debit
----------------------

Debit (charge) a tokenized credit card.

.. cssclass:: dl-horizontal dl-params

  .. dcode:: form debits.create

.. container:: code-white

  .. dcode:: scenario card_debit


.. _debits.debit-bank-account:

Create a Bank Account Debit
----------------------------

Debit (charge) a bank account.

.. note::
  :header_class: alert alert-tab-red
  :body_class: alert alert-gray
  
  A bank account must be verified with micro deposits before it can be debited. See :ref:`bank-account-verifications`.

.. cssclass:: dl-horizontal dl-params

   .. dcode:: form debits.create

.. container:: code-white

   .. dcode:: scenario bank_account_debit


Fetch a Debit
----------------

Fetches the details of a created debit.

.. container:: code-white

  .. dcode:: scenario debit_show


List All Debits
---------------

Returns a list of all debits created in the marketplace. The debits are returned
in sorted order, with the most recent debits appearing first.

.. cssclass:: dl-horizontal dl-params

  ``limit``
      *optional* integer. Defaults to ``10``.

  ``offset``
      *optional* integer. Defaults to ``0``.

.. container:: code-white

  .. dcode:: scenario debit_list


Update a Debit
--------------

Updates information about a debit

.. cssclass:: dl-horizontal dl-params

  .. dcode:: form debits.update

.. container:: code-white

  .. dcode:: scenario debit_update