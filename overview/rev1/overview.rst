Overview
=================

Feature Requests
------------------

As Balanced embraces the `open company philosophy`_, we actively and publicly
discuss feature requests and product decisions with our community on `github`_.
Do you have a feature request or issue? We’d love to hear from you!

.. _overview.support:

Support
-------

We respond to support requests and questions through several channels
including:

Follow `@balancedstatus`_ or check out `status.balancedpayments.com`_
for real-time status updates on the API, balanced.js, and Balanced’s
dashboard.

Join the Balanced `community`_ and follow us on `Twitter`_.

.. cssclass:: list-noindent

  -  `IRC`_ for real-time answers to technical support questions
  -  `Stackoverflow`_ for technical questions
  -  `Quora`_ for product and business questions
  -  Email: `support@balancedpayments.com`_

When encountering a problem, one of the best tools available to you is
the Logs area in the Dashboard. These logs give valuable insight into
what request information was received and the resulting API response. It also
gives information about operation status codes and transaction failure
messages along with the timing and affected parties and endpoints.

If additional help is required, hop into #balanced on IRC to get help
directly from developers.

Be sure to have the following handy to facilitate quick resolutions to issues:

- * A description of the problem
- * The Dashboard link to the transaction(s) related to the issue
- * Transaction OHM (this is the identifier for the corresponding log message. It's returned on errors)
- * Marketplace name
- * Timeframe of issue
- * Affected customer(s)
- * Amount and type of transaction
- * Last 4 digits and type of the affected card (if applicable)


.. _payouts.cutoff:

Submission & Delivery times
---------------------------

.. container:: table-header

   The cutoff for submitting payouts is **3:00 PM Pacific (PT)** time. Payouts will *not* be
   delivered on weekends or `bank holidays`_:

.. cssclass:: table table-hover

  ==================================== =========== ============ ===========
  Holiday                              2014        2015         2016
  ==================================== =========== ============ ===========
  New Year's Day                       January 1   January 1    January 1
  Birthday of Martin Luther King, Jr.  January 20  January 19   January 18
  Washington's Birthday                February 17 February 16  February 15
  Memorial Day                         May 26      May 25       May 30
  Independence Day                     July 4      July 4 [*]_  July 4
  Labor Day                            September 1 September 7  September 5
  Columbus Day                         October 13  October 12   October 10
  Veterans Day                         November 11 November 11  November 11
  Thanksgiving Day                     November 27 November 26  November 24
  Christmas Day                        December 25 December 25  December 26
  ==================================== =========== ============ ===========

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
     - Tuesday @ 9:00AM PT

.. [*] Assumes that day is a working business day -- does not fall on a
       weekend or a `federal reserve holiday <bank holidays>`_.



Pricing
-------------

.. container:: section

  .. container:: header3

    Check out the `pricing page`_ for out current pricing structure!

Balanced will create invoices to collect fees daily. These invoices can be
viewed under the invoices tab of the Balanced dashboard. Fees are debited from
the bank account most recently attached to the owner account of the marketplace.

For example, a buyer pays for a service on Monday from a third-party merchant. You charge
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


.. note::
  :header_class: alert alert-tab
  :body_class: alert alert-gray

  **Balanced will never take fees from the operating capital (escrow account) of the marketplace.**



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
  :body_class: alert alert-gray

  Please contact `support@balancedpayments.com <mailto:support@balancedpayments.com>`__
  if you are planning to process larger amounts.

  These limits do not apply to the marketplace owner bank account.
 


.. _kitchit: http://kitchit.com
.. _copious: http://copious.com
.. _zaarly: http://zaarly.com
.. _visual.ly: http://visual.ly
.. _Crowdtilt.com:
.. _crowdtilt: http://crowdtilt.com
.. _wanderable: http://wanderable.com
.. _Gittip: http://gittip.com
.. _ACH: http://en.wikipedia.org/wiki/Automated_Clearing_House
.. _open partnership: http://blog.gittip.com/post/28351995405/open-partnerships
.. _mitigate the risks of running a marketplace: https://github.com/gittip/www.gittip.com/issues/67
.. _payments infrastructure: https://github.com/gittip/www.gittip.com/pull/137
.. _visual design: https://github.com/gittip/www.gittip.com/issues/66#issuecomment-7439689
.. _fraud preventions systems: https://github.com/gvenkataraman/www.gittip.com/commit/ceb88e6f5e1eb7ae931cf2921866beccb49381b5
.. _discussed pricing decisions: https://github.com/balanced/balanced-api/issues/48
.. _Github: https://github.com/balanced/balanced-api/issues
.. _IRC: http://webchat.freenode.net/?channels=balanced&uio=MTE9OTIaf
.. _Stackoverflow: https://stackoverflow.com/questions/tagged/balanced-payments
.. _Quora: https://quora.com/balanced
.. _support@balancedpayments.com: mailto:support@balancedpayments.com
.. _@balancedstatus: https://twitter.com/balancedstatus
.. _Twitter: https://twitter.com/balanced
.. _status.balancedpayments.com: https://status.balancedpayments.com/
.. _community: https://www.balancedpayments.com/community
.. _Rent My Bike: http://rentmybike.heroku.com
.. _bank holidays: http://www.federalreserve.gov/aboutthefed/k8.htm
.. _FedACH directory: https://www.fededirectory.frb.org
.. _open company philosophy: https://www.balancedpayments.com/open
.. _pricing page: https://www.balancedpayments.com/pricing