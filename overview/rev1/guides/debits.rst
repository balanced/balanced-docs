.. _guides.debits:

Debits
=======================

A debit is a transaction where funds are obtained from a credit card or from a
bank account via the ACH Network. Funds obtained via credit card debits are
immediately available in escrow. Funds being obtained via ACH debits are
generally available in escrow in 3-4 business days. Currently Balanced supports
credit card debits as well as bank accounts debits via ACH.

Debits have a ``status`` attribute representing the current status of the debit
throughout the payout process. There are three possible ``status`` values:
``pending``, ``succeeded``, ``failed``

|

Creating a debit
--------------------

.. admonition:: References
  :header_class: alert alert-tab full-width alert-tab-persianBlue60
  :body_class: alert alert-green alert-persianBlue20
  
  .. cssclass:: mini-header
  
    API

  .. cssclass:: list-noindent

    - `Create a Card Debit </1.1/api/debits/#create-a-card-debit>`_
    - `Create a Bank Account Debit </1.1/api/debits/#create-a-bank-account-debit>`_
    - `Create a Bank Account Verification </1.1/api/bank-account-verifications/#create-a-bank-account-verification>`_


Debit a credit card
~~~~~~~~~~~~~~~~~~~~~

Assuming we have an existing ``Card`` we can do the following:

.. literalinclude:: examples/curl/card-debit.sh
   :language: bash

.. literalinclude:: examples/python/card-debit.py
   :language: python

.. literalinclude:: examples/ruby/card-debit.rb
   :language: ruby

.. literalinclude:: examples/php/card-debit.php
   :language: php

.. literalinclude:: examples/java/card-debit.java
   :language: java

.. literalinclude:: examples/node/card-debit.js
   :language: node


Debit a bank account
~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Requirements
  :header_class: alert alert-tab full-width alert-tab-yellow
  :body_class: alert alert-green alert-yellow
  
  Bank accounts you wish to debit must first `be verified`_.


Assuming we have an existing ``BankAccount`` we can do the following:

.. literalinclude:: examples/curl/bank-account-debit.sh
   :language: bash

.. literalinclude:: examples/python/bank-account-debit.py
   :language: python

.. literalinclude:: examples/ruby/bank-account-debit.rb
   :language: ruby

.. literalinclude:: examples/php/bank-account-debit.php
   :language: php

.. literalinclude:: examples/java/bank-account-debit.java
   :language: java

.. literalinclude:: examples/node/bank-account-debit.js
   :language: node


ACH Debit status flow
---------------------

Debits have a ``status`` attribute representing the current status of the debit
throughout the payout process. There are three possible ``status`` values:

.. cssclass:: dl-horizontal dl-params dl-param-values dd-noindent dd-marginbottom

  ``pending``
    As soon as the debit is created through the API, the status shows
    as ``pending``. This indicates that Balanced received the information for the
    debit and will begin processing. The ACH network itself processes transactions
    in a batch format. Batch submissions are processed at 3pm PST on business days.
    If the debit is created after 3pm PST, it will not be submitted for processing
    until **3pm PST** the next business day.
  ``succeeded``
    After 3-4 days, the status will change to ``succeeded`` and the funds will be
    available in escrow. Note, even after a succeeded status, the status may still
    transition to failed even after a few weeks.
  ``failed``
    After 3-4 days, the status will change to ``failed`` if the transaction was
    not successful due to a problem such as an incorrect bank account number
    or insufficient funds.

.. note::
  :header_class: alert alert-tab-yellow
  :body_class: alert alert-yellow

  After a succeeded status, the status may still transition to failed, even
  after a few weeks.

|

.. image:: https://www.balancedpayments.com/images/ach-debits/ach_debits_payment_status-01-2x-882f3b99.png

|


Refunding a debit
-------------------

A ``Refund`` resource represents a refund of a ``Debit`` transaction. The
amount of the refund may be any value up to the amount of the original
``Debit``. Refunds generally process in one day or less.


.. admonition:: References
  :header_class: alert alert-tab full-width alert-tab-persianBlue60
  :body_class: alert alert-green alert-persianBlue20
  
  .. cssclass:: mini-header
  
    API

  .. cssclass:: list-noindent

    - `Create a Refund </1.1/api/refunds/#create-a-refund>`_


In the event that you need to cancel a payout, e.g. a user is not satisfied with
the product, you can create a ``Refund``.


.. literalinclude:: examples/curl/refund-create.sh
   :language: bash

.. literalinclude:: examples/python/refund-create.py
   :language: python

.. literalinclude:: examples/ruby/refund-create.rb
   :language: ruby

.. literalinclude:: examples/php/refund-create.php
   :language: php

.. literalinclude:: examples/java/refund-create.java
   :language: java

.. literalinclude:: examples/node/refund-create.js
   :language: node


.. note::
  :header_class: alert alert-tab
  :body_class: alert alert-green

  A Debit may also be refunded from the `Dashboard`_.


.. _be verified: /1.1/api/bank-account-verifications
.. _Dashboard: https://dashboard.balancedpayments.com/