.. _marketplaces:

Marketplaces
============

Running a successful marketplaces typically requires combinations of both
:ref:`processing`, accepting credit cards, and :ref:`payouts`, paying out your
sellers and service providers. When those two disjoint services are coupled
as a means to collect money on behalf of someone else, i.e. a seller or
service provider, then that classifies as :term:`aggregation` - something that
all the credit card networks such as Visa, American Express, MasterCard, etc.
frown upon and causes risk of merchant account termination, consequently,
leaving your business without a way to process online transactions.

.. note::
   :header_class: alert alert-tab
   :body_class: alert alert-green

   From here on out, we will refer to your seller / service provider as a
   **merchant**. Learn more about :term:`merchants`.

Balanced allows you to mitigate this risk by exposing a programmatic merchant
underwriting API to easily create merchant accounts. Most merchants will
never have to leave your site. This makes it easy to accept payments on behalf
of your merchants, while keeping your accounting sane.

Let's get started!

.. Merchant Underwriting
.. ---------------------
.. 
.. Underwriting merchants involves every merchant to go through Know Your Customer
.. (KYC) regulations, which is required by the U.S. government for purposes of
.. Anti-Money Laundering (AML). This process is generally simple, and for most
.. merchants requires very little information.
.. 
.. Collecting Merchant Information
.. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. 
.. .. discuss escalating form
.. 
.. Sign-up process (API)
.. ~~~~~~~~~~~~~~~~~~~~~
.. 
.. Collecting merchant information requires slightly different information
.. depending on if the merchant is being underwritten as a person or as a
.. business.
.. 
.. Person
.. ''''''
.. 
.. .. dcode:: scenario account_underwrite_person
.. 
.. Business
.. ''''''''
.. 
.. .. dcode:: scenario account_underwrite_business
.. 
.. 
.. On Success (201 CREATED)
.. ~~~~~~~~~~~~~~~~~~~~~~~~
.. 
.. If identification and verification was successful, Balanced will return
.. a **201** status code
.. 
.. On Failure (300 MULTIPLE CHOICES)
.. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. 
.. Occasionally, the information passed to Balanced for merchant underwriting will
.. be insufficient to identify them, and Balanced will return a **300** status
.. code.
.. 
.. We specifically return **300** status code because you have multiple choices
.. -- you may either re-submit the original request along with more identifying
.. information (e.g. ``tax_id``), **or** you may redirect the user to the
.. location specified in the redirect, where Balanced will ask for more
.. information to verify the user's identity with state and federal databases.
.. 
.. If you choose to submit more information, then simply repeat the above
.. flow with corrected or additional information.
.. 
.. However, if you choose to redirect them for Balanced to underwrite them, the
.. following section will alleviate the process.
.. 
.. Redirect
.. ''''''''
.. 
.. The location you may redirect the user to is stored in the ``Location``
.. header in the response to your request. You must include a
.. ``redirect_uri`` parameter along with the original URL so Balanced knows where
.. to return the user to once they have completed the underwriting process.
.. 
.. Additionally, you may pre-fill the form for the user by encoding the
.. original JSON payload as query string parameters.
.. 
.. The encoding should follow the form of ``merchant[key]=value`` e.g.:
.. 
.. .. code-block:: javascript
.. 
..     ?merchant[type]=business&email_address=merchant@example.org&merchant[phone_number]=9046281796&redirect_uri=https://yoursite.com/verify
.. 
.. Handling Redirect Response
.. ''''''''''''''''''''''''''
.. 
.. After the user has been redirected to Balanced and if the merchant was
.. successfully underwritten, Balanced will redirect the user to your specified
.. ``redirect_uri`` with **two** parameters appended as query strings.
.. 
.. Those are ``email_address`` and ``merchant_uri``.
.. 
.. .. todo:: clarify this..
.. 
.. .. note::
..   :class: alert alert-info
.. 
..   You **MUST** submit these two parameters to successfully create the merchant
..   account.

Simulating verified with customers
----------------------------------

With the new customer resource, you can submit a name, date of birth and postal
code and the is_validated flag will be set to true in a test marketplace.  If
you set the name parameter to nothing, then the is_validated flag will be set to
false.


This will create a customer object with the is_identity_verified flag true

.. code-block:: bash

   curl -u 227d0356d9f311e29803026ba7d31e6f: https://api.balancedpayments.com/v1/customers \
   -d "name=Henry Ford" \
   -d "dob=1863-07" \
   -d "address[postal_code]=48120"


This will set the is_identity_verified flag on an existing customer from true to false

.. code-block:: bash

   curl -u 227d0356d9f311e29803026ba7d31e6f: https://api.balancedpayments.com/v1/customers/CU2kaisGxbyDuyWiNg3NjeAu \
   -d "name="

Associating debits with a merchant
----------------------------------

In order to stay compliant and to provide evidence that you're not aggregating,
when charging cards on your marketplace, all associated charges should be done
on behalf of the merchant. You must associate charges with the merchant's
account - this is very easy, simply pass the merchant account's ``uri`` via
the ``on_behalf_of`` parameter on the charge you're issuing.

.. todo:: show example

The benefits of this are clearly obvious - in order to determine how much money
you owe a specific merchant, you can easily query and all the outstanding debits
tied to this merchant and subtract the payouts you've already done to the
merchant.

.. accounting benefits

This dramatically simplifies your book-keeping and allows Balanced to take
care of most of the accounting work -- like end of year taxes, reserves, cash
flow, and operating capital.
