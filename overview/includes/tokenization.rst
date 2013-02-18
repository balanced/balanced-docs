
.. _tokenization:

Tokenizing Sensitive Information
================================

Balanced provides a PCI-compliant javascript library, dubbed ``balanced.js``
which, when included on your website, enables secure collection of payment and
sensitive information without touching your servers, keeping you completely
outside of PCI and regulatory scope.


Getting Started
---------------

This getting started is a reference to ``balanced.js`` and for your convenience
we've built a `full example page`_ that's already put together for you. We're putting
this here as we're going to reference it in the :ref:`payouts` and the :ref:`processing`
tutorials.

Here's another `jsFiddle demo`_ that demonstrates bank account tokenization.

.. _tok.including:

Including
~~~~~~~~~

Securely collecting information has never been easier, just include the
following script on your page.

.. code-block:: html

  <script type="text/javascript" src="https://js.balancedpayments.com/v1/balanced.js"></script>

.. note::
  :class: alert alert-info

  This may not work on very old browsers. For more information on how to
  support older browsers, `quirksmode`_ provides a tutorial on how to get
  javascript ``<script>`` includes to play nicely.


.. _tok.init:

Initializing
~~~~~~~~~~~~

In a separate script tag, after you've :ref:`included balanced.js <tok.including>`,
set your marketplace uri. This essentially acts as your public key and it's
OK to freely share this with anyone.

.. code-block:: html

   <script type="text/javascript">
       balanced.init('marketplaceUri');
   </script>

OK, you're ready to rock and roll!

Create a Card
~~~~~~~~~~~~~

Creating a card is as easy as constructing a object with a card's details
and invoking the ``balanced.card.create`` function.

Here's an example:

.. code-block:: javascript

   var cardData = {
     "name": "Bernhard Riemann",                 // Optional
     "card_number": "4111 1111 1111 1111",
     "expiration_month": 4,
     "expiration_year": 2014,
   };


   balanced.card.create(cardData, function(response) {
     alert(response.status);
   });


That will actually hit Balanced's servers and if successful, will tokenize
a card for you. More on that later, but first, let's discuss how to handle
the returned results from Balanced.

.. _tok.callback:

The Callback
~~~~~~~~~~~~

The second parameter just did a dummy ``alert()`` for demonstration purposes,
but this function is actually the most important piece of the integration. It is
your Balanced response handler. It takes one parameter that has three (3)
properties which you can use to drive the interaction with Balanced:

-  ``data`` - An object representing a tokenized resource (card or bank account).
-  ``error`` - Details of the error, if any.
-  ``status`` - The HTTP response code of the tokenization operation.

Here's a skeleton callback function that we can use to get started:

.. code-block:: javascript

    function callbackHandler(response) {
       switch (response.status) {
           case 201:
               // WOO HOO!
               // response.data.uri == uri of the card or bank account resource
               break;
           case 400:
               // missing field - check response.error for details
               break;
           case 402:
               // we couldn't authorize the buyer's credit card
               // check response.error for details
               break
           case 404:
               // your marketplace URI is incorrect
               break;
           case 500:
               // Balanced did something bad, please retry the request
               break;
       }
    }

So, let's show that example on creating a card again, but this time with a
proper callback handler:

.. code-block:: javascript

   var cardData = {
     "name": "Bernhard Riemann",                 // Optional
     "card_number": "4111 1111 1111 1111",
     "expiration_month": 4,
     "expiration_year": 2014,
   };

   balanced.card.create(cardData, callbackHandler);


Create a Bank Account
~~~~~~~~~~~~~~~~~~~~~

Just like creating a card, creating a bank account is very simple - just build
up an object and invoke the ``balanced.bankAccount.create`` function.

Here's an example:

.. code-block:: javascript

   var bankAccountData = {
      "name": "Levain Bakery LLC",
      "account_number": "28304871049",
      "routing_number": "121042882"
   }

   balanced.bankAccount.create(bankAccountData, callbackHandler);

Notice that we used the same :ref:`callback handler <tok.callback>` as
tokenizing a card.

.. _tok.validators:

Client-side Validation Helpers
------------------------------

``balanced.js`` includes a number of helpers that can help verify both
credit card and bank account information. Using these helpers when building your
forms adds robustness, boosting your website's user experience and dramatically
reducing declinations.

Card Validation
~~~~~~~~~~~~~~~

Validates a card number by checking if it's formatted correctly and
passes the standard `Luhn check`_. All whitespace and non-numeric data is
stripped for convenience.

.. js:function:: balanced.card.isCardNumberValid(cardNumber)

   :param cardNumber: the card number to Luhn validate.
   :returns: ``true`` if the card number matches `Luhn check`_, ``false`` otherwise.

Example:

.. code-block:: javascript

   balanced.card.isCardNumberValid('4111111111111111');       // true
   balanced.card.isCardNumberValid('4111 1111 1111 1111');    // true
   balanced.card.isCardNumberValid('4111-1111-1111-1111');    // true
   balanced.card.isCardNumberValid('42123');                  // false


Determining Card Brand
~~~~~~~~~~~~~~~~~~~~~~

Returns the card brand, calculated from the card number. If the card brand can
NOT be determined, it will return ``null``.

.. js:function:: balanced.card.cardType(cardNumber)

   :param cardNumber: the card number to determine the brand for.
   :returns: ``Mastercard``, ``American Express``, ``VISA``, ``Discover Card``, or ``null``

Example:

.. code-block:: javascript

   balanced.card.cardType('5105105105105100');   // Mastercard
   balanced.card.cardType('4111111111111111');   // VISA
   balanced.card.cardType('341111111111111');    // American Express
   balanced.card.cardType(0)                     // null


Validating the Security Code (CSC)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Checks whether or not the supplied number could be a valid card security code
for the supplied card number.

.. js:function:: balanced.card.isSecurityCodeValid(cardNumber, securityCode)

   :param cardNumber: the card number to determine the validate the security code for.
   :param securityCode: the security number to validate
   :returns: ``true`` if the csc is valid for the card number provided, ``false`` otherwise.

Example:

.. code-block:: javascript


    balanced.card.isSecurityCodeValid('4111111111111111', 999)   // true
    balanced.card.isSecurityCodeValid('4111111111111111', 9999)  // false


Validating Card Expiration
~~~~~~~~~~~~~~~~~~~~~~~~~~

Returns true if ``expirationMonth`` and ``expirationYear`` correspond to
a date in the future.

.. js:function:: balanced.card.isExpiryValid(expirationMonth, expirationYear)

   :param expirationMonth: the expiration month to validate
   :param expirationYear: the expiration year to validate
   :returns: ``true`` if the expiration date is in the future, ``false`` otherwise.

Example:

.. code-block:: javascript

    balanced.card.isExpiryValid('01', '2020');    // true
    balanced.card.isExpiryValid(1, 2010);         // false


General Card Validation
~~~~~~~~~~~~~~~~~~~~~~~

Performs a suite of checks on the submitted credit card data and returns
a dictionary of errors. Will return an empty dictionary if there are no
errors.

.. js:function:: balanced.card.validate({card_number, security_code, expiration_month, expiration_year})

   :param card_number: the card number to validate
   :param security_code: the security code to validate
   :param expiration_month: the expiration month to validate
   :param expiration_year: the expiration year to validate
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

.. _tok.validators.banks:

Validate a Bank Account's Routing Number
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Validates a USA based bank routing number using the `MICR Routing Number
Format`_.

.. js:function:: balanced.bankAccount.validateRoutingNumber(routingNumber)

  :param routingNumber: a 9 digit routing number, can have a leading zero!
  :returns: ``true`` if the routing number check digit matches, ``false`` otherwise.

Example:

.. code-block:: javascript

    balanced.bankAccount.validateRoutingNumber('321174851') // passes
    balanced.bankAccount.validateRoutingNumber('021000021') // passes
    balanced.bankAccount.validateRoutingNumber('123457890') // fails

.. warning::
   :class: alert

   The success of this method does not guarantee that the
   routing number is valid, only that it falls within a valid range.


General Bank Account Validation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::
   :class: alert alert-warning

   Account numbers can not be validated in real time. More on
   :ref:`bank accounts best practices <payouts.best_practices>`.

Performs a suite of checks on the submitted bank account data and
returns a dictionary of errors. Will return an empty dictionary if there
are no errors.

.. js:function:: balanced.bankAccount.validate({bank_code, account_number, name})

   :param bank_code: the bank routing number to validate
   :param account_number: the account number to perform a sanity check on
   :param name: the name on the bank account to perform a sanity check on
   :returns: ``{}`` if all fields are valid, else a dictionary of errors otherwise.

Example:

.. code-block:: javascript

    balanced.bankAccount.validate({
        '321174851',
        '09877765432111111',
        'Tommy Q. CopyPasta'
    })

Forms
-----

For the purposes of various examples throughout this documentation,
we've provided you with two sample forms, one to collect card information
and one to collect bank account information.

We're also going to be using `jQuery`_ throughout the examples for brevity, but
but ``balanced.js`` has no such dependency itself.

Remember, you can always use the `full example page`_ that already puts all
of this together or can ask us to write a sample form for you through one
of our :ref:`support channels <support>`.

.. _tok.card.form:

Simple Card Form
~~~~~~~~~~~~~~~~

.. literalinclude:: includes/cc-form.html
   :language: html

.. _tok.bank_account.form:

Simple Bank Account Form
~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: includes/ba-form.html
   :language: html



.. _quirksmode: http://www.quirksmode.org/js/placejs.html
.. _full example page: https://gist.github.com/2662770
.. _LUHN check: http://en.wikipedia.org/wiki/Luhn_algorithm
.. _MICR Routing Number Format: http://en.wikipedia.org/wiki/Routing_transit_number#MICR_Routing_number_format
.. _jQuery: http://www.jquery.com
.. _jsFiddle demo: http://jsfiddle.net/mahmoudimus/DGDkt/11/
