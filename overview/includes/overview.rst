.. note::
  :class: lead alert alert-info

  Please excuse our layout as we overhaul our documentation.

  * Click here for our `**OLD** documentation <https://www.balancedpayments.com/docs/api_old>`_

Overview
========

About Balanced
--------------

Balanced is a payments company that enables entrepreneurs and developers
to create new and amazing e-commerce experiences. We’ve built a
white-labeled API and web-based dashboard to help them do this.
Specifically, we offer two products: Balanced Payouts and Balanced
Processing, which can be coupled. We really like working with
marketplaces and crowd-funding platforms, but Balanced can be used for
any type of e-commerce model. You should use Balanced to charge your
buyers’ credit cards and/or pay out to your sellers’ US-based bank
accounts via `ACH`_.

We’ve been processing live transactions since October, 2010 and have a
history of working closely with our customers to solve their problems,
specifically those related to multi-party transactions. For example,
we’re in an `open partnership`_ with `Gittip`_ after volunteering code
and expertise to help them `mitigate the risks of running a
marketplace`_. To date, Balanced has contributed to Gittip’s `payments
infrastructure`_, `visual design`_, and `fraud preventions systems`_.

Balanced believes in openness and transparency, so, despite being a
payments company, we try to discuss as much of our product development
decisions in public as possible. We’ve even `discussed pricing
decisions`_ publicly with our customers.

Github Issues
-------------

We actively and publicly discuss feature requests and product decisions
with our community on `github`_. We’d love to hear from you.

.. _support:

Support
-------

We respond to support requests and questions through several channels
including:

-  `IRC`_ for real-time answers to technical support questions
-  `Stackoverflow`_ for technical questions
-  `Quora`_ for product and business questions
-  Email: `support@balancedpayments.com`_

Follow `@balancedstatus`_ or check out `status.balancedpayments.com`_
for real-time status updates on the API, ``balanced.js``, and Balanced’s
dashboard.

Join the Balanced `community`_ and follow us on `Twitter`_.

Pricing
-------

You will pay a fee of 25¢ when you successfully payout to a seller’s
bank account, and 2.9% + 30¢ when you successfully charge a buyer’s
credit card. We try to keep our pricing straightforward, so Balanced
does not charge any fees besides those listed here.

Payouts
~~~~~~~

It costs just simply 25¢ to issue a next day ACH credit. Our full
fee per operation is listed below:

.. cssclass:: table table-hover

  ============================ ===============
    operation                    cost to you
  ============================ ===============
  next-day ACH                             25¢
  failure                                $3.50
  reversal                                  $0
  batch fee                                 $0
  monthly fee                               $0
  set-up fee                                $0
  payouts to your bank account              $0
  ============================ ===============

Processing
~~~~~~~~~~

Balanced Processing costs just 2.9% and 30¢ per successful charge. Our full
fee per operation is listed below:

.. cssclass:: table table-hover

  ============================ ===============
    operation                    cost to you
  ============================ ===============
  successful charge                 2.9% + 30¢
  chargeback                            $15.00
  refund                                    $0
  failure                                   $0
  batch fee                                 $0
  monthly fee                               $0
  set-up fee                                $0
  ============================ ===============

.. _overview.fees.balanced:

How does Balanced take its cut?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Balanced will create invoices to collect fees daily. These invoices can be
viewed under the ``invoices`` tab of the Balanced dashboard. These fees are
debited from the bank account attached to the owner account of the
marketplace. Please note that Balanced will never take fees from the operating
capital (escrow account) of the marketplace.

Example:
''''''''

- A buyer pays for a service on Monday from a third-party merchant. You charge
  the buyer $10, which increases your escrow balance by $10.

  * Balanced will invoice you, on Monday for 2.9% of $10 (or 29¢), plus 30¢,
    and debit your bank account for a total of 59¢.

- On Wednesday, the third-party merchant completes performing a service for the
  buyer, and the buyer acknowledges this. You credit out payment to the
  merchant, likely keeping a portion to pay your fees. Perhaps you pay out $7
  to the merchant, leaving you with $3 in your escrow account.

  * Balanced will invoice you, on Wednesday, 25¢ for this ACH credit.

- The $3 that is left from the buyer's $10 is your revenue from this order. You
  decide to credit this to your own bank account on Friday.

  * Balanced doesn't charge you for this credit, as credits to owner accounts
    are free.

Popular Use Cases
-----------------

Marketplaces
~~~~~~~~~~~~

Balanced is most often used to power payments for online and mobile
marketplaces -- any platform facilitating payments between buyers and
sellers. For example, `kitchit`_, `copious`_, `zaarly`_, `visual.ly`_,
and many others are connecting Balanced Processing and Balanced Payouts
to charge a buyer’s credit card on behalf of a seller.

Some customers have even implemented a shopping cart checkout flow where
a single buyer can buy from many sellers with a single transaction. And
holding the funds with Balanced between Payouts and Processing can allow
the marketplace to implement an escrow-like functionality.

Crowd-funding
~~~~~~~~~~~~~

Balanced is commonly used to power payments for crowd-funding and group
purchasing platforms. For example, `crowdtilt`_, `wanderable`_,
`gittip`_, and many others are connecting Balanced Processing and
Balanced Payouts to charge many buyers’ credit cards on behalf of a
single seller.


Vendor Payments
~~~~~~~~~~~~~~~

Balanced Payouts is used by many businesses that need to pay their
sellers or vendors for supplies and services rendered.

e-Commerce
~~~~~~~~~~

Balanced Processing is used by a merchants to simply charge buyers for
items they sell directly.


Client Libraries
----------------

Balanced attempts very hard to write idiomatic code for all it's API libraries
and we pride ourselves in an extensive test suite for every client that
demonstrates almost every single method / function executed for your
convenience.

We find that this is the best way to use the client libraries. If you encounter
and issue, please file a github issue and get in touch through one our
many :ref:`support channels <support>`.

.. list-table:: API Libraries
   :widths: 10 20 20 15
   :header-rows: 1

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
   * - java
     - `balanced-java`_
     - `balanced-java tests`_
     - Balanced
   * - perl
     - `Business-BalancedPayments`_
     - `Business-BalancedPayments tests`_
     - `Crowdtilt.com`_


.. _balanced-php: https://github.com/balanced/balanced-php
.. _balanced-php tests: https://github.com/balanced/balanced-php/tree/master/tests

.. _balanced-python: https://github.com/balanced/balanced-python
.. _balanced-python tests: https://github.com/balanced/balanced-python/tree/master/tests

.. _balanced-ruby: https://github.com/balanced/balanced-ruby
.. _balanced-ruby tests: https://github.com/balanced/balanced-ruby/tree/master/spec

.. _balanced-java: https://github.com/balanced/balanced-java
.. _balanced-java tests: https://github.com/balanced/balanced-java/tree/master/src/test

.. _Business-BalancedPayments: https://github.com/Crowdtilt/Business-BalancedPayments
.. _Business-BalancedPayments tests: https://github.com/Crowdtilt/Business-BalancedPayments/tree/master/t

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
.. _mitigate the risks of running a marketplace: https://github.com/whit537/www.gittip.com/issues/67
.. _payments infrastructure: https://github.com/whit537/www.gittip.com/pull/137
.. _visual design: https://github.com/whit537/www.gittip.com/issues/66#issuecomment-7439689
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
