Getting Started
================


Start Integrating
-------------------


.. container:: span6

   .. container:: header3

      Tutorials

   .. icon-box-widget::
     :box-classes: box box-block box-blue
     :icon-classes: icon icon-page

     :ref:`Quickstart <quickstart>`

   .. icon-box-widget::
     :box-classes: box box-block box-blue
     :icon-classes: icon icon-page

     :ref:`Working with Debits <guides.debits>`

   .. icon-box-widget::
     :box-classes: box box-block box-blue
     :icon-classes: icon icon-page

     :ref:`Working with Credits <guides.credits>`

   .. icon-box-widget::
     :box-classes: box box-block box-blue
     :icon-classes: icon icon-page

     :ref:`Working with Orders <guides.orders>`


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



Client Libraries
----------------------------

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

    .. image:: //static/images/logos/subledger.png
      :target: http://subledger.com/blog/rent-my-bikes-demo/


Integration Assistance
-----------------------

Are you looking for a developer to help with Balanced integration? Check out these companies!

.. cssclass:: logos-inline

  .. image:: //static/images/logos/workmob@2x.png
    :target: https://theworkmob.com/integrations/balancedpayments
    :height: 50px
    :width: 236px

  .. image:: //static/images/logos/airpair@2x.png
    :target: http://www.airpair.com/balanced-payments
    :height: 50px
    :width: 187px




.. _Crowdtilt.com:
.. _crowdtilt: http://crowdtilt.com
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