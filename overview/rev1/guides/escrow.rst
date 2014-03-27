Understanding Escrow
======================

Every marketplace has a single escrow. This escrow account is essentially like a
pool of funds. Debits bring funds into the marketplace escrow. Credits take
funds out of the marketplace escrow.

Marketplaces have complete control over how funds are disbursed from escrow.
Funds in escrow may be distributed to recipients as desired. There is inherently
no time limit for the duration funds may sit in escrow. Best practice is to
refrain from releasing funds until after merchant fulfillment has occurred,
confirmation of a shipped product or completion of a service for example. Escrow
is not meant as a means of extended withholding. Holding funds in escrow for
extended periods of time often leads to an increased number in chargebacks and
customer dissatisfaction.

|

.. note::
  :header_class: alert alert-tab
  :body_class: alert alert-green
  
  Balanced does not collect interest of any kind on funds in escrow.
  Transactions involving credit cards and bank accounts associated to your
  marketplace are free of charge.

  
Pre-funding Escrow
------------------------

Any payout issued requires maintaining sufficient money in your Balanced escrow.

If you do not have a sufficient balance, Balanced will return a ``409`` http
status code, stating that you do not have sufficient funds to cover your
desired ACH operation. You will have to add funds to your marketplace escrow
from a credit card or bank account attached to your marketplace. This may be
done via the API or via the Balanced `dashboard`_. To do this via the API:

.. code-block:: bash

  # Get the marketplace
  curl https://api.balancedpayments.com/marketplaces \
       -H "Accept: application/vnd.api+json;revision=1.1" \
       -u ak-test-h7F8F3u41y6LzCK4nZeVd5BafaWOUuZL:

  # Determine owner customer from marketplaces.owner_customer link and get its bank accounts
  curl https://api.balancedpayments.com/customers/CU1U8FEqP5FsisYD0D5G6aS4/bank_accounts \
       -H "Accept: application/vnd.api+json;revision=1.1" \
       -u ak-test-h7F8F3u41y6LzCK4nZeVd5BafaWOUuZL:

  # Determine the debits href from the bank_accounts.debits link and create a debit
  curl https://api.balancedpayments.com/bank_accounts/BA1VKlrw3m7lNyouaU5h8Xba/debits \
       -H "Accept: application/vnd.api+json;revision=1.1" \
       -u ak-test-h7F8F3u41y6LzCK4nZeVd5BafaWOUuZL: \
       -d "amount=2000000"

.. code-block:: ruby

  Balanced::Marketplace.mine.owner_customer.bank_accounts.first.debit(
    :amount => 2000000,
    :description => 'Pre-fund Balanced escrow'
  )

.. code-block:: python

  balanced.Marketplace.mine.owner_customer.bank_accounts[0].debit(
    amount=2000000,
    description='Pre-fund Balanced escrow'
  )

.. code-block:: php

  <?php
  Balanced\Marketplace::mine()->owner_customer->bank_accounts->query()->first()->debits->create(array(
    "amount" => "2000000",
    "description" => "Pre-fund Balanced escrow",
  ));
  ?>


.. tip::
  :header_class: alert alert-tab
  :body_class: alert alert-green

  We advise that you transfer a large amount in your Balanced account or you
  may request that Balanced always keep a constant amount in your account for
  you. We're publicly tracking this on `github issue #132`_ and appreciate your input

Transfers may take 2-5 days for the funds to become available; alternatively, you
may fund your account **instantly** by debiting a credit card associated to your
marketplace.


Obtaining funds from Escrow
---------------------------

To transfer funds from your marketplace escrow to your marketplace bank account,
issue a credit:

.. code-block:: bash

  # Get the marketplace
  curl https://api.balancedpayments.com/marketplaces \
       -H "Accept: application/vnd.api+json;revision=1.1" \
       -u ak-test-h7F8F3u41y6LzCK4nZeVd5BafaWOUuZL:

  # Determine owner customer from marketplaces.owner_customer link and get its bank accounts
  curl https://api.balancedpayments.com/customers/CU1U8FEqP5FsisYD0D5G6aS4/bank_accounts \
       -H "Accept: application/vnd.api+json;revision=1.1" \
       -u ak-test-h7F8F3u41y6LzCK4nZeVd5BafaWOUuZL:

  # Determine the debits href from the bank_accounts.debits link and create a credit
  curl https://api.balancedpayments.com/bank_accounts/BA1VKlrw3m7lNyouaU5h8Xba/credits \
       -H "Accept: application/vnd.api+json;revision=1.1" \
       -u ak-test-h7F8F3u41y6LzCK4nZeVd5BafaWOUuZL: \
       -d "amount=2000000"

.. code-block:: ruby

  Balanced::Marketplace.mine.owner_customer.bank_accounts.first.credit(
    :amount => 2000000,
    :description => 'Credit from Balanced escrow'
  )

.. code-block:: python

  balanced.Marketplace.mine.owner_customer.bank_accounts[0].credit(
    amount=2000000,
    description='Credit from Balanced escrow'
  )

.. code-block:: php

  <?php
  Balanced\Marketplace::mine()->owner_customer->bank_accounts->query()->first()->credits->create(array(
    "amount" => "2000000",
    "description" => "Credit from Balanced escrow",
  ));
  ?>

Credits can take 1-3 days for the funds to become available depending on
the target bank.


.. _dashboard: https://dashboard.balancedpayments.com/
.. _github issue #132: https://github.com/balanced/balanced-api/issues/132