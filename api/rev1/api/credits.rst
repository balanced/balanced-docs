Credits
=======

To credit a bank account, you must create a new credit resource.

**NOTE** If you're sending money to a bank account, known as issuing a credit,
you do **NOT** need to verify the bank account

.. cssclass:: method-section

.. Credit a New Bank Account
.. -------------------------
.. 
.. To credit a new bank account, you simply pass the amount along with the bank
.. account details. We do not store this bank account when you create a credit
.. this way, so you can safely assume that the information has been deleted.
.. 
.. .. cssclass:: dl-horizontal dl-params
.. 
..     .. dcode:: form credits.create
..        :exclude: bank_account.0.bank_code bank_account.1
.. 
.. .. container:: code-white
.. 
..   .. dcode:: scenario credit_create_new_bank_account


Create a Credit
---------------

Credit a bank account.


.. cssclass:: dl-horizontal dl-params

    .. dcode:: form credits.create

.. container:: code-white

  .. dcode:: scenario bank_account_credit


Get a Credit
------------

Retrieve a previously created credit.

.. container:: method-description

  .. no request

.. container:: code-white

  .. dcode:: scenario credit_show


Update a Credit
---------------

Update information on a credit

.. cssclass:: dl-horizontal dl-params

  .. dcode:: form credits.update

.. container:: code-white

  .. dcode:: scenario credit_update


List All Credits
----------------

Get a list of all credits previously created. The credits are returned
in sorted order, with the most recent credits appearing first.

.. cssclass:: dl-horizontal dl-params

  ``limit``
      *optional* integer. Defaults to ``10``.

  ``offset``
      *optional* integer. Defaults to ``0``.

.. container:: code-white

  .. dcode:: scenario credit_list


.. List All Credits For a Bank Account
.. -----------------------------------
.. 
.. Returns a list of credits you've previously created to a specific bank account.
.. The ``credits_uri`` is a convenient uri provided so that you can simply issue
.. a ``GET`` to the ``credits_uri``. The credits are returned in sorted order,
.. with the most recent credits appearing first.
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
..   .. dcode:: scenario credit_list_bank_account


.. Listing All Credits For a Customer
.. ----------------------------------
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
..   .. dcode:: scenario credit_customer_list
