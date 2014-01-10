.. _best_practices:

Best Practices
==============

.. _use_balanced_js:

Use balanced.js
---------------

Use balanced.js to tokenize cards and bank accounts. balanced.js keeps your systems PCI compliant
by sending sensitive information over SSL directly to the Balanced servers.

.. note::
   :header_class: alert alert-tab
   :body_class: alert alert-gray

   This does not remove the need for you to use SSL on your servers as all financial transactions
   should occur over SSL.


.. _best_practices.payouts:

Reducing Declined Transactions
------------------------------

Fraud and Card declinations can be reduced if the following information is supplied when tokenizing a card:

.. cssclass:: list-noindent

  - ``name`` (Name on card)
  - ``cvv`` (CVV)
  - ``postal_code`` (Postal code)

|

.. note::
   :header_class: alert alert-tab-red
   :body_class: alert alert-gray

   American Express declines transactions with cards that do not include ``security_code`` and
   ``postal_code``.


Catching Fraud Early
--------------------

It's very important to take a proactive stance against fraud. Below are some
tips to help guard against it. We recommend marketplaces take advantage of
the following:

.. cssclass:: list-noindent

  - * Utilize customer verification. We highly recommended that you do not issue payouts to unverified customers. Refer to :ref:`resources.test-identity-verification`
  - * Utilize AVS. Refer to :ref:`resources.address-verification-service`
  - * Utilize CSC. Refer to :ref:`resources.card-security-code`
  - * Respond in a timely fashion to Balanced inquiries about chargebacks or suspicious transactions
  - * Report fraud to support@balancedpayments.com.


.. _best_practices.reducing-payout-delays:

Reducing Payout Delays
----------------------

Automated Clearing House transactions are asynchronous, requiring upfront effort
in educating your consumers and setting the appropriate expectations to deliver
a great product.

Balanced validates bank routing numbers in real-time using the
`FedACH directory`_, but since bank account numbers are not standardized, incorrect
bank account numbers are not caught until the payout fails.
Unfortunately, due to the nature of the ACH network, failure notifications can be delayed
for up to (4) four business days. This means that an account number typo can, on average,
cause payment delays by up to (3) three to (5) five business days.

Since you or your users may rely on these funds as operating capital, this delay can be
extremely inconvenient and frustrating to you and your users.

Our recommendation, for mitigating these user experience issues, is to properly
invest time in building a robust and reliable form to collect the merchant
bank account information properly.

Here are some tips:

#. Display a check image to illustrate which number is the routing number vs.
   account number.

   We've conveniently provided one - however, you may choose to design your
   own:

   .. figure:: https://s3.amazonaws.com/justice.web/docs/check_image.png

#. US routing numbers are 9 digits and are usually located in the lower left
   corner of most checks. Common aliases to **routing number**:

   * RTN (Routing Transit Number)
   * ABA
   * `Bank code`_

#. Routing numbers are used to set up direct deposit transfers. You can use this
   as an aid to your customers who are inquiring whether or not they have the
   right routing number.

#. If you're double checking routing numbers for customers, most banks assign routing numbers
   according to the state or region of the state that the bank account was opened in.

#. Encourage customers to check their bank websites for the routing number used specifically
   for ACH or electronic deposits. Some large banks, particularly Bank Of America, may have
   different routing numbers for checks and direct deposits.

#. Balanced has provided very useful routing number validators in our
   :ref:`balanced.js <getting_started.balanced.js_bank_accounts>` library.
   Use these helper functions to build a robust form.

#. Set your customer's expectation that payments might be delayed by up to
   (3) three to (5) five business days if incorrect information is provided.

#. Highlight to your customers that *wire transfer numbers* are **NOT** the same
   as the routing number, and they are **NOT** the same as the bank account
   number. Be sure to clarify this when asking your users for their information.

Our statistics show that most of the time, with the help of a properly designed and robust
form, your users will provide the correct bank routing and account numbers.

With correct bank information their payout will usually appear the next business day, as
expected. Once a successful payout has been made, future credits to that bank account
will continue to take one business day when issued before the
:ref:`next-day cut-offs <payouts.cutoff>`.

If a payout does fail for any reason, we’ll notify you via email, dashboard, and webhook.
If a customer complains about a payout failure and you do not see any notification with in
the expected time window, please reach out to support@balanedpayments.com and we'll track
down the payout as soon as possible.

.. _Bank code: http://en.wikipedia.org/wiki/Bank_code
.. _FedACH directory: https://www.fededirectory.frb.org


Use Meta
--------

The ``meta`` field exists on all resources in the Balanced API. It may be used
as a dictionary of arbitrary key/value pairs, where each key and value is a
string of length 255 characters or less. Illustratively, this may be used to annotate
accounts in our system with the account name on your system or annotate
transactions with order numbers. The format is generally up to you, but
Balanced reserves some keys in the ``meta`` field. These are fields that may be
passed in by you in order to help fight fraud and respond to chargebacks.

.. container:: section

  .. container:: header3

    Shipping Address

  You may supply shipping fulfillment information by prefixing keys
  specifying address data with the ``shipping.`` prefix. The specific
  fields you may provide are:

  -  shipping.address.street_address
  -  shipping.address.city
  -  shipping.address.region
  -  shipping.address.country_code (`ISO 3166-1 alpha-3`_)
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


.. _ISO 3166-1 alpha-3: http://en.wikipedia.org/wiki/ISO_3166-1_alpha-3
