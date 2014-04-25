.. _guides.disputes:

Disputes
==========

A dispute, otherwise known as a chargeback, is the result of a customer protesting
a charge made on their credit card. A customer contacts their card provider and states
they did not authorize the transaction, which results in a dispute.

Fortunately, a marketplace may challenge the dispute by providing evidence of a legitimate
transaction.

|


Common causes of disputes
---------------------------

Not all disputes are intentional. Chargebacks are often the result of a customer seeing
a charge that they don’t recognize or don’t remember on their credit card statement.

Some helpful tips to prevent chargebacks:

.. cssclass:: list-noindent

  - \- Use an easily identifiable statement descriptor by setting ``appears_on_statement_as``
  - \- Set expectations regarding shipping times for physical goods and contact your customers right away if you’re alerted to any delays
  - \- Clearly state refund policies on your website
  - \- Make it very easy for customers to contact you, and respond in a timely fashion


Dispute fees
---------------
There is a non-refundable $15 fee for each chargeback regardless of the outcome of the dispute.


Challenging a Dispute
----------------------
Once you receive notification of a chargeback it’s important to reach out directly to
the customer and find out why they are initiating the dispute. Often times customers
will forget making a particular charge and contest it. In this case, reaching out to
the customer will remind them of the charge, and call their card provider to cancel
the chargeback.

.. note::
  :header_class: alert alert-tab-yellow
  :body_class: alert alert-yellow
  
  The $15 dispute fee will still be assessed even if the customer cancels the dispute.


Unfortunately, not all disputes are as easily resolved. If you are unable to reach a
customer, or they are not being cooperative, the next steps are to gather as much
documentation as possible to demonstrate fulfillment of the transaction and send it
to support@balancedpayments.com. Balanced will use the supplied documentation to
fight the dispute on your behalf directly with the credit card provider. The
following types of documentation can help you win a chargeback:

.. cssclass:: list-noindent

  - \- Tracking information for goods that are physically delivered, such as a Fedex/UPS tracking number, etc.
  - \- A PDF of any email exchanges between yourself and the customer where you remind them of the initial charge
  - \- Receipts of purchase emailed to the cardholder upon completion of the purchase process

This information may be provided only in the following formats:

.. cssclass:: list-noindent

  - \- pdf
  - \- docx
  - \- jpg

Even if a customer agrees to cancel the chargeback themself, Balanced recommends
submitting documentation of transaction fulfillment so the dispute is contested
on your behalf so you’re protected in the event the customer forgets to cancel
the dispute!

Once documentation has been submitted, Balanced will fight the chargeback on your
behalf. The card provider will decide to either rule in favor of the marketplace
or the customer, which status will be indicated by a transition from a value of
``pending`` to one of ``won`` or ``lost``. 


Dispute Notifications
-------------------------





Viewing Disputes
---------------------

In production marketplaces, disputes will



Testing Disputes
------------------

In test marketplaces, creating a ``Card`` with the number ``6500000000000002``, will create a dispute for
any debit created with the card.


.. container:: section-ruby

  .. literalinclude:: examples/ruby/card-create-dispute.rb
    :language: ruby

.. container:: section-python

  .. literalinclude:: examples/python/card-create-dispute.py
    :language: python

.. container:: section-bash

  .. literalinclude:: examples/curl/card-create-dispute.sh
     :language: bash

.. container:: section-php

  .. literalinclude:: examples/php/card-create-dispute.php
    :language: php

.. container:: section-java

  .. literalinclude:: examples/java/card-create-dispute.java
    :language: java

.. container:: section-node

  .. literalinclude:: examples/node/card-create-dispute.js
    :language: javascript


Now debit the card.


.. container:: section-ruby

  .. literalinclude:: examples/ruby/card-debit.rb
    :language: ruby

.. container:: section-python

  .. literalinclude:: examples/python/card-debit.py
    :language: python

.. container:: section-bash

  .. literalinclude:: examples/curl/card-debit.sh
     :language: bash

.. container:: section-php

  .. literalinclude:: examples/php/card-debit.php
    :language: php

.. container:: section-java

  .. literalinclude:: examples/java/card-debit.java
    :language: java

.. container:: section-node

  .. literalinclude:: examples/node/card-debit.js
    :language: javascript


After some time has passed, a dispute will be associated to the ``Debit``.
The dispute may be retrieved in several ways.

Retrieve via the ``Debit``:

.. container:: section-ruby

  .. literalinclude:: examples/ruby/dispute-list.rb
    :language: ruby

.. container:: section-python

  .. literalinclude:: examples/python/dispute-list.py
    :language: python

.. container:: section-bash

  .. literalinclude:: examples/curl/dispute-list.sh
     :language: bash

.. container:: section-php

  .. literalinclude:: examples/php/dispute-list.php
    :language: php

.. container:: section-java

  .. literalinclude:: examples/java/dispute-list.java
    :language: java

.. container:: section-node

  .. literalinclude:: examples/node/dispute-list.js
    :language: javascript


Retrieve by href:

.. container:: section-ruby

  .. literalinclude:: examples/ruby/dispute-show.rb
    :language: ruby

.. container:: section-python

  .. literalinclude:: examples/python/dispute-show.py
    :language: python

.. container:: section-bash

  .. literalinclude:: examples/curl/dispute-show.sh
     :language: bash

.. container:: section-php

  .. literalinclude:: examples/php/dispute-show.php
    :language: php

.. container:: section-java

  .. literalinclude:: examples/java/dispute-show.java
    :language: java

.. container:: section-node

  .. literalinclude:: examples/node/dispute-show.js
    :language: javascript


You may also list all disputes:

.. container:: section-ruby

  .. literalinclude:: examples/ruby/dispute-list.rb
    :language: ruby

.. container:: section-python

  .. literalinclude:: examples/python/dispute-list.py
    :language: python

.. container:: section-bash

  .. literalinclude:: examples/curl/dispute-list.sh
     :language: bash

.. container:: section-php

  .. literalinclude:: examples/php/dispute-list.php
    :language: php

.. container:: section-java

  .. literalinclude:: examples/java/dispute-list.java
    :language: java

.. container:: section-node

  .. literalinclude:: examples/node/dispute-list.js
    :language: javascript






.. _Dashboard: https://dashboard.balancedpayments.com/

