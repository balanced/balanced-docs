.. _accounts:

Accounts
=========

An ``Account`` is a funding instrument resource which is able to store
a balance internally within the Balanced system.

Accounts are created only by the Balanced system. Only one account type
is currently available, ``payable``. Each ``Customer`` instance has one
payable account. Accounts are not debitable.

Reversals of credits issued to Accounts may cause the account balance to
go negative. The marketplace is responsible for settling the negative
account balance.

|

.. container:: header3

  Available Query Filters

.. cssclass:: dl-horizontal dl-params filters

  .. dcode:: query Accounts


Fetch an Account
-----------------

Fetches the details of an Account.

.. container:: code-white

  .. dcode:: scenario account_show


List All Accounts
------------------

Returns a list of all accounts for a marketplace.

.. cssclass:: dl-horizontal dl-params

  ``limit``
      *optional* integer. Defaults to ``10``.

  ``offset``
      *optional* integer. Defaults to ``0``.

  ``type``
      *optional* string. The account type. Available types: ``payable``


.. container:: code-white

  .. dcode:: scenario account_list


List All Accounts for a Customer
---------------------------------

Returns a list of all accounts for the specified ``Customer``.

.. container:: code-white

  .. dcode:: scenario account_list_customer


Credit an Account
--------------------

Move funds to an account.

.. cssclass:: dl-horizontal dl-params

  .. dcode:: form credits.create

.. container:: code-white

  .. dcode:: scenario account_credit