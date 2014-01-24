Credits
=======

A ``Credit`` resource represents a transaction consisting
of sending money to a bank account.

Credits have a ``status`` attribute representing the current status of the credit
throughout the payout process. There are three possible ``status`` values:

.. cssclass:: dd-noindent dd-marginbottom

  ``pending``
    As soon as the credit is created through the API, the status shows
    as ``pending``. This indicates that Balanced received the information for the
    credit and will begin processing. The ACH network itself processes transactions
    in a batch format. Batch submissions are processed at 3pm PST on business days.
    If the credit is created after 3pm PST, it will not be submitted for processing
    until **3pm PST** the next business day.
  ``succeeded``
    One business day after the batch submission, the status will change to
    ``succeeded``. That is the *expected* status of the credit. If the account
    number and routing number were entered correctly, the money should in fact
    be available to the seller. However, there is no immediate confirmation
    regarding the transaction showing up in the seller's account successfully.
  ``failed``
    The seller's bank has up to three business days from when the money *should*
    be available to indicate a rejection along with the rejection reason.
    Unfortunately, not all banks comply with ACH network policies and may respond
    after three business days with a rejection. As soon as Balanced receives the
    rejection, the status is updated to ``failed``.

|

**NOTE** If you're sending money to a bank account, known as issuing a credit,
you do **NOT** need to verify the bank account

.. cssclass:: method-section

Credit a New Bank Account
-------------------------

To credit a new bank account, you simply pass the amount along with the bank
account details. We do not store this bank account when you create a credit
this way, so you can safely assume that the information has been deleted.

.. cssclass:: dl-horizontal dl-params

    .. dcode:: form credits.create
       :exclude: bank_account.0.bank_code bank_account.1

.. container:: code-white

  .. dcode:: scenario credit_create_new_bank_account

.. cssclass:: method-section

Credit An Existing Bank Account
-------------------------------

To credit an existing bank account, you simply pass the amount to the
nested credit endpoint of a bank account. The ``credits_uri`` is a convenient
uri provided so that you can simply issue a ``POST`` with the amount and a
credit shall be created.


.. cssclass:: dl-horizontal dl-params

    .. dcode:: form bank_account_credits.create

.. container:: code-white

  .. dcode:: scenario credit_create_existing_bank_account


.. cssclass:: method-section

Retrieve a Credit
-----------------

Retrieves the details of a credit that you've previously created. Use the
``uri`` that was previously returned, and the corresponding credit
information will be returned.

.. container:: method-description

  .. no request

.. container:: code-white

  .. dcode:: scenario credit_show


.. cssclass:: method-section

List All Credits
----------------

Returns a list of credits you've previously created. The credits are returned
in sorted order, with the most recent credits appearing first.

.. cssclass:: dl-horizontal dl-params

  ``limit``
      *optional* integer. Defaults to ``10``.

  ``offset``
      *optional* integer. Defaults to ``0``.

.. container:: code-white

  .. dcode:: scenario credit_list


.. cssclass:: method-section

List All Credits For a Bank Account
-----------------------------------

Returns a list of credits you've previously created to a specific bank account.
The ``credits_uri`` is a convenient uri provided so that you can simply issue
a ``GET`` to the ``credits_uri``. The credits are returned in sorted order,
with the most recent credits appearing first.

.. cssclass:: dl-horizontal dl-params

  ``limit``
      *optional* integer. Defaults to ``10``.

  ``offset``
      *optional* integer. Defaults to ``0``.

.. container:: code-white

  .. dcode:: scenario credit_bank_account_list


.. cssclass:: method-section

Create a New Credit For a Customer
------------------------------------

.. cssclass:: dl-horizontal dl-params

  .. dcode:: form credits.create

.. container:: code-white

  .. dcode:: scenario customer_credit


.. cssclass:: method-section

Listing All Credits For a Customer
----------------------------------

.. cssclass:: dl-horizontal dl-params

  ``limit``
      *optional* integer. Defaults to ``10``.

  ``offset``
      *optional* integer. Defaults to ``0``.

.. container:: code-white

  .. dcode:: scenario credit_customer_list
