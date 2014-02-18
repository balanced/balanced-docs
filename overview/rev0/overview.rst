Overview
========

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

     :ref:`Test bank account numbers <resources.test-credit-cards>`

   .. icon-box-widget::
     :box-classes: box box-block box-purple
     :icon-classes: icon icon-page

     :ref:`Test bank account numbers <resources.test-bank-accounts>`

.. clear::

.. _overview.use_cases:

|

|

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


Third-Party Plugins
------------------------

.. container:: section

  .. container:: header3

    Shopping Carts

  .. cssclass:: list-noindent

    - `Drupal Commerce <https://drupal.org/project/commerce_balanced_payments>`_
    - `WordPress <https://github.com/pmgarman/wp-balanced-payments>`_
    - `Easy Digital Downloads <https://easydigitaldownloads.com/extensions/balanced-payment-gateway/>`_
    - `Cart66 <http://cart66.com/cloud/payment-gateways/>`_
    - `Mijreh <http://www.mijireh.com/docs/payment-gateways/>`_
    - `Spree <http://guides.spreecommerce.com/developer/payments.html#supported-gateways>`_


.. container:: section

  .. container:: header3

    Frameworks

  .. cssclass:: list-noindent

    - `Meteor.js Package <https://github.com/ianserlin/meteor-balanced-payments>`_
    - `ActiveMerchant <https://github.com/Shopify/active_merchant#supported-direct-payment-gateways>`_


.. container:: section

  .. container:: header3

    Recurring Payments

  .. cssclass:: list-noindent

    - `Chargebee <http://www.chargebee.com/partners.html>`_


.. container:: section

  .. container:: header3

    Gateways

  .. cssclass:: list-noindent

    - `Spreedly <https://core.spreedly.com/manual/payment-gateways/balanced>`_
    - `Crowdtilt API/Crowdhoster - (Crowdfunding specific) <https://github.com/Crowdtilt/crowdtilt-api-spec/>`_


.. container:: section

  .. container:: header3

    Card Readers

  .. cssclass:: list-noindent

    - `Cardflight <https://getcardflight.com/>`_


.. container:: section

  .. container:: header3

    Accounting

  .. cssclass:: list-noindent

    .. image:: //static/img/logos/subledger.png
      :target: http://subledger.com/blog/rent-my-bikes-demo/


Integration Assistance
-----------------------

Are you looking for a developer to help with Balanced integration? Check out these companies!

.. image:: //static/img/logos/workmob@2x.png
  :target: https://theworkmob.com/integrations/balancedpayments
  :height: 50px
  :width: 236px


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