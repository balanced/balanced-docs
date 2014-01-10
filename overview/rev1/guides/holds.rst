Working with Holds
===================

Balanced supports the concepts of :term:`holds`. Holds are a type of
authorization that reserves a dollar amount on a credit card to be captured at
a later time, usually within 7 days. If the transaction is not processed
(known as post-authorization) by the end of the hold period, the amount is added
back to the available credit on the cardholder's credit card.
**The customer is not billed.**

Holds are common in the industries where the amount of the goods or services
are "reserved" on the cardholder's credit card.

If you issue a debit on an account, Balanced uses holds behinds the scenes
but captures the funds immediately -- you will
**always see an expanded hold resource returned on a debit representation**.

.. warning::
  :header_class: alert alert-tab
  :body_class: alert alert-gray

  For all intents and purposes, Balanced does not recommend holds and considers
  their usage as a very advanced feature as they cause much confusion and are
  cumbersome to manage.

  If your project requires holds and you need help, please reach out
  to us using our :ref:`support channels <overview.support>`.

Creating a hold
------------------

A hold is created in a way similar to creating a debit. Creating a hold will
return a URI which can be used to perform a capture later, up to the full
amount of the hold.

.. .. dcode:: scenario hold-create


Capturing a hold
-------------------

Here's an example on how to capture a hold:

.. .. dcode:: scenario hold-capture



.. _sample page: https://gist.github.com/2662770
.. _balanced.js: https://js.balancedpayments.com/v1/balanced.js
.. _testing documentation: /docs/testing#simulating-card-failures
.. _jQuery: http://www.jquery.com