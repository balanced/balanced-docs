.. _debits:

Debits
======

To debit an account, i.e. charge a card or bank account, you must create a
new debit resource.


.. _debit.create:

Create a Debit
------------------

A debit can be created by debiting a ``Card`` or ``BankAccount`` directly.


Get a Debit
----------------

Retrieves the details of a created debit.

.. container:: method-description

  .. no request

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


Update a Debit
--------------

Updates information about a debit

.. cssclass:: dl-horizontal dl-params

  ``meta``
      *optional* **object**. Single level mapping from string keys to string values.

  ``description``
      *optional* **string**. Sequence of characters.


.. container:: code-white

  .. dcode:: scenario debit_update


Refund a Debit
--------------

Issues a refund for a particular debit. This creates a :ref:`refund <refunds>`.

.. container:: method-description

   Use the ``refund_uri`` on a :ref:`debit object <debits>`.

.. container:: code-white

   .. dcode:: scenario debit_refund


.. _info on ACH debits: http://github.com/balanced/balanced-api/issues/2
