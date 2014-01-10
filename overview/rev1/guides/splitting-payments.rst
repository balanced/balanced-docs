Splitting Payments
======================

Collecting Your Fees
~~~~~~~~~~~~~~~~~~~~

Now that you've understood how incoming money comes in to Balanced and the
concept of implicit escrow, you might ask yourself, "where do I take my
cut?" Since incoming funds are not touched by Balanced, you must issue a credit
to your own bank account with the funds you want for yourself -- that means you
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
~~~~~~~~~~~~~~~

Your marketplace listing fee is 10%. So, say Alice lists her bike for $100.00.
Bob decides to rent this bike - costing him $100.00.

- You charge Bob $100.00
- Your  balance now shows $100.00
- Alice delivers the bike to Bob
- You issue a $90.00 credit to Alice, using :ref:`Balanced Payouts <payouts>`

  -  Your listing fee is 10%, so 90% of $100.00 is $90.00

- Your marketplace's `dashboard <https://dashboard.balancedpayments.com/#/marketplaces/>`_ escrow balance now shows $10.00
- You issue a credit to your own bank account, using :ref:`Balanced Payouts <payouts>`
- Your money is in your bank account next business day
- Alice's money is in her bank account next business day
- Your marketplace's `dashboard <https://dashboard.balancedpayments.com/#/marketplaces/>`_ escrow balance now shows $0.00

Fee Scenario #2
~~~~~~~~~~~~~~~

Your marketplace renting fee is 10%. So, say Alice lists her bike for 100.00$.
Bob decides to rent this bike - costing him $110.00.

- You charge Bob $110.00

  - Your renting fee is 10%, so $100.00 * 1.10 = $110.00 is how much to charge Bob

- Your marketplace's `dashboard <https://dashboard.balancedpayments.com/#/marketplaces/>`_ escrow balance now shows $110.00
- Alice delivers the bike to Bob
- You issue a $100.00 credit to Alice, using :ref:`Balanced Payouts <payouts>`
- Your marketplace's `dashboard <https://dashboard.balancedpayments.com/#/marketplaces/>`_ escrow balance now shows $10.00
- You issue a credit for $10.00 to your own bank account, using :ref:`Balanced Payouts <payouts>`
- Your money is in your bank account next business day
- Alice's money is in her bank account next business day
- Your marketplace's `dashboard <https://dashboard.balancedpayments.com/#/marketplaces/>`_ escrow balance now shows $0.00

Fee Scenario #3
~~~~~~~~~~~~~~~

Your marketplace renting fee is 10%. You also charge a 10% listing fee.

So, say Alice lists her bike for 100.00$. Bob decides to rent this
bike - costing him $110.00.

- You charge Bob $110.00

  - Your renting fee is 10%, so $100.00 * 1.10 = $110.00 is how much to charge Bob

- Your marketplace's `dashboard <https://dashboard.balancedpayments.com/#/marketplaces/>`_ escrow balance now shows $110.00
- Alice delivers the bike to Bob
- You issue a $90.00 credit to Alice, using :ref:`Balanced Payouts <payouts>`

  -  Your listing fee is 10%, so 90% of $100.00 is $90.00

- Your marketplace's `dashboard <https://dashboard.balancedpayments.com/#/marketplaces/>`_ escrow balance now shows $20.00
- You issue a credit for $20.00 to your own bank account, using :ref:`Balanced Payouts <payouts>`
- Your money is in your bank account next business day
- Alice's money is in her bank account next business day
- Your marketplace's `dashboard <https://dashboard.balancedpayments.com/#/marketplaces/>`_ escrow balance now shows $0.00

.. cmd
.. Crediting Your Seller's Bank Account


.. todo:: talk about why this is different from payouts piece

.. cmd
.. Crediting Your Own Merchant Account

.. todo:: discuss fees etc