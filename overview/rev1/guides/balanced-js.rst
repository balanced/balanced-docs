balanced.js
==================

Using ``balanced.js`` is essential in ensuring that you're PCI compliant.
When using balanced.js, sensitive data never touches your servers. As a result,
the burden of PCI compliance shifts to Balanced,
which is `PCI-DSS Level 1 Compliant`_.

.. note::
   :header_class: alert alert-tab
   :body_class: alert alert-green

   Throughout this guide we'll be referencing this `jsFiddle example`_.
   For the sake of brevity, we'll also use `jQuery`_, but note that balanced.js
   itself doesn't rely on any Javascript framework.


Migrating from v1.0
-----------------------

A few notable changes have occurred between v1.0 and v1.1 in terms of operation.

.. cssclass:: list-noindent

  - \- Credit cards and bank accounts (funding instruments) are now tokenized at the root level
    (``/cards`` and ``/bank_accounts``) and no longer under marketplaces. As such, tokenizations
    will no longer appear in Dashboard logs.

  - \- balanced.js no longer requires an init with the marketplace URI.

  - \- Tokenized funding instruments are "claimed" by executing an authenticated request on them
    such as associating them to a ``Customer`` or a simple fetch (GET).

  - \- Unclaimed tokenized funding instruments are discarded after a short timeframe.


.. _balanced-js.include:

Including balanced.js
-----------------------

.. note::
  :header_class: alert alert-tab-yellow
  :body_class: alert alert-yellow

  This may not work on very old browsers. For more information on how to
  support older browsers, `quirksmode`_ provides a tutorial on how to get
  javascript ``<script>`` includes to play nicely.

Begin by including balanced.js in your application.

.. code-block:: html

  <script type="text/javascript" src="https://js.balancedpayments.com/1.1/balanced.js"></script>

.. note::
  :header_class: alert alert-tab-red
  :body_class: alert alert-red

  Balanced recommends against locally hosting versions of balanced.js as this limits the
  deliverability of important fixes.


.. _balanced-js.collecting-card-info:

Collecting credit card information
----------------------------------

Before we can collect credit card information, we need a place where users can
enter it in, a form. The example below is extracted from this
`jsFiddle example`_.


.. code-block:: html

  <form role="form">
    <div>
      <label>Name on Card</label>
      <input type="text" id="cc-name" autocomplete="off" placeholder="John Doe" />
    </div>
    <div>
      <label>Card Number</label>
      <input type="text" id="cc-number" autocomplete="off" placeholder="4111111111111111" maxlength="16" />
    </div>
    <div>
      <label>Expiration</label>
      <input type="text" id="cc-ex-month" autocomplete="off" placeholder="01" maxlength="2" />
      <input type="text" id="cc-ex-year" autocomplete="off" placeholder="2013" maxlength="4" />
    </div>
    <div>
      <label>Card Verification Code (CVV)</label>
      <input type="text" id="ex-cvv" autocomplete="off" placeholder="453" maxlength="4" />
    </div>
    <div>
      <label>Postal Code</label>
      <input type="text" id="ex-postal-code" autocomplete="off" placeholder="453" />
    </div>

    <a id="cc-submit">Tokenize</a>
  </form>


Now let's define our `callback`_, the block of code we want to execute after
having received a response for our tokenization request to the Balanced API.
If desired, this can be the same method as the one handling bank account 
creation request responses. Just add some checking to see what kind of response
was returned, e.g check for a ``cards`` or ``bank_accounts`` key.

.. code-block:: javascript

  function handleResponse(response) {
    if (response.status_code === 201) {
      var fundingInstrument = response.cards != null ? response.cards[0] : response.bank_accounts[0];
      // Call your backend
      jQuery.post("/path/to/your/backend", {
        uri: fundingInstrument.href
      }, function(r) {
        // Check your backend response
        if (r.status === 201) {
          // Your successful logic here from backend ruby
        } else {
        // Your failure logic here from backend ruby
        }
      });
    } else {
      // Failed to tokenize, your error logic here
    }
  }


Now register a click event for the submit button. This is where we will place
our form field values into a payload object and submit it to the Balanced API.

.. code-block:: javascript

  $('#cc-submit').click(function (e) {
    e.preventDefault();

    var payload = {
      name: $('#cc-name').val(),
      number: $('#cc-number').val(),
      expiration_month: $('#cc-ex-month').val(),
      expiration_year: $('#cc-ex-year').val(),
      cvv: $('#ex-cvv').val(),
      address: {
        postal_code: $('#ex-postal-code').val()
      }
    };

    // Create credit card
    balanced.card.create(payload, handleResponse);
  });


.. _balanced-js.collecting-bank-account-info:

Collecting bank account information
-------------------------------------

Before we can collect bank account information, we need a place where users can
enter it in, a form. The example below is extracted from this
`jsFiddle example`_.


.. code-block:: html

  <form role="form">
    <div>
      <label>Account Holder's Name</label>
      <input type="text" id="ba-name" autocomplete="off" placeholder="John Doe" />
    </div>
    <div>
      <label>Routing Number</label>
      <input type="text" id="ba-routing" autocomplete="off" placeholder="322271627" />
    </div>
    <div>
      <label>Account Number</label>
      <input type="text" id="ba-number" autocomplete="off" placeholder="9900000000" />
    </div>
    <a id="ba-submit">Tokenize</a>
  </form>


Now let's define our `callback`_, the block of code we want to execute after
having received a response for our bank account creation request to the
Balanced API. If desired, this can be the same method as the one handling card 
creation request responses. Just add some checking to see what kind of response
was returned, e.g check for a ``cards`` or ``bank_accounts`` key.

.. code-block:: javascript

  function handleResponse(response) {
    if (response.status_code === 201) {
      var fundingInstrument = response.cards != null ? response.cards[0] : response.bank_accounts[0];
      // Call your backend
      jQuery.post("/path/to/your/backend", {
        uri: fundingInstrument.href
      }, function(r) {
        // Check your backend response
        if (r.status === 201) {
          // Your successful logic here from backend ruby
        } else {
        // Your failure logic here from backend ruby
        }
      });
    } else {
      // Failed to tokenize, your error logic here
    }
  }


Now register a click event for the submit button. This is where we will place
our form field values into a payload object and submit it to the Balanced API.

.. code-block:: javascript

  $('#ba-submit').click(function (e) {
    e.preventDefault();

    var payload = {
      name: $('#ba-name').val(),
      routing_number: $('#ba-routing').val(),
      account_number: $('#ba-number').val()
    };

    // Create bank account
    balanced.bankAccount.create(payload, handleResponse);
  });


Handling Input Validation
--------------------------

When calling ``balanced.card.create``, the supplied payload will be validated
before it is sent to Balanced. For more extensive information on validating
input values, read the sections below.


Checkpoint
-----------

You should understand how to do following:

- ✓ Include balanced.js in your application
- ✓ Initialize balanced.js with a server address and revision number
- ✓ Build an input form(s) for collecting credit card and/or bank account information
- ✓ Create a response callback handler
- ✓ Register a click event for the form submit button that assembles the form values into a payload attempts to create a card. 



Method Reference - Cards
--------------------------

.. js:function:: balanced.card.create(cardDataObject, callback)

  Sends the data stored in the ``cardDataObject`` to Balanced's servers for
  tokenization.

  :param cardDataObject.expiration_month: *required*. The credit card's expiration month in the format of MM
  :param cardDataObject.expiration_year: *required*. The credit card's expiration year in the format of YYYY
  :param cardDataObject.number: *required*. The credit card number
  :param cardDataObject.address: *optional*. An object containing the credit card's address information
  :param cardDataObject.cvv: *optional*. The credit card's security code
  :param cardDataObject.name: *optional*. The credit card holder's name
  
  :returns: ``null``. Invokes the ``callback`` function with a response payload for the
            result of the tokenization.

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

.. js:function:: balanced.card.isCVVValid(cardNumber, cvv)

  Checks whether or not the supplied number could be a valid card security code
  for the supplied card number.

  :param cardNumber: the card number to determine the validate the security code for.
  :param cvv: the security number to validate
  :returns: ``true`` if the csc is valid for the card number provided, ``false`` otherwise.

  Example:

  .. code-block:: javascript

    balanced.card.isCVVValid('4111111111111111', '999')   // true
    balanced.card.isCVVValid('4111111111111111', '9999')  // false

.. js:function:: balanced.card.isExpiryValid(expirationMonth, expirationYear)

  Returns true if ``expirationMonth`` and ``expirationYear`` correspond to
  a date in the future.

  :param expirationMonth: the expiration month to validate
  :param expirationYear: the expiration year to validate
  :returns: ``true`` if the expiration date is in the future, ``false`` otherwise.

  Example:

  .. code-block:: javascript

    balanced.card.isExpiryValid('01', '2020');    // true
    balanced.card.isExpiryValid('01', '2010');     // false


.. js:function:: balanced.card.validate(cardDataObject)

  Performs a suite of checks on the submitted credit card data and returns
  a dictionary of errors. Will return an empty dictionary if there are no
  errors.

  :param cardDataObject.number: the card number to validate
  :param cardDataObject.cvv: the security code to validate
  :param cardDataObject.expiration_month: the expiration month to validate
  :param cardDataObject.expiration_year: the expiration year to validate
  :returns: ``{}`` if all fields are valid, else a dictionary of errors otherwise.

  Valid input example:
  
  .. code-block:: javascript

    balanced.card.validate({
       number:'4111111111111111',
       expiration_month:'1',
       expiration_year:'2020',
       cvv:123
    });

  Will return:

  .. code-block:: javascript
  
    {
        "cards": [
            {
                "href": "/cards/CCEfgqHgYfUYoa5CepaiBo6",
                "id": "CCEfgqHgYfUYoa5CepaiBo6",
                "links": {}
            }
        ],
        "links": {},
        "status_code": 201
    }
  
  
  Invalid input example:

  .. code-block:: javascript

    balanced.card.validate({
       number:'4111111111111111',
       expiration_month:'1',
       expiration_year:'2000',
       cvv:123,
       name:'John Doe'
    });

  Will return:

  .. code-block:: javascript

    {
        "errors": [
            {
                "description": "Invalid field [expiration_month,expiration_year] - \"1-2000\" is not a valid credit card expiration date",
                "extras": {
                    "expiration_month": "Invalid field [expiration_month,expiration_year] - \"1-2000\" is not a valid credit card expiration date",
                    "expiration_year": "Invalid field [expiration_month,expiration_year] - \"1-2000\" is not a valid credit card expiration date"
                },
                "status": "Bad Request",
                "category_code": "request",
                "additional": null,
                "status_code": 400,
                "category_type": "request"
            }
        ]
    }


Method Reference - Bank Accounts
----------------------------------

.. js:function:: balanced.bankAccount.isRoutingNumberValid(routingNumber)

  Validates a USA based bank routing number using the `MICR Routing Number Format`_.

  :param routingNumber: a 9 digit routing number, it may have a leading zero!
  :returns: ``true`` if the routing number check digit matches, ``false`` otherwise.

  .. warning::
     :header_class: alert alert-tab-yellow
     :body_class: alert alert-yellow

     The success of this method does not guarantee that the
     routing number is valid, only that it falls within a valid range.

  Example:

  .. code-block:: javascript

    balanced.bankAccount.isRoutingNumberValid('321174851') // passes
    balanced.bankAccount.isRoutingNumberValid('021000021') // passes
    balanced.bankAccount.isRoutingNumberValid('123457890') // fails


.. js:function:: balanced.bankAccount.validate(bankAccountDataObject)

  Performs a suite of checks on the submitted bank account data and
  returns a dictionary of errors. Will return an empty dictionary if there
  are no errors.

  :param bankAccountDataObject.routing_number: *required*. The bank routing number to validate
  :param bankAccountDataObject.account_number: *required*. The account number to perform a sanity check on
  :param bankAccountDataObject.name: *optional*. The name on the bank account to perform a sanity check on
  :param bankAccountDataObject.type: *optional*. The name on the bank account to perform a sanity check on
  :returns: ``{}`` if all fields are valid, else a dictionary of errors otherwise.

  .. warning::
     :header_class: alert alert-tab-yellow
     :body_class: alert alert-yellow

     Account numbers can not be validated in real time. More on
     :ref:`reducing payout delays <best_practices.reducing-payout-delays>`.

  Valid input example:

  .. code-block:: javascript

    balanced.bankAccount.validate({
       bank_code:'321174851',
       account_number:'9900000000',
       name:'John Doe'
    })

  Will return:
  
  .. code-block:: javascript
  
    {
        "bank_accounts": [
            {
                "href": "/bank_accounts/BA3J3ukgOKmvVCCPl6ElwWea",
                "id": "BA3J3ukgOKmvVCCPl6ElwWea",
                "links": {}
            }
        ],
        "links": {},
        "status_code": 201
    }
  
  Invalid input example:

  .. code-block:: javascript

    balanced.bankAccount.validate({
       bank_code:'32117485',
       account_number:'9900000000',
       name:'John Doe'
    })

  Will return:
  
  .. code-block:: javascript
  
    {
        "errors": [
            {
                "description": "Invalid field [routing_number] - \"32117485\" is not a valid routing number",
                "extras": {
                    "routing_number": "Invalid field [routing_number] - \"32117485\" is not a valid routing number"
                },
                "status": "Bad Request",
                "category_code": "request",
                "additional": null,
                "status_code": 400,
                "category_type": "request"
            }
        ]
    }


.. _jsFiddle example: http://jsfiddle.net/balanced/an5Cz/
.. _jsFiddle [tokenize credit cards]: http://jsfiddle.net/balanced/an5Cz/
.. _PCI-DSS Level 1 Compliant: http://www.visa.com/splisting/searchGrsp.do?companyNameCriteria=Balanced
.. _quirksmode: http://www.quirksmode.org/js/placejs.html
.. _jQuery: http://www.jquery.com
.. _callback: https://en.wikipedia.org/wiki/Callback_(computer_programming)
.. _LUHN check: http://en.wikipedia.org/wiki/Luhn_algorithm
.. _MICR Routing Number Format: http://en.wikipedia.org/wiki/Routing_transit_number#MICR_Routing_number_format