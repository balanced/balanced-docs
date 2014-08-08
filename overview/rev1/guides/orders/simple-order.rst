Creating a Simple Order
-------------------------

.. admonition:: References
  :header_class: alert alert-tab full-width alert-tab-persianBlue60
  :body_class: alert alert-persianBlue20

  .. cssclass:: mini-header

    API Specification

  .. cssclass:: list-noindent

    - `Orders Collection <https://github.com/balanced/balanced-api/blob/master/fixtures/orders.json>`_
    - `Order Resource <https://github.com/balanced/balanced-api/blob/master/fixtures/_models/order.json>`_

  .. cssclass:: mini-header

    API Reference

  .. cssclass:: list-noindent

    - `Create a Customer </1.1/api/customers/#create-a-customer>`_
    - `Create a Bank Account (Direct) </1.1/api/bank-accounts/#create-a-bank-account-direct>`_
    - `Create an Order </1.1/api/orders/#create-an-order>`_
    - `Update an Order </1.1/api/orders/#update-an-order>`_
    - `Create a Credit </1.1/api/credits/#create-a-credit>`_


By the end of this guide, you should understand how to do following:

.. cssclass:: list-noindent

  - \* Create a ``Customer`` representing a seller (merchant) and associate a ``BankAccount`` to it.
  - \* Create a ``Customer`` representing a buyer and associate a ``BankAccount`` to it.
  - \* Create an ``Order``
  - \* Update an ``Order``
  - \* Create an order debit
  - \* Check the order ``amount``
  - \* Check the order ``amount_escrowed``
  - \* Issue a credit from an ``Order`` to a seller
  - \* Issue a credit from an ``Order`` to the marketplace bank account

|

Let's begin by creating a ``Customer`` that represents our merchant.

.. container:: section-ruby

  .. literalinclude:: ruby/simple/customer-create.rb
     :language: ruby

.. container:: section-python

  .. literalinclude:: python/simple/customer-create.py
     :language: python

.. container:: section-bash

  .. literalinclude:: curl/simple/customer-create.sh
     :language: bash

.. container:: section-php

  .. literalinclude:: php/simple/customer-create.php
    :language: php

.. container:: section-csharp

  .. literalinclude:: csharp/simple/customer-create.cs
    :language: csharp


Next, add a bank account to the merchant. In this guide we will tokenize the
bank account directly, however, balanced.js should be used to tokenize bank
accounts in production. Refer to the balanced.js guide for more
information on implementing balanced.js in your application.

.. container:: section-ruby

  .. literalinclude:: ruby/simple/bank-account-create.rb
     :language: ruby

.. container:: section-python

  .. literalinclude:: python/simple/bank-account-create.py
     :language: python

.. container:: section-bash

  .. literalinclude:: curl/simple/bank-account-create.sh
     :language: bash

.. container:: section-php

  .. literalinclude:: php/simple/bank-account-create.php
    :language: php

.. container:: section-csharp

  .. literalinclude:: csharp/simple/bank-account-create.cs
    :language: csharp


Now create a buyer and add a card to it. Again, in this guide we will tokenize
the card directly, however, balanced.js should be used to tokenize credit cards
in production. Refer to the balanced.js guide for more information on
implementing balanced.js in your application.


.. container:: section-ruby

  .. literalinclude:: ruby/simple/create-buyer-and-card.rb
     :language: ruby

.. container:: section-python

  .. literalinclude:: python/simple/create-buyer-and-card.py
     :language: python

.. container:: section-bash

  .. literalinclude:: curl/simple/create-buyer-and-card.sh
     :language: bash

.. container:: section-php

  .. literalinclude:: php/simple/create-buyer-and-card.php
    :language: php

.. container:: section-csharp

  .. literalinclude:: csharp/simple/create-buyer-and-card.cs
    :language: csharp


Next, create an ``Order``.

.. container:: section-ruby

  .. literalinclude:: ruby/simple/order-create.rb
     :language: ruby

.. container:: section-python

  .. literalinclude:: python/simple/order-create.py
     :language: python

.. container:: section-bash

  .. literalinclude:: curl/simple/order-create.sh
     :language: bash

.. container:: section-php

  .. literalinclude:: php/simple/order-create.php
    :language: php

.. container:: section-csharp

  .. literalinclude:: csharp/simple/order-create.cs
    :language: csharp


At this point we have a merchant ``Customer`` with a bank account, a buyer
`Customer` with a credit card, and an "empty" ``Order``.

Let's give the order a description and some meta so it's easier to remember
what it was for. Of course, this information can also be specified when creating
and Order.

.. container:: section-ruby

  .. literalinclude:: ruby/simple/order-update.rb
     :language: ruby

.. container:: section-python

  .. literalinclude:: python/simple/order-update.py
     :language: python

.. container:: section-bash

  .. literalinclude:: curl/simple/order-update.sh
    :language: bash

.. container:: section-php

  .. literalinclude:: php/simple/order-update.php
    :language: php

.. container:: section-csharp

  .. literalinclude:: csharp/simple/order-update.cs
    :language: csharp


Let's debit the buyer for this Order. This is accomplished by debiting a
specific card, in this case, the buyer's, through the Order.

.. container:: section-ruby

  .. literalinclude:: ruby/simple/order-debit.rb
     :language: ruby

.. container:: section-python

  .. literalinclude:: python/simple/order-debit.py
     :language: python

.. container:: section-bash

  .. literalinclude:: curl/simple/order-debit.sh
     :language: bash

.. container:: section-php

  .. literalinclude:: php/simple/order-debit.php
    :language: php

.. container:: section-csharp

  .. literalinclude:: csharp/simple/order-debit.cs
    :language: csharp


At this point, if we inspect the Order, we'll see it now has an ``amount`` of
10000 and an escrowed amount of 10000. `amount` is the total amount of the
Order. ``amount_escrowed`` is the amount available for issuing payouts.

.. container:: section-ruby

  .. literalinclude:: ruby/simple/order-amount-escrowed.rb
     :language: ruby

.. container:: section-python

  .. literalinclude:: python/simple/order-amount-escrowed.py
     :language: python

.. container:: section-bash

  .. literalinclude:: curl/simple/order-amount-escrowed.sh
     :language: bash

.. container:: section-php

  .. literalinclude:: php/simple/order-amount-escrowed.php
    :language: php

.. container:: section-csharp

  .. literalinclude:: csharp/simple/order-amount-escrowed.cs
    :language: csharp


Let's issue a payout (credit) to our merchant.

.. container:: section-ruby

  .. literalinclude:: ruby/simple/order-credit.rb
     :language: ruby

.. container:: section-python

  .. literalinclude:: python/simple/order-credit.py
     :language: python

.. container:: section-bash

  .. literalinclude:: curl/simple/order-credit.sh
     :language: bash

.. container:: section-php

  .. literalinclude:: php/simple/order-credit.php
    :language: php


.. container:: section-csharp

  .. literalinclude:: csharp/simple/order-credit.cs
    :language: csharp


Now when inspecting the order object we'll see it still has an ``amount`` of 10000
and ``amount_escrowed`` is now 2000.

.. container:: section-ruby

  .. literalinclude:: ruby/simple/order-amount-escrowed.rb
     :language: ruby

.. container:: section-python

  .. literalinclude:: python/simple/order-amount-escrowed.py
     :language: python

.. container:: section-bash

  .. literalinclude:: curl/simple/order-amount-escrowed.sh
     :language: bash

.. container:: section-php

  .. literalinclude:: php/simple/order-amount-escrowed.php
    :language: php

.. container:: section-csharp

  .. literalinclude:: csharp/simple/order-amount-escrowed.cs
    :language: csharp


We can now retrieve all of the order's debits with:

.. container:: section-ruby

  .. literalinclude:: ruby/simple/order-debits-fetch.rb
     :language: ruby

.. container:: section-python

  .. literalinclude:: python/simple/order-debits-fetch.py
     :language: python

.. container:: section-bash

  .. literalinclude:: curl/simple/order-debits-fetch.sh
    :language: bash

.. container:: section-php

  .. literalinclude:: php/simple/order-debits-fetch.php
    :language: php

.. container:: section-csharp

  .. literalinclude:: csharp/simple/order-debits-fetch.cs
    :language: csharp


Likewise, we can retrieve all of the order's credits with:

.. container:: section-ruby

  .. literalinclude:: ruby/simple/order-credits-fetch.rb
     :language: ruby

.. container:: section-python

  .. literalinclude:: python/simple/order-credits-fetch.py
     :language: python

.. container:: section-bash

  .. literalinclude:: curl/simple/order-credits-fetch.sh
     :language: bash

.. container:: section-php

  .. literalinclude:: php/simple/order-credits-fetch.php
    :language: php

.. container:: section-csharp

  .. literalinclude:: csharp/simple/order-credits-fetch.cs
    :language: csharp


Checkpoint
~~~~~~~~~~~~

You should understand how to do following:

.. cssclass:: list-noindent

  - ✓ Create a ``Customer`` representing a seller (merchant) and associate a ``BankAccount1`` to it.
  - ✓ Create a ``Customer`` representing a buyer and associate a ``BankAccount`` to it.
  - ✓ Create an ``Order``
  - ✓ Update an ``Order``
  - ✓ Create an order debit
  - ✓ Check the order ``amount``
  - ✓ Check the order ``amount_escrowed``
  - ✓ Issue a credit from an ``Order`` to a seller
  - ✓ Issue a credit from an ``Order`` to the marketplace bank account
