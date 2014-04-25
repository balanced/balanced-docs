.. _guides.credits:

Working with Credits
=====================

A credit (payout) is a transaction where funds are sent to a bank account with
ACH direct deposit. Funds are deposited the next business day for U.S.
bank accounts and the same business day for Wells Fargo accounts.

Credits have a ``status`` attribute representing the current status of the credit
throughout the payout process. There are three possible ``status`` values:
``pending``, ``succeeded``, ``failed``

|

Payout methods
--------------

Currently Balanced only supports payouts to bank accounts via ACH but we will
add more. All of this is publicly tracked via Github issues. For example:

.. cssclass:: list-noindent

* `Payouts via Check <https://github.com/balanced/balanced-api/issues/69>`_
* `Pushing to Cards <https://github.com/balanced/balanced-api/issues/32>`_

Feel free to chime in on an existing issue or create a new one if you'd like
to see another payment method supported.


Initiating a credit
--------------------

|

API References:

.. cssclass:: list-noindent

- `Create a Credit </1.1/api/credits/#create-a-credit>`_

|

Initiating a credit (payout) is simple. Assuming we have an existing ``BankAccount`` we can
do the following:

.. literalinclude:: examples/curl/credit-create.sh
   :language: bash

.. literalinclude:: examples/python/credit-create.py
   :language: python

.. literalinclude:: examples/ruby/credit-create.rb
   :language: ruby

.. literalinclude:: examples/php/credit-create.php
   :language: php


.. note::
  :header_class: alert alert-tab
  :body_class: alert alert-green
  
  Credits may also be initiated via the `Dashboard`_.


Bank statement descriptor
--------------------------

Balanced allows marketplaces to specify the text that appears on statements for
a transaction. This is referred to as the soft descriptor and is set by
specifying the ``appears_on_statement_as`` field when creating a credit.

Characters that can be used are limited to the following (any other characters
will be rejected):

.. cssclass:: list-noindent

- \- ASCII letters (a-z and A-Z)
- \- Digits (0-9)
- \- Special characters (``.<>(){}[]+&!$;-%_?:#@~='"^\`|``)

The descriptor is limited to 14 characters. ACH credits do not have a prefix.

Example usage:

.. literalinclude:: examples/curl/credit-soft-descriptor.sh
   :language: bash

.. literalinclude:: examples/python/credit-soft-descriptor.py
   :language: python

.. literalinclude:: examples/ruby/credit-soft-descriptor.rb
   :language: ruby

.. literalinclude:: examples/php/credit-soft-descriptor.php
   :language: php


Payout status flow
-------------------

Credits have a ``status`` attribute representing the current status of the credit
throughout the payout process. There are three possible ``status`` values:

.. cssclass:: dl-horizontal dl-params dl-param-values dd-noindent dd-marginbottom

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

.. image:: https://www.balancedpayments.com/images/payouts/payouts_status-2x-30c2fcdc.png


Reversing a credit
-------------------

|

API References:

.. cssclass:: list-noindent

- `Create a Reversal </1.1/api/reversals/#create-a-reversal>`_

|

In the event that you need to cancel a payout, e.g. a user is not
satisfied with the product, you can create a ``Reversal``.

.. literalinclude:: examples/curl/reversal-create.sh
   :language: bash

.. literalinclude:: examples/python/reversal-create.py
   :language: python

.. literalinclude:: examples/ruby/reversal-create.rb
   :language: ruby

.. literalinclude:: examples/php/reversal-create.php
   :language: php

  

The status flow of a reversal is as follows:

.. image:: https://www.balancedpayments.com/images/payouts/payouts_reversal_status-2x-83ac62b3.png

|

.. note::
  :header_class: alert alert-tab
  :body_class: alert alert-green
  
  Credits may also be reversed from the `Dashboard`_.



.. _Dashboard: https://dashboard.balancedpayments.com/