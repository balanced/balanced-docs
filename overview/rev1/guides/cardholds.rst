Working with Card Holds
========================

Balanced supports the concepts of :term:`holds`. Holds are a type of
authorization that reserves a dollar amount on a credit card to be captured at
a later time, usually within 7 days. If the transaction is not processed
(known as post-authorization) by the end of the hold period, the amount is
released back to the available credit on the cardholder's credit card.
**The customer is not billed.**

Holds are common in the industries where the amount of the goods or services
are "reserved" on the cardholder's credit card or.

If you issue a debit on an account, Balanced uses holds behinds the scenes
but captures the funds immediately -- you will
**always see an expanded hold resource returned on a debit representation**.

.. warning::
  :header_class: alert alert-tab
  :body_class: alert alert-green

  For all intents and purposes, Balanced does not recommend holds and considers
  their usage to be a very advanced feature as they cause much confusion and are
  cumbersome to manage.

  If your project requires holds and you need help, please reach out
  to us using our :ref:`support channels <overview.support>`.


Creating a card hold
--------------------

A hold is created in a way similar to creating a debit. Creating a card hold
will return a href which can be used to perform a capture later, up to the full
amount of the card hold.

.. code-block:: ruby

  # card_href is the stored href for the Card
  card = Balanced::Card.fetch(card_href)
  card.hold(
    :amount => 5000,
    :description => 'Some descriptive text for the debit in the dashboard'
  )

.. code-block:: python

  # card_href is the stored href for the Card
  card = balanced.Card.fetch(card_href)
  card_hold = card.hold(
    amount=5000,
    description='Some descriptive text for the debit in the dashboard'
  )

.. code-block:: bash

  # :card_id is the stored id for the Card
  curl https://api.balancedpayments.com/cards/:card_id/card_holds \
       -H "Accept: application/vnd.api+json;revision=1.1" \
       -u ak-test-h7F8F3u41y6LzCK4nZeVd5BafaWOUuZL: \
       -d "amount=5000" \
       -d "description=Some descriptive text for the debit in the dashboard"

Capturing a card hold
---------------------

|

API References:

.. cssclass:: list-noindent

- `Capture a Card Hold </1.1/api/card-holds/#capture-a-card-hold>`_

|

When you wish to obtain the funds reserved with a card hold, capture the card
hold.

.. code-block:: ruby

  # card_hold_href is the stored href for the CardHold
  card_hold = Balanced::CardHold.fetch(card_hold_href)
  debit = card_hold.capture(
    :description => 'Some descriptive text for the debit in the dashboard',
    :appears_on_statement_as => 'ShowsUpOnStmt'
  )

.. code-block:: python

  # card_hold_href is the stored href for the CardHold
  card_hold = balanced.CardHold.fetch(card_hold_href)
  debit = card_hold.capture(
    appears_on_statement_as='ShowsUpOnStmt',
    description='Some descriptive text for the debit in the dashboard'
  )

.. code-block:: bash

  # :card_hold_id is the stored id for the CardHold
  curl https://api.balancedpayments.com/card_holds/:card_hold_id/debits \
       -H "Accept: application/vnd.api+json;revision=1.1" \
       -u ak-test-h7F8F3u41y6LzCK4nZeVd5BafaWOUuZL: \
       -d "appears_on_statement_as=ShowsUpOnStmt" \
       -d "description=Some descriptive text for the debit in the dashboard"

Voiding a card hold
---------------------

|

API References:

.. cssclass:: list-noindent

- `Void a Card Hold </1.1/api/card-holds/#void-a-card-hold>`_

|

If you wish to release the reserved funds you can always void the card hold.

.. code-block:: ruby

  # card_hold_href is the stored href for the CardHold
  card_hold = Balanced::CardHold.fetch(card_hold_href)
  card_hold.void

.. code-block:: python

  # card_hold_href is the stored href for the CardHold
  card_hold = balanced.CardHold.fetch(card_hold_href)
  card_hold.cancel()

.. code-block:: bash

  # :card_hold_id is the stored id for the CardHold
  curl https://api.balancedpayments.com/card_holds/:card_hold_id \
       -H "Accept: application/vnd.api+json;revision=1.1" \
       -u ak-test-h7F8F3u41y6LzCK4nZeVd5BafaWOUuZL: \
       -X PUT \
       -d "is_void=true"

.. _sample page: https://gist.github.com/2662770
.. _balanced.js: https://js.balancedpayments.com/v1/balanced.js
.. _testing documentation: /docs/testing#simulating-card-failures
.. _jQuery: http://www.jquery.com