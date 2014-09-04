Card Holds
========================

Balanced supports the concept of holds. Holds are a type of
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
  :body_class: alert alert-green alert-persianBlue20 references
  
  .. cssclass:: mini-header
  
    API

  - `Create a Card Hold </1.1/api/card-holds/#create-a-card-hold>`_


A hold is created in a way similar to creating a debit. Creating a card hold
will return a href which can be used to perform a capture later, up to the full
amount of the card hold.

.. snippet:: card-hold-create


Capturing a card hold
---------------------

.. admonition:: References
  :header_class: alert alert-tab full-width alert-tab-persianBlue60
  :body_class: alert alert-green alert-persianBlue20 references
  
  .. cssclass:: mini-header
  
    API

  - `Capture a Card Hold </1.1/api/card-holds/#capture-a-card-hold>`_


When you wish to obtain the funds reserved with a card hold, capture the card
hold.

.. snippet:: card-hold-capture


Voiding a card hold
---------------------

.. admonition:: References
  :header_class: alert alert-tab full-width alert-tab-persianBlue60
  :body_class: alert alert-green alert-persianBlue20 references
  
  .. cssclass:: mini-header
  
    API

  - `Void a Card Hold </1.1/api/card-holds/#void-a-card-hold>`_


If you wish to release the reserved funds you can always void the card hold.

.. snippet:: card-hold-void
