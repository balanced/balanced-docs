.. _getting_started:

Getting Started
===============

Balanced.js
-----------

``balanced.js`` is essential in ensuring that you're PCI compliant. Sensitive
data never touches your servers and as a result, the burden of PCI compliance
shifts to Balanced, which is `PCI-DSS Level 1 Compliant`_.

.. container:: mb-large

  1. Use ``balanced.js`` to send sensitive information to Balanced
  2. Use the ``uri``, returned by Balanced, as the token representing
     the sensitive information
  3. Associate that token to a customer
  4. Debit that customer


We're putting this here as we're going to reference it in the :ref:`payouts`
and the :ref:`processing` tutorials.

Including and Initializing ``balanced.js``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::
  :header_class: alert alert-tab
  :body_class: alert alert-gray

  This may not work on very old browsers. For more information on how to
  support older browsers, `quirksmode`_ provides a tutorial on how to get
  javascript ``<script>`` includes to play nicely.

.. _getting_started.including_balanced_js:

.. container:: mb-large

  Including ``balanced.js``

  .. code-block:: html

    <script type="text/javascript" src="https://js.balancedpayments.com/v1/balanced.js"></script>

.. _getting_started.initializing_balanced_js:

.. container:: mb-large

  Initializing ``balanced.js``

  In a separate script tag, after you've
  :ref:`included balanced.js <getting_started.including_balanced_js>`,
  set your marketplace uri. This essentially acts as your public key and it's
  OK to freely share this with anyone.

  .. code-block:: html

     <script type="text/javascript">
         balanced.init('marketplaceUri');
     </script>


.. _getting_started.tokenizing_a_credit_card:

Collecting credit card information
----------------------------------

.. container:: mb-large

  .. container:: header3

    Functional final result of tutorial:

    .. container:: span7

      .. icon-box-widget::
        :box-classes: box box-block box-blue
        :icon-classes: icon icon-cloud

        `jsFiddle [tokenize credit cards]`_

.. clear::
  :class: mb-large

.. note::
   :header_class: alert alert-tab
   :body_class: alert alert-gray

   Throughout this tutorial, we're using `jQuery`_ for brevity, but
   ``balanced.js`` has no such dependency itself.

1. Collect all the information from your form:

   .. code-block:: javascript

    var $form = $('#credit-card-form');
    var creditCardData = {
        card_number: $form.find('.cc-number').val(),
        expiration_month: $form.find('.cc-em').val(),
        expiration_year: $form.find('.cc-ey').val(),
        security_code: $form.find('cc-csc').val()
     };

2. Invoke the :js:func:`balanced.card.create` function with the collected information.
   Balanced will return a persistance-safe token, the ``uri``, representing
   the resource.

   Here's an example, demonstrating this:

   .. code-block:: javascript

     balanced.card.create(creditCardData, function(response) {
       console.log(response.status);
       /*
         response.data:
           Contains the body of the card resource, which you can find
           in the API reference.

           This data is an object, i.e. hash, that can be identified by
           its uri field. You may store this uri in your data store (e.g.
           postgresql, mysql, mongodb, etc) since it's perfectly safe and
           can only be retrieved by your secret key.

           More on this in the API reference.
        */
       console.log(response.data);
     });

   The second parameter just did a dummy ``alert()`` for demonstration purposes,
   but this function is actually the most important piece of the integration.

   It is your Balanced response handler. It takes one parameter that
   has three (3) properties which you can use to drive the interaction
   with Balanced:

   .. cssclass:: dl-horizontal

   ``data``
      An object representing a tokenized resource (card or bank account).
   ``error``
      Details of the error, if any.
   ``status``
      The HTTP response code of the tokenization operation.

   Here's a skeleton callback function that we can use to get started:

   .. code-block:: javascript

       function callbackHandler(response) {
          switch (response.status) {
            case 201:
                // WOO HOO! MONEY!
                // response.data.uri == URI of the bank account resource you
                // can store this card URI in your database
                console.log(response.data);
                var $form = $("#credit-card-form");
                // the uri is an opaque token referencing the tokenized card
                var cardTokenURI = response.data['uri'];
                // append the token as a hidden field to submit to the server
                $('<input>').attr({
                   type: 'hidden',
                   value: cardTokenURI,
                   name: 'balancedCreditCardURI'
                }).appendTo($form);
                break;
            case 400:
                // missing field - check response.error for details
                console.log(response.error);
                break;
            case 402:
                // we couldn't authorize the buyer's credit card
                // check response.error for details
                console.log(response.error);
                break
            case 404:
                // your marketplace URI is incorrect
                console.log(response.error);
                break;
            case 500:
                // Balanced did something bad, please retry the request
                break;
          }
       }

   So, let's show that example on creating a card again, but this time with a
   proper callback handler:

   .. code-block:: javascript

      var $form = $('#credit-card-form');
      var creditCardData = {
           card_number: $form.find('.cc-number').val(),
           expiration_month: $form.find('.cc-em').val(),
           expiration_year: $form.find('.cc-ey').val(),
           security_code: $form.find('cc-csc').val()
       };

      balanced.card.create(cardData, callbackHandler);

.. clear::

.. begin-section:

Charge a credit card
--------------------

Ok, so you've got the card token, referred to as the ``uri`` of the returned Card
resource.

Let's charge the card:

1. First, let's create an account to associate the card tokexn with:

   .. dcode:: scenario account_create_buyer

2. Associate the token with an account:

   .. dcode:: scenario account_add_card

3. Debit the account:

   .. dcode:: scenario account_create_debit

.. note::
   :class: alert alert-info

   Balanced does NOT take its fees from your charges, instead it instruments
   all operations that have occurred on the API and later invoices you. Read
   :ref:`more about fees <overview.fees.balanced>`.


Collect bank account info
-------------------------

.. container:: mb-large

  .. container:: header3

    Functional final result of tutorial:

    .. container:: span7

      .. icon-box-widget::
        :box-classes: box box-block box-blue
        :icon-classes: icon icon-cloud

        `jsFiddle [tokenize bank accounts]`_

.. clear::
  :class: mb-large

.. note::
   :header_class: alert alert-tab
   :body_class: alert alert-gray

   Throughout this tutorial, we're using `jQuery`_ for brevity, but
   ``balanced.js`` has no such dependency itself.

1. Collect all the information from your form:

   .. code-block:: javascript

    var $form = $('#credit-card-form');
    var creditCardData = {
        card_number: $form.find('.cc-number').val(),
        expiration_month: $form.find('.cc-em').val(),
        expiration_year: $form.find('.cc-ey').val(),
        security_code: $form.find('cc-csc').val()
     };

2. Invoke the :js:func:`balanced.card.create` function with the collected information.
   Balanced will return a persistance-safe token, the ``uri``, representing
   the resource.

   Here's an example, demonstrating this:

   .. code-block:: javascript

     balanced.card.create(creditCardData, function(response) {
       console.log(response.status);
       /*
         response.data:
           Contains the body of the card resource, which you can find
           in the API reference.

           This data is an object, i.e. hash, that can be identified by
           its uri field. You may store this uri in your data store (e.g.
           postgresql, mysql, mongodb, etc) since it's perfectly safe and
           can only be retrieved by your secret key.

           More on this in the API reference.
        */
       console.log(response.data);
     });

   The second parameter just did a dummy ``alert()`` for demonstration purposes,
   but this function is actually the most important piece of the integration.

   It is your Balanced response handler. It takes one parameter that
   has three (3) properties which you can use to drive the interaction
   with Balanced:

   .. cssclass:: dl-horizontal

   ``data``
      An object representing a tokenized resource (card or bank account).
   ``error``
      Details of the error, if any.
   ``status``
      The HTTP response code of the tokenization operation.

   Here's a skeleton callback function that we can use to get started:

   .. code-block:: javascript

       function callbackHandler(response) {
          switch (response.status) {
            case 201:
                // WOO HOO! MONEY!
                // response.data.uri == URI of the bank account resource you
                // can store this card URI in your database
                console.log(response.data);
                var $form = $("#credit-card-form");
                // the uri is an opaque token referencing the tokenized card
                var cardTokenURI = response.data['uri'];
                // append the token as a hidden field to submit to the server
                $('<input>').attr({
                   type: 'hidden',
                   value: cardTokenURI,
                   name: 'balancedCreditCardURI'
                }).appendTo($form);
                break;
            case 400:
                // missing field - check response.error for details
                console.log(response.error);
                break;
            case 402:
                // we couldn't authorize the buyer's credit card
                // check response.error for details
                console.log(response.error);
                break
            case 404:
                // your marketplace URI is incorrect
                console.log(response.error);
                break;
            case 500:
                // Balanced did something bad, please retry the request
                break;
          }
       }

   So, let's show that example on creating a card again, but this time with a
   proper callback handler:

   .. code-block:: javascript

      var $form = $('#credit-card-form');
      var creditCardData = {
           card_number: $form.find('.cc-number').val(),
           expiration_month: $form.find('.cc-em').val(),
           expiration_year: $form.find('.cc-ey').val(),
           security_code: $form.find('cc-csc').val()
       };

      balanced.card.create(cardData, callbackHandler);

Credit a bank account
---------------------


Client-side Validation Helpers
------------------------------

.. js:function:: balanced.card.create(card_number, expiration_month, expiration_year, security_code)

  :param card_number: The credit card number
  :param expiration_month: The credit card's expiration month
  :param expiration_year: The credit card's expiration year
  :param security_code: The credit card's security code
  :returns: Your mom

.. _quirksmode: http://www.quirksmode.org/js/placejs.html
.. _full example page: https://gist.github.com/2662770
.. _LUHN check: http://en.wikipedia.org/wiki/Luhn_algorithm
.. _MICR Routing Number Format: http://en.wikipedia.org/wiki/Routing_transit_number#MICR_Routing_number_format
.. _jQuery: http://www.jquery.com
.. _jsFiddle: http://jsfiddle.net/
.. _jsFiddle [tokenize bank accounts]: http://jsfiddle.net/mahmoudimus/DGDkt/11/
.. _jsFiddle [tokenize credit cards]: http://jsfiddle.net/mjallday/BtXfr/
.. _PCI-DSS Level 1 Compliant: http://www.visa.com/splisting/searchGrsp.do?companyNameCriteria=Pound%20Payments
