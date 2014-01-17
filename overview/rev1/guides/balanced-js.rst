Using balanced.js
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


.. _balanced-js.include:

Including balanced.js
-----------------------

.. note::
  :header_class: alert alert-tab-yellow
  :body_class: alert alert-yellow

  This may not work on very old browsers. For more information on how to
  support older browsers, `quirksmode`_ provides a tutorial on how to get
  javascript ``<script>`` includes to play nicely.

.. code-block:: html

  <script type="text/javascript" src="https://js.balancedpayments.com/1.1/balanced.js"></script>


.. _balanced-js.initialize:

Initialize balanced.js
--------------------------

balanced.js needs to be initialized with the address of the Balanced API server
to which it should connect, as well as the revision of the API to use, in this
case, https://api.balancedpayments.com, and revision 1.1.

.. code-block:: html

  <script type="text/javascript">
    $(document).ready(function () {
      balanced.init({
        server: 'https://api.balancedpayments.com',
        revision: 1.1
      });
    });
  </script>


.. _balanced-js.collecting-card-info:

Collecting credit card information
----------------------------------

Before we can collect credit card information, we need a place where users can
ender it in, a form. The example below is extracted this `jsFiddle example`_.


.. code-block:: html

  <form role="form" class="form-horizontal">
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
      <label>Security Code (CVV)</label>
      <input type="text" id="ex-csc" autocomplete="off" placeholder="453" maxlength="4" />
    </div>
    <a id="cc-submit">Tokenize</a>
  </form>


Now let's define our `callback`_, the block of code we want to execute after
having received a response for our tokenization request to the Balanced API.

.. code-block:: javascript

  function handleResponse(response) {
    if (response.status === 201 && response.href) {
      // Successful tokenization
      // Call your backend
      jQuery.post("/path/to/your/backend", {
        uri: response.href
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
      security_code: $('#ex-csc').val()
    };

    // Tokenize credit card
    balanced.card.create(payload, handleResponse);
  });
















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



.. _jsFiddle example: http://jsfiddle.net/balanced/an5Cz/
.. _jsFiddle [tokenize credit cards]: http://jsfiddle.net/balanced/an5Cz/
.. _PCI-DSS Level 1 Compliant: http://www.visa.com/splisting/searchGrsp.do?companyNameCriteria=Balanced
.. _quirksmode: http://www.quirksmode.org/js/placejs.html
.. _jQuery: http://www.jquery.com
.. _callback: https://en.wikipedia.org/wiki/Callback_(computer_programming)