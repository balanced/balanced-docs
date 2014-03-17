.. _resources:

Resources
=========

.. _resources.test-credit-cards:

Test credit card numbers
------------------------

These cards will be accepted in our system only for a **TEST** marketplace.
**Do not use these card numbers in Production marketplaces.**

.. cssclass:: table

  ============== =========================== ================ ==============================
   Card Brand          Number                       CVV         Result
  ============== =========================== ================ ==============================
  ``VISA``        ``4111111111111111``            ``123``       Success
  ``MasterCard``  ``5105105105105100``            ``123``       Success
  ``AMEX``         ``341111111111111``           ``1234``       Success
  ``VISA``        ``4444444444444448`` [#]_       ``123``       Processor Failure
  ``VISA``        ``4222222222222220`` [#]_       ``123``       Tokenization Error
  ``MasterCard``  ``5112000200000002``            ``200``       CVV Match Fail
  ``VISA``        ``4457000300000007``            ``901``       CVV Unsupported
  ============== =========================== ================ ==============================

.. [#] Simulate a card which can be tokenized but will not be accepted for creating
       holds or debits. This type of failure is what you would expect if you try to
       create a hold on a card with insufficient funds.
.. [#] To simulate a card which cannot be tokenized but passes a LUHN check. You could
       expect this failure when a user tried to enter in a credit card which used to
       work but has been canceled.


.. _resources.test-bank-accounts:

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
   :class: table

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
     - Transitions status to ``pending``
   * - ``321174851``
     - ``9900000001``
     - Transitions status to ``pending``
   * - ``021000021``
     - ``9900000002``
     - Transitions status to ``succeeded``
   * - ``321174851``
     - ``9900000003``
     - Transitions status to ``succeeded``
   * - ``021000021``
     - ``9900000004``
     - Transitions status to ``failed``
   * - ``321174851``
     - ``9900000005``
     - Transitions status to ``failed``


.. _resources.test-identity-verification:

Testing Customer identity verification
---------------------------------------

``Customer`` resources have a ``merchant_status`` attribute for determining
the Customer's underwritten status.

Supply address and date of birth information to trigger a ``true`` response.

The following will set ``merchant_status`` to ``underwritten``

.. code-block:: javascript

  {
      "name": "Henry Ford",
      "dob_month": 07,
      "dob_year": 1985,
      "address": {
          "postal_code": "48120"
      }
  }


The following will set ``merchant_status`` to ``need-more-information``

.. code-block:: javascript

  {
      "name": "Henry Ford",
      "dob_month": 07,
      "dob_year": 1985
  }

``merchant_status`` will be one of: ``need-more-information``, ``underwritten``,
or ``rejected``.


Funding Instrument Fingerprint
--------------------------------

Every ``Card`` and ``BankAccount`` resource has a ``fingerprint`` attribute
that can be used to check if a card has already been tokenized.

For credit cards, ``fingerprint`` is calculated using ``card_number`` and the
card expiration date.

For bank accounts, ``fingerprint`` is calculated using ``account_number``,
``routing_number``, ``name``, and ``type``.


.. _resources.address-verification-service:

Address Verification Service
----------------------------

AVS, Address Verification Service, provides a means to verify that the address
supplied during card tokenization matches the address of the credit card.

Supplying a ``street_addrees`` or ``postal_code`` during tokenization initiates
the AVS check. The ``Card`` will have a ``postal_code_check`` attribute
containing the AVS check result.

``avs_street_match`` will be one of: ``yes``, ``no``, ``unsupported``
``postal_code_check`` will be one of: ``yes``, ``no``, ``unsupported``

Additionally, ``avs_result`` can be examined to ascertain more detailed
information about the address verification attempt. 


Simulating Postal Code Check Responses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Postal code test values:

.. cssclass:: table

  ============== ====================================
   Postal Code    Result                    
  ============== ====================================
  ``94301``        AVS Postal code matches      
  ``90210``        AVS Postal code does not match
  ``90211``        AVS Postal code is unsupported
  ============== ====================================


Simulating AVS Street Match Responses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cssclass:: table

  =================== ================== ===========================
  Address line1        Postal Code        Result             
  =================== ================== ===========================
  ``965 Mission St``   ``94103``          AVS street matches
  ``21 Jump St``       ``90210``          AVS street does not match
  =================== ================== ===========================



.. _resources.card-verification-value:

Card Verification Value
-----------------------

CVV, Card Verification Value, provides a means to verify that the
``cvv`` supplied during card tokenization matches the CVV
for the credit card. The ``Card`` will have a ``cvv_match``
attribute containing the CSC check result. It's strongly recommended you do
not process transactions with cards that fail this check.

``cvv_match`` will be one of: ``yes``, ``no``, ``unsupported``

Additionally, ``cvv_result`` can be examined to ascertain more detailed
information about the match attempt.


1.1 Changelog
---------------

A short list of changes:

.. cssclass:: list-noindent

  - * Hypermedia API
  - * Cards can be charged without being associated to a customer
  - * Transactions are now created via the funding instrument, not via the customer. E.g. `card.debit(amount)`, `bank_account.credit(amount)` is now favoured over `customer.debit(card, amount)`
  - * Failing to create a transaction will result in a transaction being created with a `FAILED` status. E.g. debiting a card with insufficient funds will result in a transaction with a `FAILED` status. These are filtered out of the API by default but can be specifically retrieved with a status filter e.g. `/credits?status=failed`
  - * A new resource called "Orders" has been created to allow grouping transactions. An Order can consist of 0:n buyers, 0:n debits and 0:n credits to a single seller. Each debit associated with an Order will result in the Order's escrow balance accruing the value of the debit rather than the marketplace's escrow balance. You cannot pay out more than the total amount escrowed for an Order.
  - * Accounts no longer exist, customers and orders are the primary grouping constructs for transactions, customers are the primary grouping construct for funding instruments.
  - * Funding instruments can be tokenized without specifying the marketplace, performing an authenticated GET on the tokenized funding instrument will automatically associate it to your marketplace.
  - * Transaction statuses have been standardized to be one of: ``pending``, ``succeeded``, ``failed``. There is no longer a ``paid`` status.

The most obvious technical difference between revision 1.1 and 1.0 is that the
Balanced API switched from plain JSON to a `JSON API envelope`_. You can learn
more about JSON API by reading the `format spec`_. In a nutshell, JSON API
standardizes the structure of request and response payloads. It allows us to
handle some edge cases that our previous formats could not handle such as side
loading un-nested content.

Here's what a typical resource now looks like with revision 1.1:

.. code-block:: bash

  curl https://api.balancedpayments.com/marketplaces/TEST-MP1TCNbswn3s3I2UxnZyM7Pq \
      -u ak-test-2DBryLFR3BBam1CipbWEGSO6gqVOBKghP:

.. code-block:: javascript

  {
    "marketplaces": [
      {
        "in_escrow": 10091234,
        "domain_url": "example.com",
        "name": "Test Marketplace",
        "links": {
          "owner_customer": "CU1TEG4xJzSrSn7mVtzE7SKI"
        },
        "href": "/marketplaces/TEST-MP1TCNbswn3s3I2UxnZyM7Pq",
        "created_at": "2013-11-14T19:09:10.924065Z",
        "support_email_address": "support@example.com",
        "updated_at": "2013-11-14T19:09:11.758110Z",
        "support_phone_number": "+16505551234",
        "production": false,
        "meta": {},
        "unsettled_fees": 0,
        "id": "TEST-MP1TCNbswn3s3I2UxnZyM7Pq"
      }
    ],
    "links": {
      "marketplaces.debits": "/debits",
      "marketplaces.reversals": "/reversals",
      "marketplaces.customers": "/customers",
      "marketplaces.credits": "/credits",
      "marketplaces.cards": "/cards",
      "marketplaces.card_holds": "/card_holds",
      "marketplaces.refunds": "/refunds",
      "marketplaces.owner_customer": "/customers/{marketplaces.owner_customer}",
      "marketplaces.transactions": "/transactions",
      "marketplaces.bank_accounts": "/bank_accounts",
      "marketplaces.callbacks": "/callbacks",
      "marketplaces.events": "/events"
    }
  }


Here's what the same resource looked like in revision 1.0:

.. code-block:: bash

  curl https://api.balancedpayments.com/v1/marketplaces/TEST-MP1TCNbswn3s3I2UxnZyM7Pq \
      -u ak-test-2DBryLFR3BBam1CipbWEGSO6gqVOBKghP:

.. code-block:: javascript

  {
    "callbacks_uri": "/v1/marketplaces/TEST-MP1TCNbswn3s3I2UxnZyM7Pq/callbacks",
    "support_email_address": "support@example.com",
    "_type": "marketplace",
    "events_uri": "/v1/events",
    "accounts_uri": "/v1/marketplaces/TEST-MP1TCNbswn3s3I2UxnZyM7Pq/accounts",
    ...
    "debits_uri": "/v1/marketplaces/TEST-MP1TCNbswn3s3I2UxnZyM7Pq/debits",
    "credits_uri": "/v1/marketplaces/TEST-MP1TCNbswn3s3I2UxnZyM7Pq/credits",
    "bank_accounts_uri": "/v1/marketplaces/TEST-MP1TCNbswn3s3I2UxnZyM7Pq/bank_accounts"
  }


By no longer nesting resources in responses clients are simpler. Payload size is
also reduced if nested resources are duplicated. Additionally, by standardizing
on JSON API, an open specification, Balanced enables customers to utilize
tooling that handles JSON API out of the box. For example, Balanced `now uses`_
the `EmberJS JSON API support`_ rather than the old `customized data library`_.

We've also fixed up many inconsistencies in revision 1.0 and enabled some handy
behavior such as `creating transactions with a failed status`_, and  
`charging cards without a customer`_. We've also added a new `Orders resource`_
which allow you to keep track of order fulfillment and ensure against
accidental over payouts.

.. _FedACH directory: https://www.fededirectory.frb.org

.. _now uses: https://github.com/balanced/balanced-dashboard/issues/671
.. _EmberJS JSON API support: https://github.com/daliwali/ember-json-api
.. _customized data library: https://github.com/balanced/balanced-dashboard/blob/master/app/models/core/serializers/rev0.js
.. _format spec: http://jsonapi.org/format
.. _JSON API envelope: http://jsonapi.org/
.. _creating transactions with a failed status: https://gist.github.com/mjallday/7589639
.. _charging cards without a customer: https://gist.github.com/mjallday/7589592
.. _Orders resource: https://gist.github.com/mjallday/92940a2e9dcb07f5b038