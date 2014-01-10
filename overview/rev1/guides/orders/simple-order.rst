Creating a Simple Order
-------------------------

Let's begin by creating a ``Customer`` that represents our merchant.

.. code-block:: ruby

  @merchant = Balanced::Customer.new(
    :name => 'Henry Ford',
    :dob_month => 7,
    :dob_year => 1963,
    :address => {
      :postal_code => '48120'
    }
  ).save

Next, add a bank account to the merchant. In this guide we will tokenize the
bank account directly, however, balanced.js should be used to tokenize bank
accounts in production. Refer to the balanced.js guide for more
information on implementing balanced.js in your application.

.. code-block:: ruby

  @bank_account = @merchant.bank_accounts.create(
    :name => 'William Henry Cavendish III',
    :routing_number => '321174851',
    :account_number => '0987654321',
    :type => 'checking'
  )


Now create a buyer and add a card to it. Again, in this guide we will tokenize
the card directly, however, balanced.js should be used to tokenize credit cards
in production. Refer to the balanced.js guide for more information on
implementing balanced.js in your application.

.. code-block:: ruby

  @buyer = Balanced::Customer.new(
    :name => 'John Buyer'
  ).save
  
  @card = @buyer.cards.create(
    :number => '5105105105105100',
    :expiration_month => '12',
    :expiration_year => '2020',
    :cvv => '123'
  )

Next, create an ``Order``.

.. code-block:: ruby

  @order = @merchant.create_order


At this point we have a merchant ``Customer`` with a bank account, a buyer
`Customer` with a credit card, and an "empty" ``Order``.

Let's give the order a description and some meta so it's easier to remember
what it was for. Of course, this information can also be specified when creating
and Order.

.. code-block:: ruby

  @order.description = 'Item description'
  @order.meta = {
    'item_url' => 'https://neatitems.com/12342134123'
  }
  @order.save

Let's debit the buyer for this Order. This is accomplished by debiting a
specific card, in this case, the buyer's, through the Order.

.. code-block:: ruby

  debit = @order.debit_from(
    :source => @card,
    :amount => 10000
  )

At this point, if we inspect the Order, we'll see it now has an ``amount`` of
10000 and an escrowed amount of 10000. `amount` is the total amount of the
Order. ``amount_escrowed`` is the amount available for issuing payouts.

.. code-block:: ruby

   @order.reload          # reload the order to get recent changes
   @order.amount          # will be 10000
   @order.amount_escrowed # will be 10000


Let's issue a payout (credit) to our merchant.

.. code-block:: ruby

  @order.credit_to(
    :destination => @bank_account,
    :amount => 8000
  )

Now when inspecting the order object we'll see it still has an ``amount`` of 10000
and ``amount_escrowed`` is now 2000.

.. code-block:: ruby

   @order.reload          # reload the order to get recent changes
   @order.amount          # will be 10000
   @order.amount_escrowed # will be 2000

We can now retrieve all of the order's debits with:

.. code-block:: ruby

  @order.debits

Likewise, we can retrieve all of the order's credits with:

.. code-block:: ruby

  @order.credits