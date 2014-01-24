.. _debits:

Debits
======

A ``Debit`` resource represents a transaction consisting of obtaining
(charging) money from a funding instrument, i.e, a ``Card`` or ``BankAccount``.

A debit can be created by debiting a ``Card`` or ``BankAccount`` directly.

Debits have a ``status`` attribute representing the current status of the debit
throughout the payout process. There are three possible ``status`` values:

.. cssclass:: dd-noindent dd-marginbottom

  ``pending``
    As soon as the debit is created through the API, the status shows
    as ``pending``. This indicates that Balanced received the information for the
    debit and will begin processing. The ACH network itself processes transactions
    in a batch format. Batch submissions are processed at 3pm PST on business days.
    If the debit is created after 3pm PST, it will not be submitted for processing
    until **3pm PST** the next business day.
  ``paid``
    After 3-4 days, the status will change to ``succeeded`` and the funds will be
    available in escrow.
  ``failed``
    After 3-4 days, the status will change to ``failed`` if the transaction was
    not successful due to a problem such as an incorrect bank account number
    or insufficient funds.

|

.. cssclass:: method-section

.. _debits.create:

Create a New Debit
------------------

.. todo:: debit an account with different cards
.. todo:: debit an owner account

Debits an account. Returns a ``uri`` that  can later be used to reference this
debit.

Successful creation of a debit using a card will return an associated ``hold``
mapping as part of the response. This :ref:`hold <holds>` was created and
captured behind the scenes automatically. For ACH debits there is no
corresponding hold.

.. cssclass:: dl-horizontal dl-params

  .. dcode:: form debits.create

.. container:: code-white

  .. dcode:: scenario customer_create_debit


.. cssclass:: method-section

Retrieve a Debit
----------------

Retrieves the details of a created debit.

.. container:: method-description

  .. no request

.. container:: code-white

  .. dcode:: scenario debit_show


.. cssclass:: method-section

List All Debits
---------------

Returns a list of debits you've previously created. The debits are returned
in sorted order, with the most recent debits appearing first.

.. cssclass:: dl-horizontal dl-params

  ``limit``
      *optional* integer. Defaults to ``10``.

  ``offset``
      *optional* integer. Defaults to ``0``.

.. container:: code-white

  .. dcode:: scenario debit_list


.. cssclass:: method-section

List All Debits For a Customer
------------------------------

Returns a list of debits you've previously created against a specific account.
The ``debits_uri`` is a convenient uri provided so that you can simply issue
a ``GET`` to the ``debits_uri``. The debits are returned in sorted order,
with the most recent debits appearing first.

.. cssclass:: dl-horizontal dl-params

  ``limit``
      *optional* integer. Defaults to ``10``.

  ``offset``
      *optional* integer. Defaults to ``0``.

.. container:: code-white

  .. dcode:: scenario debit_customer_list


.. cssclass:: method-section

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


.. cssclass:: method-section

Refund a Debit
--------------

Issues a refund for a particular debit. This creates a :ref:`refund <refunds>`.

.. container:: method-description

   Use the ``refund_uri`` on a :ref:`debit object <debits>`.

.. container:: code-white

   .. dcode:: scenario debit_refund


.. _info on ACH debits: http://github.com/balanced/balanced-api/issues/2
