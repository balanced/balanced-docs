.. _processing:

Processing
==========

Balanced provides a complete processing solution for accepting credit
card payments in a simple, secure manner, relieving you from the hassles
of PCI compliance.


Debits
------

.. container:: span6

   .. container:: header3

      Tutorials

   .. icon-box-widget::
     :box-classes: box box-block box-blue
     :icon-classes: icon icon-page

     :ref:`Collect credit card info <getting_started.collecting_card_info>`

   .. icon-box-widget::
     :box-classes: box box-block box-blue
     :icon-classes: icon icon-page

     :ref:`Charge a credit card <getting_started.charging_cards>`


.. container:: span6

   .. container:: header3

     Form Building

   .. icon-box-widget::
     :box-classes: box box-block box-turquoise
     :icon-classes: icon icon-page

     `Sample credit card form <http://jsfiddle.net/balanced/ZwhrA/>`_
   
   .. icon-box-widget::
     :box-classes: box box-block box-turquoise
     :icon-classes: icon icon-page

     `Sample bank account form <http://jsfiddle.net/balanced/ZwhrA/>`_


.. container:: span6

   .. container:: header3

     Testing

   .. icon-box-widget::
     :box-classes: box box-block box-purple
     :icon-classes: icon icon-page

     :ref:`Test credit card numbers <resources.test_credit_cards>`


.. clear::

Refunds
-------

You can refund a debit up to its original amount, so that means you can partially
refund a debit as well.

In order for a refund to go through successfully, you *must* have enough money
in :ref:`implicit escrow <mp.escrow>` to cover your refund.

.. note::
  :header_class: alert alert-tab
  :body_class: alert alert-green

  For credit cards it typically takes one business day for refunds to
  be reflected on a card statement, but it's possible for the issuing bank to
  take as many as five business days to process a refund.


Here are some scenarios:

Full Refund
~~~~~~~~~~~

Let's say you've debited an account for $20.00

* Your marketplace's `dashboard <https://dashboard.balancedpayments.com/#/marketplaces/>`_ escrow balance says $20.00
* You issue a refund for $20.00
* Your marketplace's `dashboard <https://dashboard.balancedpayments.com/#/marketplaces/>`_ escrow balance says $0.00


Partial Refund
~~~~~~~~~~~~~~

You can also perform multiple partial refunds up to the original amount.

Let's say you've debited an account for $20.00

* Your marketplace's `dashboard <https://dashboard.balancedpayments.com/#/marketplaces/>`_ escrow balance says $20.00
* You issue a refund for $10.00
* Your marketplace's `dashboard <https://dashboard.balancedpayments.com/#/marketplaces/>`_ escrow balance says $10.00
* You issue another refund for $5.00
* Your marketplace's `dashboard <https://dashboard.balancedpayments.com/#/marketplaces/>`_ escrow balance says $5.00

Not Enough Funds to Refund
~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's say you've debited an account for $20.00

* Your marketplace's `dashboard <https://dashboard.balancedpayments.com/#/marketplaces/>`_ escrow balance says $20.00
* You issue a refund for $30.00
* The API will return a **400** status code, similar to:

.. code-block:: bash

   Bad Request: 400: Invalid field [amount] - "3000" must be <= 2000


.. _processing.holds:

Holds
-----

Balanced supports the concepts of :term:`holds`. Holds are a type of
authorization that reserves (i.e. holds) a dollar amount on the customer's
credit card for the merchant to process later, usually within 7 days. If the
transaction is not processed (known as post-authorization) by the end of the
hold period, the amount is added back to the available credit on the
cardholder's credit card. **The customer is not billed.**

Holds are common in the industries where the amount of the goods or services
are "reserved" on the cardholder's credit card.

If you issue a debit on an account, Balanced uses holds behinds the scenes
but captures the funds immediately -- you will
**always see an expanded hold resource returned on a debit representation**.

.. warning::
  :header_class: alert alert-tab
  :body_class: alert alert-green

  For all intents and purposes, Balanced does not recommend holds and considers
  their usage as a very advanced feature as they cause much confusion and are
  cumbersome to manage.

  If your project requires holds and you need help, please reach out
  to us using our :ref:`support channels <overview.support>`.

Creating a hold
~~~~~~~~~~~~~~~

A hold is created in a way similar to creating a debit. Creating a hold will
return a URI which can be used to perform a capture later, up to the full
amount of the hold.

.. dcode:: scenario hold-create


Capturing a hold
~~~~~~~~~~~~~~~~

Here's an example on how to capture a hold:

.. dcode:: scenario hold-capture



.. _sample page: https://gist.github.com/2662770
.. _balanced.js: https://js.balancedpayments.com/v1/balanced.js
.. _testing documentation: /docs/testing#simulating-card-failures
.. _jQuery: http://www.jquery.com


.. _processing.transaction-limits:

Transaction Limits
------------------

The minimum transaction amount is $0.50.

The maximum transaction amounts are as follows:

Credit cards - $15,000 per transaction.

Bank account debits - $15,000 per transaction.

Bank account credits - $15,000 per transaction.


.. note::
  :header_class: alert alert-tab
  :body_class: alert alert-green

  Please contact `support@balancedpayments.com <mailto:support@balancedpayments.com>`__
  if you are planning to process larger amounts.

  These limits do not apply to the marketplace owner bank account.
