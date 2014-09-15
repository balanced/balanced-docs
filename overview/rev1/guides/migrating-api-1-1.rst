Migrating to API 1.1
======================

**API v1.1 is not backward-compatible with v1.0.** Resources deprecated in v1.0 were
removed in v1.1, ``Account`` for example. Many attribute names were standardized.
Features were superseded.

When using API v1.1, v1.0 URIs (/v1/...) are automatically handled by the API, so no
modification is necessary. As always, **do not manually build URIs/hrefs**.

|

Topic overview
-----------------

Fortunately, migrating from API 1.0 to API 1.1 is fairly simple.
By the end of this topic, you should understand the following:

- Key changes introduced in API 1.1.
- An overview of the general steps needed to migrate to API 1.1.


1.1 Changelog
---------------

Resource removals
~~~~~~~~~~~~~~~~~~

The ``Account`` resource, deprecated in 1.0 in favor of the ``Customer`` resource, has been removed.


Resource additions
~~~~~~~~~~~~~~~~~~~~

The `Order </1.1/guides/orders>`_ resource has been added.

  An ``Order`` resource is a construct that logically groups related transaction operations for a
  particular merchant (Customer). The ``Order`` resource facilitates transaction reconciliation in the
  following ways:

  |
  
  - each ``Order`` maintains an individual balance, which is separate from both other ``Order`` balances the marketplace balance
  - prevents over crediting funds by allowing payouts up to the amount_escrowed in each Order
  - flow of funds is trackable as funds credited from an Order are mapped to the Debits that brought the funds into it
  
  The Order resource supersedes the use of ``on_behalf_of`` and ``payment_group_code``.
  
Failed transactions create a resource instance.

  Failing to create a transaction will result in a transaction being created with a ``FAILED`` status.
  E.g. debiting a card with insufficient funds will result in a transaction created with a ``FAILED`` status.
  These are filtered out of the API responses by default but can be specifically retrieved with a status
  filter e.g. ``GET /credits?status=failed``


Operational changes
~~~~~~~~~~~~~~~~~~~~

balanced.js no longer requires an ``init()`` call.

  Funding instruments are not tokenized directly under a marketplace. They must be claimed after tokenization.

Funding instruments tokenized via balanced.js must be claimed.

  Before they can be used, funding instruments must be claimed to the marketplace by performing an
  authenticated request such as a ``GET`` on the funding instrument, or associating it to a ``Customer``.
  Unclaimed tokenized funding instruments are discarded after a short timeframe.

Tokenizations via balanced.js do not appear in logs.

  Tokenizations do not appear in marketplace logs because tokenizations occur at the root level
  and not under the marketplace.

Card verifications are performed after a ``Card`` is claimed.

  Card verifications such as CVV and AVS checks are performed when the ``Card`` is claimed to a
  marketplace. An authenticated request will claim the card and initiate the verifications.

Funding instruments do not require a ``Customer``

  Funding instruments, with the exception of bank accounts you wish to debit, do not require an associated
  ``Customer``.

Transactions are performed via orders.

  ``Customer`` resources are no longer debitable or creditable. Transactions should be performed via ``Orders``.
  E.g. ``order.debit_from(source=buyer_card, amount=amount)``,
  ``order.credit_to(source=merchant_bank_account, amount=amount)`` should now be used
  instead of ``customer.debit`` or ``customer.credit``.


Transaction statuses have been standardized.

  Transaction statuses are one of: ``pending``, ``succeeded``, ``failed``.
  
  There is no longer a ``paid`` status.


``uri`` attributes have transitioned to ``href`` attributes.


Hypermedia API
~~~~~~~~~~~~~~~

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
tooling that handles JSON API out of the box. For example, Balanced now uses
the `EmberJS JSON API support`_ rather than the old `customized data library`_.



Migrate to API 1.1
---------------------

Step 1: Migrate from Account to Customer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``Account`` resource was deprecated in v1.0 in favor of the ``Customer`` resource.
Migrating to Customer is simple and must be done before migrating to v1.1. To simplify
migration, each ``Account`` has a 1:1 mapping to a ``Customer`` instance that has the
same ``Card``, ``BankAccount``, and transaction information. This ``Customer`` instance
is accessible through the ``customer_uri`` attribute on the ``Account`` instance.

Since everyone's application code differs, we'll offer some simple pseudocode:

.. code-block:: html

  for each stored account uri
    replace stored uri with account's customer_uri attribute


Underwriting differs between ``Account`` and ``Customer``.

  Underwriting is not required for ``Customer`` resource creation. Repeat updating the ``Customer``
  resource with more information until the ``Customer`` has a ``merchant_status`` attribute of
  ``underwritten``.

``Customer`` does not have a unique email constraint.

  Marketplaces that rely on a unique email constraint for ``Account`` instances need to implement
  their own logic to retain this ability.
  


Step 2: Update the client library version
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Update your client library version to the latest 1.x version available. **1.x library versions
are for API v1.1 or newer. 0.x library versions are for API v1.0.**

Client libraries that retrieved resources via the ``find`` method should now use the
``fetch`` method.

Many field names and resource attributes were standardized, new ones added, some removed. Refer to the
`API documentation </1.1/api>`_ for more information.


Step 3: Upgrade balanced.js
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Review the `balanced.js guide </1.1/guides/balanced-js>`_.

Tokenizations do not appear in marketplace logs because tokenizations occur at the root level and
not under the marketplace. After tokenizing a card, claim it to the marketplace with an
authenticated request. This will also initiate card verifications, if the funding instrument is a
``Card``.

balanced.js no longer requires an ``init()`` call with the marketplace URI. Remove it.

Update fields for card payloads.

  - ``card_number`` is now ``number``.
  - ``security_code`` is now ``cvv``.
  - ``phone_number`` has been removed.
  - Address fields are no longer top level. Place them in an object as the ``address`` field.
  - ``street_address`` is now two separate fields, ``line1`` and ``line2``.
  - ``region`` has been removed.

Update fields for bank account payloads.

  ``type`` is now ``account_type``


Step 4: Update transaction logic to use ``Orders``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In 1.0, transaction calls operated around the ``Customer`` resource, e.g. ``customer.debit``.
Transaction code logic should now be updated to use the ``Order`` resource.

We begin by creating an Order. ``merchant`` is an instance of a ``Customer``.

.. snippet:: order-create

Then we can debit a buyer.

.. snippet:: order-debit

Then we can credit the merchant.

.. snippet:: order-credit


See the `Orders guide </1.1/guides/orders>`_ for more information.

|

Associating a ``Customer`` and a ``Card`` is now done via the funding instrument.

.. snippet:: card-associate-to-customer


Additional resources
~~~~~~~~~~~~~~~~~~~~~~

Sometimes it helps to see a real-world example. Our example application, RentMyBikes,
demonstrates a Balanced integration in Python and Ruby on Rails. Below are pull
requests showing the process of migrating RentMyBikes to API 1.1 and introducing use
of the ``Order`` resource.

| RentMyBikes Rails 1.1 - https://github.com/balanced/rentmybikes-rails/pull/22
| RentMyBikes Rails Orders - https://github.com/balanced/rentmybikes-rails/pull/25
| RentMyBikes Python 1.1 - https://github.com/balanced/rentmybikes/pull/8
| RentMyBikes Python Orders - https://github.com/balanced/rentmybikes/pull/11




.. _format spec: http://jsonapi.org/format
.. _JSON API envelope: http://jsonapi.org/
.. _EmberJS JSON API support: https://github.com/daliwali/ember-json-api
.. _customized data library: https://github.com/balanced/balanced-dashboard/blob/master/app/models/core/serializers/rev0.js
.. _creating transactions with a failed status: https://gist.github.com/mjallday/7589639
.. _charging cards without a customer: https://gist.github.com/mjallday/7589592
.. _Orders resource: https://gist.github.com/mjallday/92940a2e9dcb07f5b038