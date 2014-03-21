:orphan:

Charging Funding Instruments
==================================

A funding instrument is a resource which represents a source or target for
interactions involving money.


Charging a Card
----------------

Charging a card is a synchronous operation. Immediately after charging a card,
the funds will be available for use.

API References:

.. cssclass:: list-noindent

  - `Create a Card (Direct) </1.1/api/cards/#create-a-card-direct>`_
  - `Charge a Card </1.1/api/cards/#charge-a-card>`_

|

.. note::
  :header_class: alert alert-tab-red
  :body_class: alert alert-red
  
  The example below demonstrates how to create cards directly via the API.
  This method is not recommended for production environments. Please use
  balanced.js to create cards.


First, let's create a ``Card`` to work with.

.. literalinclude:: ruby/card-create.rb
   :language: ruby

.. literalinclude:: python/card-create.py
   :language: python

.. literalinclude:: curl/card-create.sh
   :language: bash

.. literalinclude:: php/card-create.php
   :language: php


Now that we have a ``Card``, we can charge it. This will issue a ``Debit`` which
will deduct funds from the target credit card.

.. literalinclude:: ruby/card-debit.rb
   :language: ruby

.. literalinclude:: python/card-debit.py
   :language: python

.. literalinclude:: curl/card-debit.sh
   :language: bash

.. literalinclude:: php/card-debit.php
   :language: php


Since card debits are immediate, we can check our escrow to see the funds are
indeed available.

.. literalinclude:: ruby/marketplace-in-escrow.rb
   :language: ruby

.. literalinclude:: python/marketplace-in-escrow.py
   :language: python

.. literalinclude:: curl/marketplace-in-escrow.sh
   :language: bash

.. literalinclude:: php/marketplace-in-escrow.php
   :language: php


Charging a Bank Account
------------------------

Charging a bank account is an asynchronous operation. An ACH debit is not
immediate and takes 1-4 days to complete. Eventually you'll want to create a
``Callback`` and listen for an ``Event`` to be alerted on changes to ACH
transactions.

API References:

.. cssclass:: list-noindent

  - `Create a Bank Account (Direct) </1.1/api/bank-accounts/#create-a-bank-account-direct>`_
  - `Create a Bank Account Verification </1.1/api/bank-account-verifications/#create-a-bank-account-verification>`_
  - `Confirm a Bank Account Verification </1.1/api/bank-account-verifications/#confirm-a-bank-account-verification>`_
  - `Charge a Bank Account </1.1/api/bank-accounts/#charge-a-bank-account>`_

|

.. note::
  :header_class: alert alert-tab-red
  :body_class: alert alert-red
  
  The example below demonstrates how to create bank accounts directly via the
  API. This method is not recommended for production environments. Please use
  balanced.js to create bank accounts.


First, let's create a ``BankAccount`` to work with.

.. literalinclude:: ruby/bank-account-create.rb
   :language: ruby

.. literalinclude:: python/bank-account-create.py
   :language: python

.. literalinclude:: curl/bank-account-create.sh
   :language: bash

.. literalinclude:: php/bank-account-create.php
   :language: php

We now have a ``BankAccount`` instance to work with. Before a ``BankAccount``
can be charged (debited) it must be verified with micro deposits. This is done
by initiating a bank account verification. When a bank account verification is
initiated, Balanced will send two random amounts each less than $1 to the target
bank account. These amounts will show on the bank account statement usually in
1-2 days. Since time is going to pass here, you probably want to store the
``BankAccountVerification`` href to simplify later fetching.

.. literalinclude:: ruby/bank-account-verification-create.rb
   :language: ruby

.. literalinclude:: python/bank-account-verification-create.py
   :language: python

.. literalinclude:: curl/bank-account-verification-create.sh
   :language: bash

.. literalinclude:: php/bank-account-verification-create.php
   :language: php

Once the amounts have posted on the bank account statement, the bank account
owner then should return to your application and enter these amounts into a form
which sends the values to Balanced as follows:

.. note::
  :header_class: alert alert-tab
  :body_class: alert alert-green
  
  The verification values in test marketplaces are always 1 and 1.


.. literalinclude:: ruby/bank-account-verification-confirm.rb
   :language: ruby

.. literalinclude:: python/bank-account-verification-confirm.py
   :language: python

.. literalinclude:: curl/bank-account-verification-confirm.sh
   :language: bash

.. literalinclude:: php/bank-account-verification-confirm.php
   :language: php


At this point we have a verified bank account that we can now charge (debit).
This will issue a ``Debit`` which will deduct funds from the target credit 
bank account.

.. code-block:: ruby

  bank_account.debit(
    :amount => 5000,
    :appears_on_statement_as => 'Statement text',
    :description => 'Some descriptive text for the debit in the dashboard'
  )

.. code-block:: python

  bank_account.debit(
    appears_on_statement_as='Statement text',
    amount=5000,
    description='Some descriptive text for the debit in the dashboard'
  )

.. code-block:: bash

  curl https://api.balancedpayments.com/bank_accounts/BA2akihQKCAhhkX5aecSubr2/debits \
     -H "Accept: application/vnd.api+json;revision=1.1" \
     -u ak-test-h7F8F3u41y6LzCK4nZeVd5BafaWOUuZL: \
     -d "appears_on_statement_as=Statement text" \
     -d "amount=5000" \
     -d "description=Some descriptive text for the debit in the dashboard"

.. code-block:: php

  $bank_account->debits->create(array(
    "amount" => "5000",
    "appears_on_statement_as" => "Statement text",
    "description" => "Some descriptive text for the debit in the dashboard",
  ));


Checkpoint
-----------

Up to this point you should have:

- ✓ Created a ``Card`` and/or ``BankAccount``
- ✓ Initiated a bank account verification
- ✓ Confirmed a bank account verification
- ✓ Charged a ``Card`` and/or ``BankAccount``

Ensure you have met these points before proceeding.


.. container:: box-left

  .. icon-box-widget::
     :box-classes: box box-block box-blue
     :icon-classes: icon icon-arrow-left

     :doc:`Setup <setup>`

.. container:: box-right

  .. read-more-widget::
    :box-classes: box box-block box-blue right
    :icon-classes: icon icon-arrow

    :doc:`Issuing Payouts <payouts>`
 
  .. clear::

|