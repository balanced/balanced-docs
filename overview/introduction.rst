Overview
========

.. container:: overview-large

  Balanced is a payments company dedicated to increasing the world's
  economic output. To do this, we've decided to work with online
  marketplaces and crowdfunding platforms to help them create new forms of commerce.
  We’ve built a white-labeled API and open sourced dashboard to help them
  do this. And while we really like working with marketplaces and
  crowdfunding platforms, Balanced can be used for e-commerce models of all types.

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


.. container:: integration

   .. container:: copy-box

      Start Integrating


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

   .. icon-box-widget::
     :box-classes: box box-block box-blue
     :icon-classes: icon icon-page

     :ref:`Collect bank account info <getting_started.collecting_bank_info>`

   .. icon-box-widget::
     :box-classes: box box-block box-blue
     :icon-classes: icon icon-page

     :ref:`Credit bank account <getting_started.credit_bank_account>`


.. container:: span6

   .. container:: header3

     Form Building

   .. icon-box-widget::
     :box-classes: box box-block box-turquoise
     :icon-classes: icon icon-page

     `Sample credit card form <#collecting-credit-card-information>`_

   .. icon-box-widget::
     :box-classes: box box-block box-turquoise
     :icon-classes: icon icon-page

     `Sample bank account form <#collect-bank-account-info>`_


.. container:: span6

   .. container:: header3

     Testing

   .. icon-box-widget::
     :box-classes: box box-block box-purple
     :icon-classes: icon icon-page

     `Test credit card numbers <#test-credit-card-numbers>`_

   .. icon-box-widget::
     :box-classes: box box-block box-purple
     :icon-classes: icon icon-page

     `Test bank account numbers <#test-bank-account-numbers>`_

.. clear::

.. _overview.use_cases:



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
   :widths: 15 17 18 15
   :header-rows: 1
   :class: table table-hover

   * - Language / Platform
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
..   * - node
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


Use Cases
---------

.. container:: header3 mb-ten

  Marketplaces

Balanced is most often used to power payments for online and mobile
marketplaces -- any platform facilitating payments between buyers and
sellers. For example, `kitchit`_, `copious`_, `zaarly`_, `visual.ly`_,
and many others are connecting Balanced Processing and Balanced Payouts
to charge a buyer’s credit card on behalf of a seller.

Some customers have even implemented a shopping cart checkout flow where
a single buyer can buy from many sellers with a single transaction. And
holding the funds with Balanced between Payouts and Processing can allow
the marketplace to implement an escrow-like functionality.

.. container:: header3 mb-ten

  Crowd-Funding

Balanced is commonly used to power payments for crowd-funding and group
purchasing platforms. For example, `crowdtilt`_, `wanderable`_,
`gittip`_, and many others are connecting Balanced Processing and
Balanced Payouts to charge many buyers’ credit cards on behalf of a
single seller.

.. container:: header3 mb-ten

  Vendor Payments

Balanced Payouts is used by many businesses that need to pay their
sellers or vendors for supplies and services rendered.

.. container:: header3 mb-ten

  E-Commerce

Balanced Processing is used by a merchants to simply charge buyers for
items they sell directly.

.. _overview.github_issues:

Github Discussions
------------------

We actively and publicly discuss feature requests and product decisions
with our community on `github`_. We’d love to hear from you.


.. _overview.support:

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


Certified Developers
--------------------

We've partnered with `WorkMob`_ -- a marketplace for custom API development
projects -- to help companies looking for assistance with their Balanced API
integration find a quality Balanced certified developer.

Create a project on `WorkMob`_ to get started:

.. image:: https://s3.amazonaws.com/theworkmob_partners/balanced.png
  :target: https://theworkmob.com/integrations/balancedpayments
  :width: 375

If you'd like to find a developer to help with your Balanced integration
outside of WorkMob, please post your criteria on `this Github issue`_.


Accounting
----------

`Subledger`_ is an API for in-application accounting.

`Subledger`_ makes it easy to:

* Produce financial reports for your finance team
* Manage accounts payable to sellers vs cash in escrow
* Maintain a financial audit trail for compliance reasons

Interested? You should definitely check out this `post`_ about how Balanced + Subledger can work together to do your payments and accounting. *#LoveAPIs*

.. image:: /static/img/subledger.png
   :target: http://subledger.com


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

.. _this Github issue: https://github.com/balanced/balanced-api/issues/315
.. _WorkMob: https://theworkmob.com/
.. _Subledger: http://subledger.com
.. _post: http://subledger.com/blog/rent-my-bikes-demo/
