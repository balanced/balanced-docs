.. _getting_started:

Getting Started
===============

Balanced.js
-----------

``balanced.js`` is essential in ensuring that you're PCI compliant. Sensitive
data never touches your servers and as a result, the burden of PCI compliance
shifts to Balanced, which is `PCI-DSS Level 1 Compliant`_.

.. container::

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

.. container::

  Including ``balanced.js``

  .. code-block:: html

    <script type="text/javascript" src="https://js.balancedpayments.com/v1/balanced.js"></script>

.. _getting_started.initializing_balanced_js:

.. container::

  Initializing ``balanced.js``

  In a separate script tag, after you've
  :ref:`included balanced.js <getting_started.including_balanced_js>`,
  set your marketplace uri. This essentially acts as your public key and it's
  OK to freely share this with anyone.

  .. code-block:: html

     <script type="text/javascript">
         balanced.init('${REPLACE_THIS_WITH_YOUR_MARKETPLACE_URI}');
     </script>

  Example:

  .. code-block:: html

     <script type="text/javascript">
         balanced.init('/v1/marketplaces/TEST-MP5JtbXVDZkSGruOJyNasPqy');
     </script>

  You can find your API key secret and marketplace URI from your
  `dashboard <https://dashboard.balancedpayments.com/>`_.

.. _getting_started.collecting_card_info:

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
   Balanced will return a persistence-safe token, the ``uri``, representing
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

   .. _getting_started.callback:

   The second parameter just did a dummy ``alert()`` for demonstration purposes,
   but this function is actually the most important piece of the integration.

   It is your Balanced response handler. It takes one parameter that
   has three (3) properties which you can use to drive the interaction
   with Balanced:


   .. cssclass:: dl-horizontal

     ``data``
        | An object representing a tokenized resource (card or bank account).
     ``error``
        | Details of the error, if any.
     ``status``
        | The HTTP response code of the tokenization operation.

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

      balanced.card.create(creditCardData, callbackHandler);

.. clear::

.. _getting_started.charging_cards:

Charge a credit card
--------------------

Ok, so you've got the card token, referred to as the ``uri`` of the returned Card
resource.

Let's charge the card:

1. First, let's create a customer to which we can associate a card:

   .. dcode:: scenario customer_create

2. Associate the token with the customer:

   .. dcode:: scenario customer_add_card

3. Debit the customer:

   .. dcode:: scenario customer_create_debit

.. clear::
  :class: mb-large

.. note::
   :header_class: alert alert-tab
   :body_class: alert alert-gray

   Balanced does NOT take its fees from your charges, instead it instruments
   all operations that have occurred on the API and later invoices you. Read
   :ref:`more about fees <invoicing.fees>`.

.. _getting_started.collecting_bank_info:

Collect bank account info
-------------------------

.. container:: mb-large

  .. container:: header3

    Functional final result of tutorial:

    .. container:: span8

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

      var $form = $('#bank-account-form');
      var bankAccountData = {
          name: $form.find('.ba-name').val(),
          account_number: $form.find('.ba-an').val(),
          bank_code: $form.find('.ba-rn').val(),
          type: $form.find('select').val()
      };

2. Invoke the :js:func:`balanced.bankAccount.create` function with the collected information.
   Balanced will return a persistence-safe token, the ``uri``, representing
   the resource.

   Here's an example, demonstrating this:

   .. code-block:: javascript

     balanced.bankAccount.create(bankAccountData, function(response) {
       console.log(response.status);
       /*
         response.data:
           Contains the body of the bank account resource, which you can find
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
        | An object representing a tokenized resource (card or bank account).
     ``error``
        | Details of the error, if any.
     ``status``
        | The HTTP response code of the tokenization operation.

   Here's a skeleton callback function that we can use to get started:

   .. code-block:: javascript

       function callbackHandler(response) {
          switch (response.status) {
            case 201:
                // WOO HOO! MONEY!
                // response.data.uri == URI of the bank account resource you
                // should store this bank account URI to later credit it
                console.log(response.data);
                var $form = $("#bank-account-form");
                // the uri is an opaque token referencing the tokenized bank account
                var bank_account_uri = response.data['uri'];
                // append the token as a hidden field to submit to the server
                $('<input>').attr({
                   type: 'hidden',
                   value: bank_account_uri,
                   name: 'balancedBankAccountURI'
                }).appendTo($form);
                $form.attr({action: requestBinURL});
                $form.get(0).submit();
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

        var $form = $('#bank-account-form');
        var bankAccountData = {
            name: $form.find('.ba-name').val(),
            account_number: $form.find('.ba-an').val(),
            bank_code: $form.find('.ba-rn').val(),
            type: $form.find('select').val()
        };

        balanced.bankAccount.create(bankAccountData, responseCallbackHandler);

.. _getting_started.credit_bank_account:

Credit a bank account
---------------------

After collecting the bank account information via balanced.js, you'll have
the bank account token, referred to as the ``uri`` of the returned BankAccount
resource.

Let's issue a credit to this bank account:

1. First, create a customer to which the bank account can be associated:

   .. dcode:: scenario customer_create

2. Associate the token with the customer:

   .. dcode:: scenario customer_add_bank_account

3. Credit the customer:

   .. dcode:: scenario customer_credit

.. clear::
  :class: mb-large

.. note::
   :header_class: alert alert-tab
   :body_class: alert alert-gray

   For simplicity, Balanced does NOT take its fees from any of your
   operations, instead it meters your API usage and invoices you nightly.
   Read :ref:`more about fees <invoicing.fees>`.

.. note::
   :header_class: alert alert-tab
   :body_class: alert alert-gray

   Please note that for American Express cards it is mandatory to collect 
   the zip-code or the transaction will fail. 

.. _getting_started.balanced.js_cards:

Balanced.js Card Reference
--------------------------

.. js:function:: balanced.card.create(cardDataObject, callback)

  Sends the data stored in the ``cardDataObject`` to Balanced's servers for
  tokenization.

  :param cardDataObject.card_number: *required*.  The credit card number
  :param cardDataObject.expiration_month: *required*. The credit card's expiration month in the format of MM
  :param cardDataObject.expiration_year: *required*. The credit card's expiration year in the format of YYYY
  :param cardDataObject.security_code: *optional*. The credit card's security code
  :param cardDataObject.name: *optional*. The credit card holder's name
  :param cardDataObject.postal_code: *optional*. The credit card's billing postal code (zip code in the USA)
  :returns: ``null``. Invokes the ``callback`` function with three parameters -
            ``data``, ``errors`` and ``status``. If successful, the ``data``
            parameter has a resource representation which can be identified by
            its ``uri``

.. js:function:: balanced.card.isCardNumberValid(cardNumber)

  Validates a card number by checking if it's formatted correctly and
  passes the standard `Luhn check`_. All whitespace and non-numeric data is
  stripped for convenience.

  :param cardNumber: the card number to Luhn validate.
  :returns: ``true`` if the card number matches `Luhn check`_, ``false`` otherwise.

  Example:

  .. code-block:: javascript

    balanced.card.isCardNumberValid('4111111111111111');       // true
    balanced.card.isCardNumberValid('4111 1111 1111 1111');    // true
    balanced.card.isCardNumberValid('4111-1111-1111-1111');    // true
    balanced.card.isCardNumberValid('42123');                  // false

.. js:function:: balanced.card.cardType(cardNumber)

  Returns the card brand, calculated from the card number. If the card brand can
  NOT be determined, it will return ``null``.

  :param cardNumber: the card number to determine the brand for.
  :returns: ``Mastercard``, ``American Express``, ``VISA``, ``Discover Card``, or ``null``

  Example:

  .. code-block:: javascript

    balanced.card.cardType('5105105105105100');   // Mastercard
    balanced.card.cardType('4111111111111111');   // VISA
    balanced.card.cardType('341111111111111');    // American Express
    balanced.card.cardType(0)                     // null

.. js:function:: balanced.card.isSecurityCodeValid(cardNumber, securityCode)

  Checks whether or not the supplied number could be a valid card security code
  for the supplied card number.

  :param cardNumber: the card number to determine the validate the security code for.
  :param securityCode: the security number to validate
  :returns: ``true`` if the csc is valid for the card number provided, ``false`` otherwise.

  Example:

  .. code-block:: javascript

    balanced.card.isSecurityCodeValid('4111111111111111', 999)   // true
    balanced.card.isSecurityCodeValid('4111111111111111', 9999)  // false

.. js:function:: balanced.card.isExpiryValid(expirationMonth, expirationYear)

  Returns true if ``expirationMonth`` and ``expirationYear`` correspond to
  a date in the future.

  :param expirationMonth: the expiration month to validate
  :param expirationYear: the expiration year to validate
  :returns: ``true`` if the expiration date is in the future, ``false`` otherwise.

  Example:

  .. code-block:: javascript

    balanced.card.isExpiryValid('01', '2020');    // true
    balanced.card.isExpiryValid(1, 2010);         // false


.. js:function:: balanced.card.validate(cardDataObject)

  Performs a suite of checks on the submitted credit card data and returns
  a dictionary of errors. Will return an empty dictionary if there are no
  errors.

  :param cardDataObject.card_number: the card number to validate
  :param cardDataObject.security_code: the security code to validate
  :param cardDataObject.expiration_month: the expiration month to validate
  :param cardDataObject.expiration_year: the expiration year to validate
  :returns: ``{}`` if all fields are valid, else a dictionary of errors otherwise.

  Example:

  .. code-block:: javascript

    balanced.card.validate({
       card_number:'4111111111111111',
       expiration_month:1,
       expiration_year:2000,
       security_code:123
    });

  Will return:

  .. code-block:: javascript

    {expiration: '"1-2000" is not a valid credit card expiration date'}


.. _getting_started.balanced.js_bank_accounts:

Balanced.js BankAccount Reference
----------------------------------

.. js:function:: balanced.bankAccount.validateRoutingNumber(routingNumber)

  Validates a USA based bank routing number using the `MICR Routing Number Format`_.

  :param routingNumber: a 9 digit routing number, it may have a leading zero!
  :returns: ``true`` if the routing number check digit matches, ``false`` otherwise.

  .. warning::
     :header_class: alert alert-tab
     :body_class: alert alert-gray

     The success of this method does not guarantee that the
     routing number is valid, only that it falls within a valid range.

  Example:

  .. code-block:: javascript

    balanced.bankAccount.validateRoutingNumber('321174851') // passes
    balanced.bankAccount.validateRoutingNumber('021000021') // passes
    balanced.bankAccount.validateRoutingNumber('123457890') // fails


.. js:function:: balanced.bankAccount.validate(bankAccountDataObject)

  Performs a suite of checks on the submitted bank account data and
  returns a dictionary of errors. Will return an empty dictionary if there
  are no errors.

  :param bankAccountDataObject.bank_code: The bank routing number to validate
  :param bankAccountDataObject.account_number: the account number to perform a sanity check on
  :param bankAccountDataObject.name: the name on the bank account to perform a sanity check on
  :returns: ``{}`` if all fields are valid, else a dictionary of errors otherwise.

  .. warning::
     :header_class: alert alert-tab
     :body_class: alert alert-gray

     Account numbers can not be validated in real time. More on
     :ref:`reducing payout delays <best_practices.reducing-payout-delays>`.

  Example:

  .. code-block:: javascript

    balanced.bankAccount.validate({
       bank_code:'321174851',
       account_number:'09877765432111111',
       name:'Tommy Q. CopyPasta'
    })


.. _quirksmode: http://www.quirksmode.org/js/placejs.html
.. _full example page: https://gist.github.com/2662770
.. _LUHN check: http://en.wikipedia.org/wiki/Luhn_algorithm
.. _MICR Routing Number Format: http://en.wikipedia.org/wiki/Routing_transit_number#MICR_Routing_number_format
.. _jQuery: http://www.jquery.com
.. _jsFiddle: http://jsfiddle.net/
.. _jsFiddle [tokenize bank accounts]: http://jsfiddle.net/mahmoudimus/DGDkt/11/
.. _jsFiddle [tokenize credit cards]: http://jsfiddle.net/mjallday/BtXfr/
.. _PCI-DSS Level 1 Compliant: http://www.visa.com/splisting/searchGrsp.do?companyNameCriteria=Pound%20Payments
