.. _debits:

Debits
======

To debit an account, i.e. charge a card or bank account, you must create a
new debit resource.


.. _debit.create:

Create a Debit
------------------

A debit can be created by debiting a ``Card`` or ``BankAccount`` directly.


Debit a Card
------------------

Debit (charge) a tokenized credit card.

.. cssclass:: dl-horizontal dl-params

  .. dcode:: form debits.create

.. container:: code-white

  .. dcode:: scenario card_debit


Debit a Bank Account
---------------------

Debit (charge) a bank account.

.. note::
  :header_class: alert alert-tab-red
  :body_class: alert alert-gray
  
  A bank account must be verified with micro deposits before it can be debited. See :ref:`bank-account-verifications`.

.. cssclass:: dl-horizontal dl-params

   .. dcode:: form debits.create

.. container:: code-white

   .. dcode:: scenario bank_account_debit


Get a Debit
----------------

Retrieves the details of a created debit.

.. container:: method-description

  .. no request

.. container:: code-white

  .. dcode:: scenario debit_show


Update a Debit
--------------

Updates information about a debit

.. cssclass:: dl-horizontal dl-params

  .. dcode:: form debits.update


.. container:: code-white

  .. dcode:: scenario debit_update


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


.. List Debits for a Customer
.. --------------------------
.. 
.. Returns a list of debits for the specified customer. The debits are returned
.. in sorted order, with the most recent debits appearing first.
.. 
.. .. cssclass:: dl-horizontal dl-params
.. 
..   ``limit``
..       *optional* integer. Defaults to ``10``.
.. 
..   ``offset``
..       *optional* integer. Defaults to ``0``.
.. 
.. .. container:: code-white
.. 
..   .. dcode:: scenario debit_list_customer

