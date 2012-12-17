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
   :class: alert alert-info

   From here on out, we will refer to your seller / service provider as a
   **merchant**. Learn more about :term:`merchants`.

Balanced allows you to mitigate this risk by exposing a programmatic merchant
underwriting API to easily create merchant accounts. Most merchants will
never have to leave your site. This makes it easy to accept payments on behalf
of your merchants, while keeping your accounting sane.

Let's get started!

Merchant Underwriting
---------------------

Underwriting merchants involves every merchant to go through Know Your Customer
(KYC) regulations, which is required by the U.S. government for purposes of
Anti-Money Laundering (AML). This process is generally simple, and for most
merchants requires very little information.

Collecting Merchant Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. discuss escalating form

Sign-up process (API)
~~~~~~~~~~~~~~~~~~~~~

Collecting merchant information requires slightly different information
depending on if the merchant is being underwritten as a person or as a
business.

Person
''''''

.. dcode:: account_underwrite_person

Business
''''''''

.. dcode:: account_underwrite_merchant


On Success (201 CREATED)
~~~~~~~~~~~~~~~~~~~~~~~~

If identification and verification was successful, Balanced will return
a **201** status code

On Failure (300 MULTIPLE CHOICES)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Occasionally, the information passed to Balanced for merchant underwriting will
be insufficient to identify them, and Balanced will return a **300** status
code.

We specifically return **300** status code because you have multiple choices
-- you may either re-submit the original request along with more identifying
information (e.g. ``tax_id``), **or** you may redirect the user to the
location specified in the redirect, where Balanced will ask for more
information to verify the user's identity with state and federal databases.

If you choose to submit more information, then simply repeat the above
flow with corrected or additional information.

However, if you choose to redirect them for Balanced to underwrite them, the
following section will alleviate the process.

Redirect
''''''''

The location you may redirect the user to is stored in the ``Location``
header in the response to your request. You must include a
``redirect_uri`` parameter along with the original URL so Balanced knows where
to return the user to once they have completed the underwriting process.

Additionally, you may pre-fill the form for the user by encoding the
original JSON payload as query string parameters.

The encoding should follow the form of ``merchant[key]=value`` e.g.:

.. code-block:: javascript

    ?merchant[type]=business&email_address=merchant@example.org&merchant[phone_number]=9046281796&redirect_uri=https://yoursite.com/verify

Handling Redirect Response
''''''''''''''''''''''''''

After the user has been redirected to Balanced and if the merchant was
successfully underwritten, Balanced will redirect the user to your specified
``redirect_uri`` with **two** parameters appended as query strings.

Those are are ``email_address`` and ``merchant_uri``.

.. todo:: clarify this..

.. note::
  :class: alert alert-info

  You **MUST** submit these two parameters to successfully create the merchant
  account.


Associating debits/charges with a merchant
------------------------------------------

In order to stay compliant and to provide evidence that you're not aggregating,
when charging cards on your marketplace, all associated charges should be done
on behalf of the merchant. You must associate charges with the merchant's
account - this is very easy, simply pass the merchant account's ``uri`` via
the ``merchant_uri`` parameter on the charge you're issuing.

.. todo:: show example

The benefits of this are clearly obvious - in order to determine how much money
you owe a specific merchant, you can easily query and all the outstanding debits
tied to this merchant and subtract the payouts you've already done to the
merchant.

.. accounting benefits

This dramatically simplifies your book-keeping and allows Balanced to take
care of most of the accounting work -- like end of year taxes, reserves, cash
flow, and operating capital.


Funds Flow
----------

It's important to understand how the funds flow works on Balanced. First and
foremost, when a charge occurs on Balanced, the amount you've charged your
user is the exact amount that shows up in the balance.

.. more images
.. more explanations
.. more scenarios

.. _mp.escrow:

Escrow
~~~~~~

This means that once a card is successfully charged, your funds are implicitly,
in escrow, for your marketplace. This gives you complete control on
funds disbursement.

You may choose to keep the money in implicit escrow for as long as you desire
- but the common use case for this is to wait for any type of fulfillment
from your merchants -- such as confirmation of a shipped product or
completion of a service.

Since :ref:`Balanced Payouts <payouts>` delivers funds to your merchant within
one (1) business day, you can get a bit more creative as well. For example,
you may stagger the funds for disbursement at different times during the order
process - for example:

- A buyer has paid for a service
- Your merchant needs half of the payout amount as working capital
- You issue 50% of the amount you charged the buyer as a credit to the merchant
  using :ref:`Balanced Payouts <payouts>`
- The merchant performs the service and buyer is happy with the service
- You can pay the other half post completion of the service

In today's growing collaborative consumption economy, this model is extremely
powerful for providing marketplace liquidity to enable new forms of commerce.

Collecting Your Fees
~~~~~~~~~~~~~~~~~~~~

Now that you've understood how incoming money comes in to Balanced and the
concept of implicit escrow, you might ask yourself, "where do I take my
cut?"

Since incoming funds are not touched by Balanced, you must issue a credit to
your own bank account with the funds you want for yourself -- that means you
must do the math to calculate the difference.

There are three common scenarios:

.. adding them to the buyer

1. adding your business' fee to the total amount charged during checkout

.. taking it from the merchant

2. with-holding some of the funds from the merchant and diverting those funds to yourself

.. both

3. doing both of these :)

Here are some examples that can clarify these scenarios, but first let's give
a little context:

Let's say you have a marketplace called **Rent\ My\ Bike** [#]_, which provides
a platform for bike owners, a.k.a. merchants, to put their bikes for rent by
renters, a.k.a. the buyers.

Recap:

- The bike owners are the merchants.
- The renters are the buyers.
- Your marketplace is called Rent By Bike

.. [#] Our sample marketplace is actually called `Rent My Bike`_ :)


Fee Scenario #1
'''''''''''''''

Your marketplace listing fee is 10%. So, say Alice lists her bike for 100.00$.
Bob decides to rent this bike - costing him $100.00.

- You charge Bob $100.00
- Your ``in_escrow`` balance now shows $100.00
- Alice delivers the bike to Bob
- You issue a $90.00 credit to Alice, using :ref:`Balanced Payouts <payouts>`

  -  Your listing fee is 10%, so 90% of $100.00 is $90.00

- Your ``in_escrow`` balance now shows $10.00
- You issue a credit to your own bank account, using :ref:`Balanced Payouts <payouts>`
- Your money is in your bank account next business day
- Alice's money is in her bank account next business day
- Your ``in_escrow`` balance now shows $0.00

Fee Scenario #2
'''''''''''''''

Your marketplace renting fee is 10%. So, say Alice lists her bike for 100.00$.
Bob decides to rent this bike - costing him $110.00.

- You charge Bob $110.00

  - Your renting fee is 10%, so $100.00 * 1.10 = $110.00 is how how much to charge Bob

- Your ``in_escrow`` balance now shows $110.00
- Alice delivers the bike to Bob
- You issue a $100.00 credit to Alice, using :ref:`Balanced Payouts <payouts>`
- Your ``in_escrow`` balance now shows $10.00
- You issue a credit for $10.00 to your own bank account, using :ref:`Balanced Payouts <payouts>`
- Your money is in your bank account next business day
- Alice's money is in her bank account next business day
- Your ``in_escrow`` balance now shows $0.00

Fee Scenario #3
'''''''''''''''

Your marketplace renting fee is 10%. You also charge a 10% listing fee.

So, say Alice lists her bike for 100.00$. Bob decides to rent this
bike - costing him $110.00.

- You charge Bob $110.00

  - Your renting fee is 10%, so $100.00 * 1.10 = $110.00 is how how much to charge Bob

- Your ``in_escrow`` balance now shows $110.00
- Alice delivers the bike to Bob
- You issue a $90.00 credit to Alice, using :ref:`Balanced Payouts <payouts>`

  -  Your listing fee is 10%, so 90% of $100.00 is $90.00

- Your ``in_escrow`` balance now shows $20.00
- You issue a credit for $20.00 to your own bank account, using :ref:`Balanced Payouts <payouts>`
- Your money is in your bank account next business day
- Alice's money is in her bank account next business day
- Your ``in_escrow`` balance now shows $0.00


Crediting Your Seller's Bank Account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. todo:: talk about why this is different from payouts piece


Crediting Your Own Merchant Account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. todo:: discuss fees etc


.. Best Practices
.. --------------
..
.. Using Meta for Custom Annotation
.. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
..
.. Breakdown of Escrow Balance by Merchant
.. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
..
.. _Rent My Bike: https://rentmybike.co
