.. _fees:

Pricing and fees
================

You will pay a fee of 25¢ when you successfully payout to a seller’s
bank account, and 2.9% + 30¢ when you successfully charge a buyer’s
credit card. We try to keep our pricing straightforward, so Balanced
does not charge any fees besides those listed here.

.. _fees.payouts:

Payout Pricing
--------------

It costs just simply 25¢ to issue a next-day ACH credit. Our full
fee per operation is listed below:

.. cssclass:: table table-hover

  ============================ ===============
    operation                    cost to you
  ============================ ===============
  next-day ACH                             25¢
  failure                                $3.50
  reversal                                  $0
  batch fee                                 $0
  monthly fee                               $0
  set-up fee                                $0
  payouts to your bank account              $0
  ============================ ===============

.. _fees.processing:

Processing Pricing
------------------

Charging credit cards costs just 2.9% and 30¢ per successful charge. Our full
fees per operation is listed below:

.. cssclass:: table table-hover

  ================================ ===================
    operation                        cost to you
  ================================ ===================
  successful credit card charge       2.9% + 30¢
  issuing a hold                             30¢ [*]_
  successful bank account charge        1% + 30¢
  chargeback                              $15.00
  refund                                      $0
  failure                                     $0
  batch fee                                   $0
  monthly fee                                 $0
  set-up fee                                  $0
  ================================ ===================

.. [*] If you issue a hold and then successfully charge, you only incur
       the 2.9% fee - there is no additional 30¢ fee.


.. _fees.balanced:

Invoicing fees
--------------

Balanced will create invoices to collect fees daily. These invoices can be
viewed under the invoices tab of the Balanced dashboard. These fees are
debited from the bank account attached to the owner account of the
marketplace.

.. note::
  :header_class: alert alert-tab
  :body_class: alert alert-gray

  **Balanced will never take fees from the operating capital (escrow account) of the marketplace.**

Example
~~~~~~~

A buyer pays for a service on Monday from a third-party merchant. You charge
the buyer $10, which increases your escrow balance by $10. Balanced will invoice
you, on Monday for 2.9% of $10 (or 29¢), plus 30¢, and debit your bank account
for a total of 59¢.

On Wednesday, the third-party merchant completes performing a service for the
buyer, and the buyer acknowledges this. You credit out payment to the
merchant, likely keeping a portion to pay your fees. Perhaps you pay out $7
to the merchant, leaving you with $3 in your escrow account. Balanced will
invoice you, on Wednesday, 25¢ for this ACH credit.

The $3 that is left from the buyer's $10 is your revenue from this order. You
decide to credit this to your own bank account on Friday. Balanced doesn't
charge you for this credit, as credits to owner accounts are free.


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

Once a card is successfully charged your funds are implicitly in escrow for
your marketplace. This gives you complete control on funds disbursement.

You may choose to keep the money in escrow for as long as you desire
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

1. with-holding some of the funds from the merchant and diverting those funds to yourself

.. taking it from the merchant

2. adding your business' fee to the total amount charged during checkout

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
- Your marketplace is called Rent My Bike

.. [#] Our sample marketplace is actually called `Rent My Bike`_ :)

.. _Rent My Bike: http://rentmybike.heroku.com


Fee Scenario #1
'''''''''''''''

Your marketplace listing fee is 10%. So, say Alice lists her bike for $100.00.
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

.. cmd
.. Crediting Your Seller's Bank Account


.. todo:: talk about why this is different from payouts piece

.. cmd
.. Crediting Your Own Merchant Account

.. todo:: discuss fees etc
