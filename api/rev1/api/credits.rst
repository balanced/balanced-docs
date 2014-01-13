Credits
=======

A ``Credit`` resource represents a transaction consisting
of sending money to a bank account.

|

.. container:: header3

  Available Query Filters

.. cssclass:: dl-horizontal dl-params filters

  .. dcode:: query Credits

.. note::
  :header_class: alert alert-tab
  :body_class: alert alert-gray

  Bank accounts that only receive credits do **not** need to be verified.


Create a Credit
---------------

Send money to a bank account.

.. cssclass:: dl-horizontal dl-params

    .. dcode:: form credits.create

.. container:: code-white

  .. dcode:: scenario bank_account_credit


Retrieve a Credit
-----------------

Retrieve a previously created credit.

.. container:: method-description

  .. no request

.. container:: code-white

  .. dcode:: scenario credit_show


List All Credits
----------------

Retrieve a list of all previously created credits. The credits
are returned in sorted order, with the most recent credits appearing
first.

.. cssclass:: dl-horizontal dl-params

  ``limit``
      *optional* integer. Defaults to ``10``.

  ``offset``
      *optional* integer. Defaults to ``0``.

.. container:: code-white

  .. dcode:: scenario credit_list


List All Credits for a Bank Account
-----------------------------------

Returns a list of previously created credits to a specific bank account.
The credits are returned in sorted order, with the most recent credits
appearing first.

.. container:: code-white

  .. dcode:: scenario credit_list_bank_account


Update a Credit
---------------

Update information for an existing credit.

.. cssclass:: dl-horizontal dl-params

  .. dcode:: form credits.update

.. container:: code-white

  .. dcode:: scenario credit_update

