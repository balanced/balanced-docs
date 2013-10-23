FAQ
===

.. _fees:

Pricing & Fees
--------------

You will pay a fee of 25¢ when you successfully payout to a seller’s
bank account, and 2.9% + 30¢ when you successfully charge a buyer’s
credit card. We try to keep our pricing straightforward, so Balanced
does not charge any fees besides those listed here.

.. _fees.payouts:

Payout Pricing
''''''''''''''

It costs just simply 25¢ to issue a next-day ACH credit. Our full
fee per operation is listed below:

.. cssclass:: table table-hover

  ============================ ===============
    Operation                    Cost to you
  ============================ ===============
  next-day ACH                             25¢
  failure                                $1.00
  reversal                                  $0
  batch fee                                 $0
  monthly fee                               $0
  set-up fee                                $0
  payouts to your bank account              $0
  ============================ ===============

.. _fees.processing:

Processing Pricing
''''''''''''''''''

Charging credit cards costs just 2.9% and 30¢ per successful charge. Our full
fees per operation is listed below:

.. cssclass:: table table-hover

  ================================ ===================
    Operation                        Cost to you
  ================================ ===================
  successful credit card charge       2.9% + 30¢ [#]_
  successful bank account charge        1% + 30¢ [#]_
  chargeback                              $15.00
  refund                                      $0
  failure                                     $0
  batch fee                                   $0
  monthly fee                                 $0
  set-up fee                                  $0
  ================================ ===================


.. [#] Includes implicit hold.
.. [#] Fee is capped at $5


.. _invoicing.fees:

Invoicing fees
''''''''''''''

Balanced will create invoices to collect fees daily. These invoices can be
viewed under the invoices tab of the Balanced dashboard. These fees are
debited from the bank account attached to the owner account of the
marketplace.

.. note::
  :header_class: alert alert-tab
  :body_class: alert alert-gray

  **Balanced will never take fees from the operating capital (escrow account) of the marketplace.**

Example
'''''''

A buyer pays for a service on Monday from a third-party merchant. You charge
the buyer $10, which increases your escrow balance by $10. Balanced will invoice
you, on Monday for 2.9% of $10 (or 29¢), plus 30¢, and debit your bank account
for a total of 59¢.

On Wednesday, the third-party merchant completes performing a service for the
buyer, and the buyer acknowledges this. You credit out payment to the
merchant, likely keeping a portion to pay your fees. Perhaps you pay out $7
to the merchant, leaving you with $3 in your escrow account. Balanced will
invoice you, on Wednesday, 25¢ for this ACH credit.

The $3 that is left from the buyer's $10 is your revenue from this order. You
decide to credit this to your own bank account on Friday. Balanced doesn't
charge you for this credit, as credits to owner accounts are free.

Testing
-------

.. _resources.test_credit_cards:

Card Numbers
````````````

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

Bank Accounts
`````````````

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

Simulating erroneous routing numbers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. dcode:: scenario bank-account-invalid-routing-number

Simulating a pending status
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. dcode:: scenario credit_pending_state

Simulating a paid status
~~~~~~~~~~~~~~~~~~~~~~~~

.. dcode:: scenario credit_paid_state

Simulating a failed status
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. dcode:: scenario credit_failed_state

Identity Verification
`````````````````````

.. _resources.test-identity-verification:

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

Support
-------

We respond to support requests and questions through several channels
including:

-  `IRC`_ for real-time answers to technical support questions
-  `Stackoverflow`_ for technical questions
-  `Quora`_ for product and business questions
-  Email: `support@balancedpayments.com`_

Follow `@balancedstatus`_ or check out `status.balancedpayments.com`_
for real-time status updates on the API, balanced.js, and Balanced’s
dashboard.

Join the Balanced `community`_ and follow us on `Twitter`_.

.. _payouts.cutoff:

Payout Submission & Delivery Times
----------------------------------

.. container:: table-header

   The cutoff for submitting payouts is **3:00 PM Pacific (PT)** time. Payouts will *not* be
   delivered on weekends or `bank holidays`_:

.. cssclass:: table table-hover

  ==================================== =========== =========== =========== ============ ===========
  Holiday                              2012        2013        2014        2015         2016
  ==================================== =========== =========== =========== ============ ===========
  New Year's Day                       January 2   January 1   January 1   January 1    January 1
  Birthday of Martin Luther King, Jr.  January 16  January 21  January 20  January 19   January 18
  Washington's Birthday                February 20 February 18 February 17 February 16  February 15
  Memorial Day                         May 28      May 27      May 26      May 25       May 30
  Independence Day                     July 4      July 4      July 4      July 4 [*]_  July 4
  Labor Day                            September 3 September 2 September 1 September 7  September 5
  Columbus Day                         October 8   October 14  October 13  October 12   October 10
  Veterans Day                         November 12 November 11 November 11 November 11  November 11
  Thanksgiving Day                     November 22 November 28 November 27 November 26  November 24
  Christmas Day                        December 25 December 25 December 25 December 25  December 26
  ==================================== =========== =========== =========== ============ ===========

.. [*] Saturday

.. container:: table-header

   Here's some common scenarios for payouts. Remember, the next-day cut off is
   at **3:00 PM Pacific (PT)**.

.. list-table::
   :widths: 20 35 20
   :header-rows: 1
   :class: table table-hover

   * - Type of scenario
     - Example submission date
     - Available when? [*]_
   * - Most common
     - Tuesday @ 1:45PM PT
     - Wednesday @ 9:00AM PT
   * - `Bank holidays`_
     - July 3rd @ 1:30PM PT
     - July 5th @ 9:00AM PT
   * - Late submission
     - Friday @ 3:30PM PT
     - Tuesday @ 3:30PM PT

.. [*] Assumes that day is a working business day -- does not fall on a
       weekend or a `federal reserve holiday <bank holidays>`_.

.. _sample page: https://gist.github.com/2662770
.. _balanced.js: https://js.balancedpayments.com/v1/balanced.js
.. _testing documentation: /docs/testing#simulating-card-failures
.. _jQuery: http://www.jquery.com
.. _dashboard: https://dashboard.balancedpayments.com/
.. _issues: https://github.com/balanced/balanced-api/issues
.. _bank holidays: http://www.federalreserve.gov/aboutthefed/k8.htm
.. _FedACH directory: https://www.fededirectory.frb.org
.. _github issue #151: https://github.com/balanced/balanced-api/issues/151
.. _github issue #70: https://github.com/balanced/balanced-api/issues/70
.. _github issue #132: https://github.com/balanced/balanced-api/issues/132

Canceling Credits
-----------------

Canceling a credit is currently under active development and discussion on
`github issue #151`_ - it's not very straightforward due to the asynchronous
nature of ACH.

If you require immediately canceling of a credit, please contact us via any
of our :ref:`support channels <overview.support>` and we will attempt to cancel the
credit.

When referencing a specific credit, please provide the credit's ``uri`` so that
we may quickly proceed with fulfilling your request.

.. _Github: https://github.com/balanced/balanced-api/issues
.. _IRC: http://webchat.freenode.net/?channels=balanced&uio=MTE9OTIaf
.. _Stackoverflow: https://stackoverflow.com/questions/tagged/balanced-payments
.. _Quora: https://quora.com/balanced
.. _support@balancedpayments.com: mailto:support@balancedpayments.com
.. _@balancedstatus: https://twitter.com/balancedstatus
.. _Twitter: https://twitter.com/balanced
.. _status.balancedpayments.com: https://status.balancedpayments.com/
.. _community: https://www.balancedpayments.com/community

.. _quirksmode: http://www.quirksmode.org/js/placejs.html
.. _full example page: https://gist.github.com/2662770
.. _LUHN check: http://en.wikipedia.org/wiki/Luhn_algorithm
.. _MICR Routing Number Format: http://en.wikipedia.org/wiki/Routing_transit_number#MICR_Routing_number_format
.. _jQuery: http://www.jquery.com
.. _JSFiddle: http://jsfiddle.net/
.. _JSFiddle - Tokenize bank accounts: http://jsfiddle.net/balanced/ZwhrA/
.. _JSFiddle - Tokenize credit cards: http://jsfiddle.net/balanced/ZwhrA/
.. _PCI-DSS Level 1 Compliant: http://www.visa.com/splisting/searchGrsp.do?companyNameCriteria=Pound%20Payments

