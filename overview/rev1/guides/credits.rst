.. _guides.credits:

Credits
=====================

A credit (payout) is a transaction where funds are sent to a bank account with
ACH direct deposit. Funds are deposited the next business day for U.S.
bank accounts and the same business day for Wells Fargo accounts.

Credits have a ``status`` attribute representing the current status of the credit
throughout the payout process. There are three possible ``status`` values:
``pending``, ``succeeded``, ``failed``


Balanced currently supports payouts to:

- \- Bank accounts via ACH
- \- Debit cards

|

Create a credit
----------------------

.. admonition:: References
  :header_class: alert alert-tab full-width alert-tab-persianBlue60
  :body_class: alert alert-green alert-persianBlue20
  
  .. cssclass:: mini-header
  
    API

  .. cssclass:: list-noindent

    - `Create a Credit to a Bank Account </1.1/api/credits/#create-a-credit-to-a-bank-account>`_
    - `Create a Credit to a Card </1.1/api/credits/#create-a-credit-to-a-card>`_

|

.. note::
  :header_class: alert alert-tab alert-tab-pineGreen80
  :body_class: alert alert-green alert-pineGreen20
  
  Credits may also be initiated via the `Dashboard`_.

|

Create a credit to a bank account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Initiating a credit (payout) to a bank account is simple. Assuming we have an existing ``BankAccount`` we can
do the following:

.. literalinclude:: examples/curl/credit-create.sh
   :language: bash

.. literalinclude:: examples/python/credit-create.py
   :language: python

.. literalinclude:: examples/ruby/credit-create.rb
   :language: ruby

.. literalinclude:: examples/php/credit-create.php
   :language: php

.. literalinclude:: examples/java/credit-create.java
   :language: java

.. literalinclude:: examples/node/credit-create.js
   :language: node

.. literalinclude:: examples/csharp/credit-create.cs
   :language: csharp


Create a credit to a Card
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Initiating a credit (payout) to a card is simple, but there are a few requirements to be aware of.

.. admonition:: Requirements
  :header_class: alert alert-tab full-width alert-tab-yellow
  :body_class: alert alert-green alert-yellow

  .. cssclass:: list-noindent no-border

    - ``name`` must have been supplied on card tokenization.
    - ``card_type`` must be ``debit``
    - ``card_category`` cannot be ``prepaid``. Pre-paid cards are not supported.

  The maximum amount per transaction is $2,500.

|

Assuming we have an existing and creditable ``Card`` we can do the following:

.. literalinclude:: examples/curl/card-credit.sh
   :language: bash

.. literalinclude:: examples/python/card-credit.py
   :language: python

.. literalinclude:: examples/ruby/card-credit.rb
   :language: ruby

.. literalinclude:: examples/php/card-credit.php
   :language: php

.. literalinclude:: examples/java/card-credit.java
   :language: java

.. literalinclude:: examples/node/card-credit.js
   :language: node

.. literalinclude:: examples/csharp/card-credit.cs
   :language: csharp


Statement descriptor
--------------------------

Balanced allows marketplaces to specify the text that appears on statements for
a transaction. This is referred to as the soft descriptor and is set by
specifying the ``appears_on_statement_as`` field when creating a credit.


.. admonition:: Requirements
  :header_class: alert alert-tab full-width alert-tab-yellow
  :body_class: alert alert-green alert-yellow

  Characters that can be used are limited to the following (any other characters
  will be rejected):

  .. cssclass:: no-border

    - \- ASCII letters (a-z and A-Z)
    - \- Digits (0-9)
    - \- Special characters (``.<>(){}[]+&!$;-%_?:#@~='"^\`|``)

  Descriptor length limit:

  .. cssclass:: no-border

    - \- ACH credits: 14 characters. ACH credits do not have a prefix.
    - \- Card credits: 12 characters.


Example usage:

.. literalinclude:: examples/curl/credit-soft-descriptor.sh
   :language: bash

.. literalinclude:: examples/python/credit-soft-descriptor.py
   :language: python

.. literalinclude:: examples/ruby/credit-soft-descriptor.rb
   :language: ruby

.. literalinclude:: examples/php/credit-soft-descriptor.php
   :language: php

.. literalinclude:: examples/java/credit-soft-descriptor.java
   :language: java

.. literalinclude:: examples/node/credit-soft-descriptor.js
   :language: node

.. literalinclude:: examples/csharp/credit-soft-descriptor.cs
   :language: csharp


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

.. admonition:: References
  :header_class: alert alert-tab full-width alert-tab-persianBlue60
  :body_class: alert alert-green alert-persianBlue20
  
  .. cssclass:: mini-header
  
    API
  
  .. cssclass:: list-noindent

    - `Create a Reversal </1.1/api/reversals/#create-a-reversal>`_


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

.. literalinclude:: examples/java/reversal-create.java
   :language: java

.. literalinclude:: examples/node/reversal-create.js
   :language: node

.. literalinclude:: examples/csharp/reversal-create.cs
   :language: csharp


The status flow of a reversal is as follows:

.. image:: https://www.balancedpayments.com/images/payouts/payouts_reversal_status-2x-83ac62b3.png

|

.. note::
  :header_class: alert alert-tab
  :body_class: alert alert-green
  
  Credits may also be reversed from the `Dashboard`_.



.. _Dashboard: https://dashboard.balancedpayments.com/