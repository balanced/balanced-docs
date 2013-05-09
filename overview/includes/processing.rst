.. _processing:

Balanced Processing
===================

Balanced Processing provides a complete solution for accepting credit
card payments in a simple, secure manner, relieving you from the hassles of PCI
compliance.

Tutorial
--------

At a high level, we're going to implement the process for creating a charge.
Here's how we're going to accomplish this:

* Securely collecting credit card information with ``balanced.js``
* Securely submitting that information to Balanced
* Creating an account and charging your buyer


Collecting credit card information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::
   :class: alert alert-info

   We have a fully implemented `sample page`_ for you, that you can use to get
   started immediately. At any point during this tutorial you feel overwhelmed
   or you want help, please use any of the :ref:`support channels <support>` we
   have available.


Follow the steps for :ref:`including <tok.including>` and
:ref:`initializing<tok.init>` ``balanced.js``.

We're going to use the :ref:`card sample form <tok.card.form>`
from the :ref:`tokenization` section as it will do very basic information
collection for us.

For convenience, we've rendered the html into a fully functioning form:

.. container::
   :name: cc-form

   .. raw:: html
      :file: cc-form.html


To collect the information from the form, we're going to enlist the help
of some simple javascript:

.. code-block:: javascript

   // TODO: Replace this with your marketplace URI
   var marketplaceUri = '{YOUR-MARKETPLACE-URI}';
   var $form = $('#credit-card-form');

   // collect the data from the form.
   var creditCardData = {
       card_number: $form.find('.cc-number').val(),
       expiration_month: $form.find('.cc-em').val(),
       expiration_year: $form.find('.cc-ey').val(),
       security_code: $form.find('cc-csc').val()
   };

Now, let's handle the response from Balanced using a simple callback:

.. code-block:: javascript

   function responseCallbackHandler(response) {
      switch (response.status) {
        case 400:
            // missing or invalid field - check response.error for details
            console.log(response.error);
            break;
        case 404:
            // your marketplace URI is incorrect
            console.log(response.error);
            break;
        case 201:
            // WOO HOO! MONEY!
            // response.data.uri == URI of the card resource
            // you should store this returned card URI to later charge it
            console.log(response.data);
            $.post('your-marketplace.tld/cards', response.data);
        }
    }

.. note::
   :class: alert alert-info

   ``$.post('your-marketplace.tld/cards', response.data);`` is used
   as an example above. However, what you should do is iterate through the
   ``response.data`` object and add hidden form fields to submit alongside
   the form. Let us know if you need :ref:`any assistance <support>`, we're
   happy to help.

   You can find out more about the :ref:`callback here <tok.callback>`.

Now, let's submit it!

.. code-block:: javascript

   balanced.card.create(bankAccountData, responseCallbackHandler);


Operating with a Card Token
~~~~~~~~~~~~~~~~~~~~~~~~~~~

So you're done tokenizing card data? Congratulations! However, before you
do any operations on a card, you must associate the card to an account. That
means that if you just want to charge a card, you must create an account,
associate the card with that account, and then issue a debit.

.. _processing.buyer.acct_with_tok:

Creating an account
'''''''''''''''''''

Ok, so you've got the card token, referred to as the ``uri`` of the returned Card
resource.

Let's create an account to associate the card token with:

.. dcode:: scenario account_create_buyer

As always, anytime you create a resource on Balanced, you should
 :ref:`store the uri <uri_vs_id>` in your database.

.. _processing.buyer.add_tok_to_acct:

Associating a card to an existing account
'''''''''''''''''''''''''''''''''''''''''

A very common operation is associating a new card with an existing account.
Let's show how this is done:

.. dcode:: scenario account_add_card

This will add the card to the account specified by the account URI, **and make
it the primary funding source for any future holds and debits**.

Charging a Card
'''''''''''''''

Once you've either :ref:`added a card to a new account
<processing.buyer.acct_with_tok>` or :ref:`associated a card to an existing
account <processing.buyer.add_tok_to_acct>`, you can now easily charge the card
-- or to be exact, debit an account:

.. dcode:: scenario account_create_debit

.. note::
   :class: alert alert-info

   Balanced does NOT take its fees from your charges, instead it instruments
   all operations that have occurred on the API and later invoices you. Read
   :ref:`more about fees <overview.fees.balanced>`.


Refunds
-------

You can refund a debit up to its original amount, so that means you can partially
refund a debit as well.

In order for a refund to go through successfully, you *must* have enough money
in :ref:`implicit escrow <mp.escrow>` to cover your refund.

Note that for credit cards it typically takes one business day for refunds to
be reflected on a card statement, but it's possible for the issuing bank to
take as many as five business days to process a refund.

Here are some scenarios:

Full Refund
~~~~~~~~~~~

Let's say you've debited an account for $20.00

* Your ``in_escrow`` balance says $20.00
* You issue a refund for $20.00
* Your ``in_escrow`` balance says $0.00


Partial Refund
~~~~~~~~~~~~~~

You can also perform multiple partial refunds up to the original amount.

Let's say you've debited an account for $20.00

* Your ``in_escrow`` balance says $20.00
* You issue a refund for $10.00
* Your ``in_escrow`` balance says $10.00
* You issue another refund for $5.00
* Your ``in_escrow`` balance says $5.00

Not Enough Funds to Refund
~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's say you've debited an account for $20.00

* Your ``in_escrow`` balance says $20.00
* You issue a refund for $30.00
* The API will return a **400** status code, similar to:

  .. code-block:: bash

     Bad Request: 400: Invalid field [amount] - "3000" must be <= 2000


Holds
-----

Balanced supports the concepts of :term:`holds`. Holds are a type of
authorization that reserves (i.e. holds) a dollar amount on the customer's
credit card for the merchant to process later, usually within 7 days. If the
transaction is not processed (known as post-authorization) by the end of the
hold period, the amount is added back to the available credit on the
cardholder's credit card. **The customer is not billed.**

Holds are common in the industries where the amount of the goods or services
are "reserved" on the cardholder's credit card.

If you issue a debit on an account, Balanced uses holds behinds the scenes
but captures the funds immediately -- you will always see a hold returned on a
debit. For example:

.. dcode:: scenario account-create-debit
    :section-include: response

.. warning::
   :class: alert

   For all intents and purposes, Balanced does not recommend holds and considers
   their usage as a very advanced feature as they cause much confusion and are
   cumbersome to manage.

   If your project requires holds and you need help, please reach out
   to us using our :ref:`support channels <support>`.


Creating a hold
~~~~~~~~~~~~~~~

A hold is created in a way similar to creating a debit. Creating a hold will
return a URI which can be used to perform a capture later, up to the full
amount of the hold.

.. dcode:: scenario account-create-hold


Capturing a hold
~~~~~~~~~~~~~~~~

Here's an example on how to capture a hold:

.. dcode:: scenario account-capture-hold


.. _processing-testing:

Testing
-------

Test credit card numbers
~~~~~~~~~~~~~~~~~~~~~~~~

These cards will be accepted in our system only for a **TEST** marketplace.

.. cssclass:: table table-hover

  ============== ======================= ================ ==============================
   Card Brand          Number             Security Code     Result
  ============== ======================= ================ ==============================
  VISA             4111111111111111          123            SUCCESS
  MasterCard       5105105105105100          123            SUCCESS
  AMEX              341111111111111         1234            SUCCESS
  VISA             4444444444444448 [#]_     123            SIMULATE PROCESSOR FAILURE
  VISA             4222222222222220 [#]_     123            SIMULATE TOKENIZATION ERROR
  ============== ======================= ================ ==============================

.. [#] Simulate a card which can be tokenized but will not be accepted for creating
       holds or debits. This type of failure is what you would expect if you try to
       create a hold on a card with insufficient funds.
.. [#] To simulate a card which cannot be tokenized but passes a LUHN check. You could
       expect this failure when a user tried to enter in a credit card which used to
       work but has been canceled.


Best Practices
--------------

Using Meta for Custom Annotation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``meta`` field exists on all resources in the Balanced API. It may be used
as a dictionary of arbitrary key/value pairs, where each key and value is a
string of length 255 characters or less. This may be used to, e.g., annotate
accounts in our system with the account name on your system, or annotate
transactions with order numbers. The format is generally up to you, except in
the case of...

Using Meta for Fraud
~~~~~~~~~~~~~~~~~~~~

Balanced reserves some keys in the ``meta`` field. These are fields that may be
passed in by you in order to help fight fraud.

Shipping Address
''''''''''''''''

You may supply shipping fulfillment information by prefixing keys
specifying address data with the ``shipping.`` prefix. The specific
fields you may provide are:

-  shipping.address.street_address
-  shipping.address.city
-  shipping.address.region
-  shipping.address.country_code
-  shipping.carrier
-  shipping.tracking_number

Let's say you want to pass on shipping address, along with shipping
carrier (USPS, UPS, FedEx, etc.) and tracking number on a debit. This is
what the ``meta`` field would look like when represented as a JSON
dictionary:

.. code-block:: javascript

    meta = {
        'shipping.address.street_address': '801 High St',
        'shipping.address.city': 'Palo Alto',
        'shipping.address.region': 'CA',
        'shipping.address.postal_code': '94301',
        'shipping.address.country_code': 'USA',
        'shipping.carrier': 'FEDEX',
        'shipping.tracking_number': '1234567890'
    }


.. _sample page: https://gist.github.com/2662770
.. _balanced.js: https://js.balancedpayments.com/v1/balanced.js
.. _testing documentation: /docs/testing#simulating-card-failures
.. _jQuery: http://www.jquery.com
