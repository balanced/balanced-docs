.. _resources:

Resources
=========

Client Libraries
----------------

Balanced attempts very hard to write idiomatic code for all it's API libraries
and we pride ourselves in an extensive test suite for every client that
demonstrates almost every single method / function executed for your
convenience.

We find that this is the best way to use the client libraries. If you encounter
and issue, please file a github issue and get in touch through one our
many :ref:`support channels <overview.support>`.

.. list-table::
   :widths: 15 17 18 15
   :header-rows: 1
   :class: table table-hover

   * - Language / Platform
     - Repository
     - Tests
     - Primary Contributor
   * - python
     - `balanced-python`_
     - `balanced-python tests`_
     - Balanced
   * - ruby
     - `balanced-ruby`_
     - `balanced-ruby tests`_
     - Balanced
   * - php
     - `balanced-php`_
     - `balanced-php tests`_
     - Balanced
   * - php (symfony2 bundle)
     - `JmBalancedPaymentBundle <https://github.com/jeremymarc/JmBalancedPaymentBundle>`_
     - `JmBalancedPaymentBundle Tests <https://github.com/jeremymarc/JmBalancedPaymentBundle/tree/master/Tests>`_
     - `Jeremy Marc <https://twitter.com/jeremymarc>`_
   * - java
     - `balanced-java`_
     - `balanced-java tests`_
     - Balanced
   * - iOS
     - `balanced-ios`_
     - `balanced-ios tests`_
     - `Ben Mills (Remear)`_
   * - perl
     - `Business-BalancedPayments`_
     - `Business-BalancedPayments tests`_
     - `Crowdtilt.com`_
..   * - node
     - `balanced-node`_
     - `balanced-node tests`_
     - Balanced


.. _balanced-php: https://github.com/balanced/balanced-php
.. _balanced-php tests: https://github.com/balanced/balanced-php/tree/master/tests

.. _balanced-python: https://github.com/balanced/balanced-python
.. _balanced-python tests: https://github.com/balanced/balanced-python/tree/master/tests

.. _balanced-ruby: https://github.com/balanced/balanced-ruby
.. _balanced-ruby tests: https://github.com/balanced/balanced-ruby/tree/master/spec

.. _balanced-java: https://github.com/balanced/balanced-java
.. _balanced-java tests: https://github.com/balanced/balanced-java/tree/master/src/test

.. _balanced-node: https://github.com/balanced/balanced-node
.. _balanced-node tests: https://github.com/balanced/balanced-node/tree/master/test


.. _Business-BalancedPayments: https://github.com/Crowdtilt/Business-BalancedPayments
.. _Business-BalancedPayments tests: https://github.com/Crowdtilt/Business-BalancedPayments/tree/master/t

.. _balanced-ios: https://github.com/balanced/balanced-ios
.. _balanced-ios tests: https://github.com/balanced/balanced-ios/tree/master/BalancedTests


.. _Ben Mills (Remear): http://unfiniti.com


.. _resources.request-logs:

Request Logs
------------

As you integrate and test :ref:`payouts`, you may find it useful to view
all your sanitized API request logs. They are viewable via the logs section
in the `dashboard`_

.. _dashboard: https://dashboard.balancedpayments.com/

.. SUBHEADERS
   glossary / terms
   client library reference
   api reference
   balanced.js
   testing


The Hash Attribute
------------------

Every ``Card`` and ``BankAccount`` resource has an attribute than can be used
to check if the same card is being added again.

For credit cards, this is the ``hash`` attribute. This is calculated using
``card_number`` and the expiration.

For bank accounts, this is the ``fingerprint`` attribute. This is calculated using
``account_number``, ``routing_number``, ``name``, and ``type``.


.. _resources.address-verification-service:

Address Verification Service
----------------------------

AVS, **A**\ ddress **V**\ erification **S**\ ervice, provides a means to
verify that the postal_code supplied during card tokenization matches the
billing zip code of the credit card.

Supplying a ``postal_code`` during tokenization initiates the AVS check.
The ``Card`` will have a ``postal_code_check`` attribute containing the
AVS check result.

``postal_code_check`` will be one of: ``passed``, ``failed``, ``unknown``


.. _resources.card-security-code:

Card Security Code
------------------

CSC, **C**\ ard **S**\ ecurity **C**\ ode, provides a means to verify that the
``security_code`` supplied during card tokenization matches the security_code
for the credit card. The ``Card`` will have a ``security_code_check``
attribute containing the CSC check result. It's strongly recommended you do
not process transactions with cards that fail this check.

``security_code_check`` will be one of: ``passed``, ``failed``, ``unknown``


.. _FedACH directory: https://www.fededirectory.frb.org

Certified Developers
--------------------

We've partnered with `APIXchange`_ -- a marketplace for custom API development
projects -- to help companies looking for assistance with their Balanced API
integration find a quality Balanced certified developer.

Create a project on `APIXchange`_ to get started:

.. image:: https://apixchange.com/static/img/embed-button.png
  :target: https://apixchange.com/landing/balanced

If you'd like to find a developer to help with your Balanced integration
outside of APIXchange, please post your criteria on `this Github issue`_.

.. _this Github issue: https://github.com/balanced/balanced-api/issues/315
.. _APIXchange: https://apixchange.com/
