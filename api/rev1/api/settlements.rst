.. _settlements:

Settlements
============

A ``Settlement`` represents the settlement of an ``Account`` balance
against a bank account.

|

.. container:: header3

  Available Query Filters

.. cssclass:: dl-horizontal dl-params filters

  .. dcode:: query Settlements


Create a Settlement
--------------------

Create a Settlement. The balance of the specified account will be settled
against the specified funding instrument.

.. cssclass:: dl-horizontal dl-params

    .. dcode:: form settlements.create

.. container:: code-white

  .. dcode:: scenario settlement_create


Fetch a Settlement
--------------------

Fetches the details of a Settlement.

.. container:: code-white

  .. dcode:: scenario settlement_show


List All Settlements
---------------------

Returns a list of all Settlements for a marketplace.

.. cssclass:: dl-horizontal dl-params

  ``limit``
      *optional* integer. Defaults to ``10``.

  ``offset``
      *optional* integer. Defaults to ``0``.


.. container:: code-white

  .. dcode:: scenario settlement_list


List All Settlements for an Account
------------------------------------

Returns a list of all Settlements for the specified ``Account``.

.. container:: code-white

  .. dcode:: scenario settlement_list_account
