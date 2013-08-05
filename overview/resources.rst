.. _resources:

Resources
=========

.. _resources.client_libraries:

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
   :widths: 10 20 20 15
   :header-rows: 1
   :class: table table-hover

   * - Language
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
   * - node
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

.. _Crowdtilt.com:
.. _crowdtilt: http://crowdtilt.com



.. _resources.test_credit_cards:

Test credit card numbers
------------------------

These cards will be accepted in our system only for a **TEST** marketplace.

.. cssclass:: table table-hover

  ============== =========================== ================ ==============================
   Card Brand          Number                  Security Code     Result
  ============== =========================== ================ ==============================
  ``VISA``        ``4111111111111111``            ``123``       SUCCESS
  ``MasterCard``  ``5105105105105100``            ``123``       SUCCESS
  ``AMEX``         ``341111111111111``           ``1234``       SUCCESS
  ``VISA``        ``4444444444444448`` [#]_       ``123``       SIMULATE PROCESSOR FAILURE
  ``VISA``        ``4222222222222220`` [#]_       ``123``       SIMULATE TOKENIZATION ERROR
  ============== =========================== ================ ==============================

.. [#] Simulate a card which can be tokenized but will not be accepted for creating
       holds or debits. This type of failure is what you would expect if you try to
       create a hold on a card with insufficient funds.
.. [#] To simulate a card which cannot be tokenized but passes a LUHN check. You could
       expect this failure when a user tried to enter in a credit card which used to
       work but has been canceled.

.. _resources.test_bank_accounts:

Test bank account numbers
-------------------------

Balanced provides various utilities to aid you in testing your :ref:`payouts`
integration.

When integrating payouts, it's worth noting that incorrect bank routing numbers
are a very commonly encountered error as Balanced does real-time checks against
the `FedACH directory`_.

To aid you while integrating, Balanced provides special routing and
account numbers that can simulate various scenarios that can go wrong.

.. list-table::
   :widths: 15 20 40
   :header-rows: 1
   :class: table table-hover

   * - Routing Number
     - Account Number
     - Scenario
   * - ``100000007``
     - ``8887776665555``
     - Invalid Routing Number
   * - ``111111118``
     - ``8887776665555``
     - Invalid Routing Number
   * - ``021000021``
     - ``9900000000``
     - Transitions credit state to ``pending``
   * - ``321174851``
     - ``9900000001``
     - Transitions credit state to ``pending``
   * - ``021000021``
     - ``9900000002``
     - Transitions credit state to ``paid``
   * - ``321174851``
     - ``9900000003``
     - Transitions credit state to ``paid``
   * - ``021000021``
     - ``9900000004``
     - Transitions credit state to ``failed``
   * - ``321174851``
     - ``9900000005``
     - Transitions credit state to ``failed``

simulating erroneous routing numbers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. dcode:: scenario bank-account-invalid-routing-number

simulating pending status
~~~~~~~~~~~~~~~~~~~~~~~~~

.. dcode:: scenario credit_pending_state

simulating paid status
~~~~~~~~~~~~~~~~~~~~~~

.. dcode:: scenario credit_paid_state

simulating failed status
~~~~~~~~~~~~~~~~~~~~~~~~

.. dcode:: scenario credit_failed_state


Test identity verification
-----------------------------------

``Customer`` resources have an ``is_identity_verified`` attribute.

Omit address data to trigger a ``false`` response. Supply address data
to trigger a ``true`` response.

The following will set ``is_identity_verified`` to ``true``

.. code-block:: javascript

  {
      'name': 'Henry Ford',
      'dob': '1863-07',
      'address': {
          'postal_code': '48120'
      }
  }


The following will set ``is_identity_verified`` to ``false``

.. code-block:: javascript

  {
      'name': 'Henry Ford',
      'dob': '1863-07'
  }


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

.. _uri_vs_id:

Storing the URI vs ID
---------------------

Do you store the ``uri`` or the ``id`` in your database? \ **Always, always
store the uri**.

The ``uri`` stands for **u**\ niversal **r**\ esource **i**\ dentifier and it's
exactly what it is. An identifier.

Do not attempt to be clever and try to save a few bytes by storing the ``id``
and constructing the ``uri`` later.

This will almost always lead to disaster. A ``uri`` is opaque and Balanced
reserves the right to use HTTP semantics later to change them, so you
should **NEVER** store the ``id``.

Fun fact: our internal statistics show that client libraries that construct
the ``uri`` receive roughly 2 orders of magnitude more ``404`` status codes
from Balanced than clients which use the ``uri`` directly.


.. SUBHEADERS
   couponing
   mobile checkout
   guest checkout
   recurring
   group buying
   shopping cart
   accounting

.. _resources.best_practices:

Best Practices
--------------

.. _resources.best_practices.payouts:

Payouts Best Practices
~~~~~~~~~~~~~~~~~~~~~~~

Automated Clearing House transactions are asynchronous, requiring upfront effort
in educating your consumers and setting the appropriate expectations to deliver
a great product.

There are a few simple best practices that can dramatically increase user
convenience, allowing for a much more enjoyable experience and minimizing
problematic encounters.


Sending a payout for the first time
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There’s a very small chance the first payout to a customer can fail. This is
usually due to the customer accidentally providing an incorrect bank account
number.

Balanced validates bank routing numbers in real-time using the
`FedACH directory`_, but since bank accounts are not standardized, incorrect
bank account numbers are not caught until the payout fails and Balanced
is notified (3) three to (5) five business days after submission!

Our statistics show that most of the time, your users will provide the correct
bank routing and account numbers with the help of a properly designed and robust
form. Their payout will appear the next business day, as expected. Once a
successful payout has been made, future credits to that bank account
will continue to take one business day when issued before the
:ref:`next-day cut-offs <payouts.cutoff>`.

However, if a payout fails, we’ll notify you via email, dashboard, and webhook.

Help your users avoid mistakes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Due to the nature of the ACH network, failure notifications can be delayed
for up to (4) four business days! This can be extremely inconvenient and
frustrating to your users and your business, since some merchants rely on
speedy ACH payments for operating capital.

For example, an account number typo can, on average, cause payment delays by
up to (3) three to (5) five business days!

Our recommendation, for mitigating these user experience issues, is to properly
invest time in building a robust and reliable form to acquire merchant
bank account information properly.

Here are some tips:

#. Display a check image to illustrate which number is the routing number vs.
   account number.

   We've conveniently provided one - however, you may choose to design your
   own:

   .. figure:: https://s3.amazonaws.com/justice.web/docs/check_image.png

#. US routing numbers are 9 digits and are usually located in the lower left
   corner of most checks. Common aliases to **routing number**:

   * RTN (Routing Transit Number)
   * ABA
   * `Bank code`_

#. Routing numbers are used to set up direct deposit transfers. You can use this
   as an aid to your customers who are inquiring whether or not they have the
   right routing number.

#. Balanced has provided very useful routing number validators in our
   :ref:`balanced.js <getting_started.balanced.js_bank_accounts>` library.
   Be sure to use these helper functions to build a robust form.

#. Set your customer's expectation that payments might be delayed by up to
   (3) three to (5) five business days if incorrect information is provided.

#. Highlight to your customers that *wire transfer numbers* are **NOT** the same
   as the routing number, and they are **NOT** the same as the bank account
   number. Be sure to clarify this when asking your users for their information.


.. _Bank code: http://en.wikipedia.org/wiki/Bank_code
.. _FedACH directory: https://www.fededirectory.frb.org


The Meta Field
--------------

The ``meta`` field exists on all resources in the Balanced API. It may be used
as a dictionary of arbitrary key/value pairs, where each key and value is a
string of length 255 characters or less. This may be used to, e.g., annotate
accounts in our system with the account name on your system, or annotate
transactions with order numbers. The format is generally up to you, except in
the case of...

Using Meta for Fraud
~~~~~~~~~~~~~~~~~~~~

Balanced reserves some keys in the ``meta`` field. These are fields that may be
passed in by you in order to help fight fraud.

Shipping Address
''''''''''''''''

You may supply shipping fulfillment information by prefixing keys
specifying address data with the ``shipping.`` prefix. The specific
fields you may provide are:

-  shipping.address.street_address
-  shipping.address.city
-  shipping.address.region
-  shipping.address.country_code
-  shipping.carrier
-  shipping.tracking_number

Let's say you want to pass on shipping address, along with shipping
carrier (USPS, UPS, FedEx, etc.) and tracking number on a debit. This is
what the ``meta`` field would look like when represented as a JSON
dictionary:

.. code-block:: javascript

  meta = {
      'shipping.address.street_address': '801 High St',
      'shipping.address.city': 'Palo Alto',
      'shipping.address.region': 'CA',
      'shipping.address.postal_code': '94301',
      'shipping.address.country_code': 'USA',
      'shipping.carrier': 'FEDEX',
      'shipping.tracking_number': '1234567890'
  }


The Hash Attribute
------------------

Every ``Card`` and ``BankAccount`` resource has an attribute than can be used
to check if the same card is being added again.

For credit cards, this is the ``hash`` attribute. This is calculated using
``card_number`` and the expiration.

For bank accounts, this is the ``fingerprint`` attribute. This is calculated using
``account_number``, ``routing_number``, ``name``, and ``type``.

