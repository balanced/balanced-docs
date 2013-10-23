Reference
=========

REST API
--------

Balanced.js
-----------

The balanced.js javascript library is used to securely tokenize debit/credit cards and bank account directly from the user's browser.
By using balanced.js to exchange sensitive information with Balanced directly from the user's browser, your application is never
passed sensitive credit card or bank information. This means you don't need to worry about PCI compliance issues.

balanced.card
`````````````

.. container:: balanced-js-card

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

balanced.bankAccount
````````````````````

.. container:: balanced-js-bank-account

  .. _getting_started.balanced.js_bank_accounts:

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

    :param bankAccountDataObject.routing_number: The bank routing number to validate
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
         routing_number:'321174851',
         account_number:'09877765432111111',
         name:'Tommy Q. CopyPasta'
      })


  .. _quirksmode: http://www.quirksmode.org/js/placejs.html
  .. _full example page: https://gist.github.com/2662770
  .. _LUHN check: http://en.wikipedia.org/wiki/Luhn_algorithm
  .. _MICR Routing Number Format: http://en.wikipedia.org/wiki/Routing_transit_number#MICR_Routing_number_format
  .. _jQuery: http://www.jquery.com
  .. _JSFiddle: http://jsfiddle.net/
  .. _JSFiddle - Tokenize bank accounts: http://jsfiddle.net/balanced/ZwhrA/
  .. _JSFiddle - Tokenize credit cards: http://jsfiddle.net/balanced/ZwhrA/
  .. _PCI-DSS Level 1 Compliant: http://www.visa.com/splisting/searchGrsp.do?companyNameCriteria=Pound%20Payments

iOS SDK
-------

Please see the `README on Github <https://github.com/balanced/balanced-ios>`_ for documentation for the iOS SDK.

Android SDK
-----------

Please see the `README on Github <https://github.com/balanced/balanced-android>`_ for documentation for the Android SDK.