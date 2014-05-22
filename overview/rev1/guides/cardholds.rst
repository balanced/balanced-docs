Card Holds
========================

Balanced supports the concepts of :term:`holds`. Holds are a type of
authorization that reserves a dollar amount on a credit card to be captured at
a later time, usually within 7 days. If the transaction is not processed
(known as post-authorization) by the end of the hold period, the amount is
released back to the available credit on the cardholder's credit card.
**The customer is not charged.**

Holds are common in the industries where the amount of the goods or services
are "reserved" on the cardholder's credit card or.

If you issue a debit on an account, Balanced uses holds behinds the scenes
but captures the funds immediately -- you will
**always see an expanded hold resource returned on a debit representation**.

.. warning::
  :header_class: alert alert-tab alert-tab-yellow
  :body_class: alert alert-yellow

  For all intents and purposes, Balanced does not recommend holds and considers
  their usage to be a very advanced feature as they cause much confusion and are
  cumbersome to manage.

  If your project requires holds and you need help, please reach out
  to us using our :ref:`support channels <overview.support>`.

|

Creating a card hold
--------------------

.. admonition:: References
  :header_class: alert alert-tab full-width alert-tab-persianBlue60
  :body_class: alert alert-green alert-persianBlue20
  
  .. cssclass:: mini-header
  
    API

  .. cssclass:: list-noindent

    - `Create a Card Hold </1.1/api/card-holds/#create-a-card-hold>`_


A hold is created in a way similar to creating a debit. Creating a card hold
will return a href which can be used to perform a capture later, up to the full
amount of the card hold.

.. literalinclude:: examples/curl/card-hold-create.sh
   :language: bash

.. literalinclude:: examples/python/card-hold-create.py
   :language: python

.. literalinclude:: examples/ruby/card-hold-create.rb
   :language: ruby

.. literalinclude:: examples/php/card-hold-create.php
   :language: php

.. literalinclude:: examples/java/card-hold-create.java
   :language: java

.. literalinclude:: examples/node/card-hold-create.js
   :language: node


Capturing a card hold
---------------------

.. admonition:: References
  :header_class: alert alert-tab full-width alert-tab-persianBlue60
  :body_class: alert alert-green alert-persianBlue20
  
  .. cssclass:: mini-header
  
    API

  .. cssclass:: list-noindent

    - `Capture a Card Hold </1.1/api/card-holds/#capture-a-card-hold>`_


When you wish to obtain the funds reserved with a card hold, capture the card
hold.

.. literalinclude:: examples/curl/card-hold-capture.sh
   :language: bash

.. literalinclude:: examples/python/card-hold-capture.py
   :language: python

.. literalinclude:: examples/ruby/card-hold-capture.rb
   :language: ruby

.. literalinclude:: examples/php/card-hold-capture.php
   :language: php

.. literalinclude:: examples/java/card-hold-capture.java
   :language: java

.. literalinclude:: examples/node/card-hold-capture.js
   :language: node


Voiding a card hold
---------------------

.. admonition:: References
  :header_class: alert alert-tab full-width alert-tab-persianBlue60
  :body_class: alert alert-green alert-persianBlue20
  
  .. cssclass:: mini-header
  
    API

  .. cssclass:: list-noindent

    - `Void a Card Hold </1.1/api/card-holds/#void-a-card-hold>`_


If you wish to release the reserved funds you can always void the card hold.

.. literalinclude:: examples/curl/card-hold-void.sh
   :language: bash

.. literalinclude:: examples/python/card-hold-void.py
   :language: python

.. literalinclude:: examples/ruby/card-hold-void.rb
   :language: ruby

.. literalinclude:: examples/php/card-hold-void.php
   :language: php

.. literalinclude:: examples/java/card-hold-void.java
   :language: java

.. literalinclude:: examples/node/card-hold-void.js
   :language: node



.. _sample page: https://gist.github.com/2662770
.. _balanced.js: https://js.balancedpayments.com/v1/balanced.js
.. _testing documentation: /docs/testing#simulating-card-failures
.. _jQuery: http://www.jquery.com