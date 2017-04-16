.. _debits:

Debits
======

A ``Debit`` resource represents a transaction consisting of obtaining
(charging) money from a funding instrument, i.e, a ``Card`` or ``BankAccount``.

A debit can be created by debiting a ``Card`` or ``BankAccount`` directly.

Debits have a ``status`` attribute representing the current status of the debit
throughout the payout process. There are three possible ``status`` values:

.. cssclass:: dl-horizontal dl-params dl-param-values dd-noindent dd-marginbottom

  ``pending``
    As soon as the debit is created through the API, the status shows
    as ``pending``. This indicates that Balanced received the information for the
    debit and will begin processing. The ACH network itself processes transactions
    in a batch format. Batch submissions are processed at 3:30 PM Pacific Time on business days.
    If the debit is created after 3:30 PM Pacific Time, it will not be submitted for processing
    until **3:30 PM Pacific Time the next business day**.
  ``succeeded``
    After 3-4 days, the status will change to ``succeeded`` and the funds will be
    available in escrow.
  ``failed``
    After 3-4 days, the status will change to ``failed`` if the transaction was
    not successful due to a problem such as an incorrect bank account number
    or insufficient funds.

|

.. container:: header3

  Available Query Filters

.. cssclass:: dl-horizontal dl-params filters

  .. dcode:: query Debits


.. _debits.debit-card:

Create a Card Debit
----------------------

Debit (charge) a tokenized credit card.

.. note::
  :header_class: alert alert-tab-red
  :body_class: alert alert-red

  All new production marketplaces created after November 7th 2014, are
  required to link all debits and credits via the Orders resource to remain
  compliant. Not doing so can result in having your marketplace suspended.

.. cssclass:: dl-horizontal dl-params

  .. dcode:: form debits.create

.. container:: code-white

  .. dcode:: scenario debit_order


.. _debits.debit-bank-account:

Create a Bank Account Debit
----------------------------

Debit (charge) a bank account.

.. note::
  :header_class: alert alert-tab-red
  :body_class: alert alert-red

  All new production marketplaces created after November 7th 2014, are
  required to link all debits and credits via the Orders resource to remain
  compliant. Not doing so can result in having your marketplace suspended.

.. note::
  :header_class: alert alert-tab-yellow
  :body_class: alert alert-yellow
  
  A bank account must be verified with micro deposits before it can be debited. See :ref:`bank-account-verifications`.

.. cssclass:: dl-horizontal dl-params

   .. dcode:: form debits.create

.. container:: code-white

   .. dcode:: scenario bank_account_debit_order


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


Refund a Debit
----------------

Issues a refund for a ``Debit``. A ``Refund`` can be for any amount less than or
equal to the original ``Debit`` amount.

.. cssclass:: dl-horizontal dl-params

  .. dcode:: form refunds.create

.. container:: code-white

  .. dcode:: scenario refund_create


Fetch a Debit Dispute
-------------------------

Fetch a dispute via a debit.

.. container:: code-white

  .. dcode:: scenario debit_dispute_show