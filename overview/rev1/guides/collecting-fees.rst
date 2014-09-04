Collecting Fees
======================

When processing payments in Balanced, you're probably asking yourself,
"How do I take my cut?" There are inherently no restrictions on how you
calculate and distribute your fees.

Incoming funds are not touched by Balanced, you must issue a credit
to your own bank account with the funds you want for yourself -- that means you
must do the math to calculate the difference.

Throughout this guide we'll use our example marketplace,
`Rent My Bike <http://rentmybike.co>`_ to demonstrate some common fee
handling scenarios.

Background information:

- Rent My Bike provides a platform for bike owners to rent out their bikes.
- The bike owners are the merchants.
- The renters are the buyers.

|

Inclusive Fees
---------------

An inclusive fee scenario is where the fees you plan to collect come out of the
original item or service price.

Your marketplace listing fee is 10%. So, say Alice lists her bike for $100.00.
Bob decides to rent this bike - costing him $100.00.

- You charge Bob $100.00
- Your balance now shows $100.00
- Alice delivers the bike to Bob
- You issue a $90.00 credit to Alice

  - Your listing fee is 10%, so 90% of $100.00 is $90.00

- Your marketplace's `dashboard <https://dashboard.balancedpayments.com/#/marketplaces/>`_ escrow balance now shows $10.00
- You issue a credit to your own bank account
- Your money is in your bank account next business day
- Alice's money is in her bank account next business day
- Your marketplace's `dashboard <https://dashboard.balancedpayments.com/#/marketplaces/>`_ escrow balance now shows $0.00


Additional Fees
----------------

An additional fee scenario is where the fees you plan to collect are added to
the original item or service price.

Your marketplace renting fee is 10%. So, say Alice lists her bike for $100.00.
Bob decides to rent this bike, costing him $110.00.

- You charge Bob $110.00

  - Your renting fee is 10%, so $100.00 * 1.10 = $110.00 is how much to charge Bob

- Your marketplace's `dashboard <https://dashboard.balancedpayments.com/#/marketplaces/>`_ escrow balance now shows $110.00
- Alice delivers the bike to Bob
- You issue a $100.00 credit to Alice
- Your marketplace's `dashboard <https://dashboard.balancedpayments.com/#/marketplaces/>`_ escrow balance now shows $10.00
- You issue a credit for $10.00 to your own bank account
- Your money is in your bank account next business day
- Alice's money is in her bank account next business day
- Your marketplace's `dashboard <https://dashboard.balancedpayments.com/#/marketplaces/>`_ escrow balance now shows $0.00


Double-Ended Fees
------------------

A double-ended fee scenario is where the fees you plan to collect come from 
both the buyer, upon payment for an item or service, and the seller during a
payout.

Your marketplace renting fee is 10%. You also charge a 10% listing fee.

So, say Alice lists her bike for 100.00$. Bob decides to rent this
bike - costing him $110.00.

- \- You charge Bob $110.00

  - Your renting fee is 10%, so $100.00 * 1.10 = $110.00 is how much to charge Bob

- \- Your marketplace's `dashboard <https://dashboard.balancedpayments.com/#/marketplaces/>`_ escrow balance now shows $110.00
- \- Alice delivers the bike to Bob
- \- You issue a $90.00 credit to Alice

  -  Your listing fee is 10%, so 90% of $100.00 is $90.00

- \- Your marketplace's `dashboard <https://dashboard.balancedpayments.com/#/marketplaces/>`_ escrow balance now shows $20.00
- \- You issue a credit for $20.00 to your own bank account
- \- Your money is in your bank account next business day
- \- Alice's money is in her bank account next business day
- \- Your marketplace's `dashboard <https://dashboard.balancedpayments.com/#/marketplaces/>`_ escrow balance now shows $0.00