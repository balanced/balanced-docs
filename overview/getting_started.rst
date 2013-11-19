.. _getting_started:

Getting Started
===============

Saving & Charging Cards
-----------------------

Saving and charging a card with Balanced is both simple and secure. First we tokenize the card with one of Balanced's client libraries. We must exchange the sensitive card info with a token that represents the card in Balanced's system. This keeps all sensitive data out of your system, relieving you of PCI compliance.

Then we simply create Balanced customer object and associate the card to the customer, and charge the card!

These steps are enumerated here:

1. Tokenize the card (via balanced.js_, iOS_ SDK or Android_ SDK)
2. Create the customer and associate the card token to the customer
3. Charge the card

Step 1 is done client-side, steps 2 and 3 are done server-side. Code examples are included below.

.. _balanced.js: https://github.com/balanced/balanced-js
.. _iOS: https://github.com/balanced/balanced-ios
.. _Android: https://github.com/balanced/balanced-android

.. container:: step
  
  **1. Tokenize the card**

  .. raw:: html

    <ul class="nav nav-tabs">
      <li class="active"><a href="#tokenize-js" data-toggle="tab">Javascript</a></li>
      <li><a href="#tokenize-ios" data-toggle="tab">iOS</a></li>
      <li><a href="#tokenize-android" data-toggle="tab">Android</a></li>
    </ul>

  .. container:: tab-content

    .. container:: tab-pane active
      :name: tokenize-js

      .. code-block:: javascript

        var callback = function(response) {
          switch (response.status) {
            case 201:
              // Persist the card on your server with the card uri
              $.ajax({
                url: '/cards',
                data: {card: {uri: response.data['uri']}}
              })
              break;
            case 400:
              // missing field - check response.error for details
              console.log(response.error);
              break;
            case 402:
              // we couldn't authorize the buyer's credit card
              // check response.error for details
              console.log(response.error);
              break;
            case 404:
              // your marketplace URI is incorrect
              console.log(response.error);
              break;
            case 500:
              // Balanced did something bad, please retry the request
              break;
           }
        }

        var $form = $('#credit-card-form');
        var creditCardData = {
          card_number: $form.find('.cc-number').val(),
          expiration_month: $form.find('.cc-em').val(),
          expiration_year: $form.find('.cc-ey').val(),
          security_code: $form.find('.cc-csc').val()
        };

        balanced.card.create(creditCardData, callback)

    .. container:: tab-pane
      :name: tokenize-ios

      .. code-block:: objective-c

        Balanced *balanced = [[Balanced alloc] initWithMarketplaceURI:@"/v1/marketplaces/TEST-MP6E3EVlPOsagSdcBNUXWBDQ"];
        BPCard *card = [[BPCard alloc] initWithNumber:@"4242424242424242" expirationMonth:8 expirationYear:2025 securityCode:@"123"];
        [balanced tokenizeCard:card onSuccess:^(NSDictionary *responseParams) {
          // success
        } onError:^(NSError *error) {
          // failure
        }];

    .. container:: tab-pane
      :name: tokenize-android

      .. code-block:: java

        Balanced balanced = new Balanced(marketplaceURI, context);
        Card card = new Card("4242424242424242", 9, 2014, "123");

        String cardURI = "";

        Card card = new Card("4242424242424242", 9, 2014, "123");
        Balanced balanced = new Balanced(marketplaceURI, context);
        try {
            cardURI = balanced.tokenizeCard(card);
        }
        catch (CardNotValidatedException e) {
            error = e;
        }
        catch (CardDeclinedException e) {
            error = e;
        }
        catch (Exception e) {
            e.printStackTrace();
        }

.. container:: step

  **2. Create the customer and associate the card**

  .. raw:: html

    <ul class="nav nav-tabs">
      <li class="active"><a href="#create-customer-ruby" data-toggle="tab">Ruby</a></li>
      <li><a href="#create-customer-python" data-toggle="tab">Python</a></li>
      <li><a href="#create-customer-php" data-toggle="tab">PHP</a></li>
    </ul>

  .. container:: tab-content

    .. container:: tab-pane active
      :name: create-customer-ruby

      .. code-block:: ruby

        customer = Balanced::Customer.new
        customer.save
        customer.card_uri = params[:card_uri]
        customer.save

    .. container:: tab-pane
      :name: create-customer-python

      .. code-block:: python

        customer = balanced.Customer.find('/v1/customers/CU12eUdTk8OgEj7VbJVFeP0q')
        customer.add_card('/v1/marketplaces/TEST-MP5FKPQwyjvVgTDt7EiRw3Kq/cards/CC15RAm6JJIEIae6bicvlWRw')

    .. container:: tab-pane
      :name: create-customer-php

      .. code-block:: php

        $customer = BalancedCustomer::get("/v1/customers/CU12eUdTk8OgEj7VbJVFeP0q");
        $customer->addCard("/v1/marketplaces/TEST-MP5FKPQwyjvVgTDt7EiRw3Kq/cards/CC15RAm6JJIEIae6bicvlWRw");

.. container:: step

  **3. Charge the Card**

  .. raw:: html

    <ul class="nav nav-tabs">
      <li class="active"><a href="#charge-card-ruby" data-toggle="tab">Ruby</a></li>
      <li><a href="#charge-card-python" data-toggle="tab">Python</a></li>
      <li><a href="#charge-card-php" data-toggle="tab">PHP</a></li>
    </ul>

  .. container:: tab-content

    .. container:: tab-pane active
      :name: charge-card-ruby

      .. code-block:: ruby

        card_uri = current_user.default_card.uri # Retrieve the card URI from local storage
        card = Balanced::Card.find(card_uri)
        card.debit(amount: 10000) # charge the card for $10

    .. container:: tab-pane
      :name: charge-card-python

      .. code-block:: python

        card_uri = current_user.default_card.uri # Retrieve the card URI from local storage
        card = balanced.Card.find(card_uri)
        card.debit(amount: 10000) # charge the card for $10

    .. container:: tab-pane
      :name: charge-card-php

      .. code-block:: php

        $card = BalancedCard::get("/v1/customers/CU12eUdTk8OgEj7VbJVFeP0q/cards/CC15RAm6JJIEIae6bicvlWRw");
        $card->debit(10000);

Paying Bank Accounts
--------------------

The steps for saving customer bank accounts are transferring funds to them are very similar to saving and charging cards.
First we tokenize the bank account details with a client library, then we associate the bank account resource to a Balanced customer,
and then we credit funds to the bank account.

These steps are enumerated here:

1. Tokenize the bank account (via balanced.js_, iOS_ SDK or Android_ SDK)
2. Create the customer (if necessary) and associate the bank account to the customer
3. Charge the card

.. container:: step
  
  **1. Tokenize the bank account**

  .. raw:: html

    <ul class="nav nav-tabs">
      <li class="active"><a href="#tokenize-bank-js" data-toggle="tab">Javascript</a></li>
      <li><a href="#tokenize-bank-ios" data-toggle="tab">iOS</a></li>
      <li><a href="#tokenize-bank-android" data-toggle="tab">Android</a></li>
    </ul>

  .. container:: tab-content

    .. container:: tab-pane active
      :name: tokenize-bank-js

      .. code-block:: javascript

        var callback = function(response) {
          switch (response.status) {
            case 201:
              // Persist the bank account on your server with the card uri
              $.ajax({
                url: '/bank_accounts',
                data: {bank_account: {uri: response.data['uri']}}
              })
              break;
            case 400:
              // missing field - check response.error for details
              console.log(response.error);
              break;
            case 402:
              // we couldn't authorize the buyer's credit card
              // check response.error for details
              console.log(response.error);
              break;
            case 404:
              // your marketplace URI is incorrect
              console.log(response.error);
              break;
            case 500:
              // Balanced did something bad, please retry the request
              break;
           }
        }

        var $form = $('#bank-account-form');
        var bankAccountData = {
          name: $form.find('.ba-name').val(),
          routing_number: $form.find('.ba-routing-number').val(),
          account_number: $form.find('.ba-account-number').val(),
          type: $form.find('select').val() // e.g. 'Checking' or 'Savings' (optional)
        };

        balanced.bankAccount.create(bankAccountData, callback)

    .. container:: tab-pane
      :name: tokenize-bank-ios

      .. code-block:: objective-c

        BPBankAccount *ba = [[BPBankAccount alloc] initWithRoutingNumber:@"053101273" accountNumber:@"111111111111" accountType:BPBankAccountTypeChecking name:@"Johann Bernoulli"];
        [balanced tokenizeBankAccount:ba onSuccess:^(NSDictionary *responseParams) {
          // success
        } onError:^(NSError *error) {
          // failure
        }];

    .. container:: tab-pane
      :name: tokenize-bank-android

      .. code-block:: java

        String bankAccountURI = "";

        Balanced balanced = new Balanced(marketplaceURI, context);
        BankAccount bankAccount = new BankAccount("053101273", "111111111111", AccountType.CHECKING, "Johann Bernoulli");

        try {
            bankAccountURI = balanced.tokenizeBankAccount(bankAccount);
        }
        catch (BankAccountRoutingNumberInvalidException e) {
            error = e;
        }
        catch (Exception e) {
            e.printStackTrace();
        }

.. container:: step
  
  **2. Associate bank account to customer**

  .. raw:: html

    <ul class="nav nav-tabs">
      <li class="active"><a href="#associate-bank-ruby" data-toggle="tab">Ruby</a></li>
      <li><a href="#associate-bank-python" data-toggle="tab">Python</a></li>
      <li><a href="#associate-bank-php" data-toggle="tab">PHP</a></li>
    </ul>

  .. container:: tab-content

    .. container:: tab-pane active
      :name: associate-bank-ruby

      .. code-block:: ruby

        customer = Balanced::Customer.find('/v1/customers/CU7o5OSA8KuFSSjweE54NITe')
        customer.add_bank_account('/v1/bank_accounts/BA34SkYByn3BY564IK12tGEU')

    .. container:: tab-pane
      :name: associate-bank-python

      .. code-block:: python

        customer = balanced.Customer.find('/v1/customers/CU7o5OSA8KuFSSjweE54NITe')
        customer.add_bank_account('/v1/bank_accounts/BA7q1HxYvJr41fVUPk8vMrCm')

    .. container:: tab-pane
      :name: associate-bank-php

      .. code-block:: php

        $customer = BalancedCustomer::get("/v1/customers/CU12eUdTk8OgEj7VbJVFeP0q");
        $customer->addBankAccount("/v1/bank_accounts/BA7q1HxYvJr41fVUPk8vMrCm");

.. container:: step
  
  **3. Transfer funds to bank account**

  .. raw:: html

    <ul class="nav nav-tabs">
      <li class="active"><a href="#credit-bank-ruby" data-toggle="tab">Ruby</a></li>
      <li><a href="#credit-bank-python" data-toggle="tab">Python</a></li>
      <li><a href="#credit-bank-php" data-toggle="tab">PHP</a></li>
    </ul>

  .. container:: tab-content

    .. container:: tab-pane active
      :name: credit-bank-ruby

      .. code-block:: ruby

        bank_account = Balanced::BankAccount.find('/v1/bank_accounts/BA34SkYByn3BY564IK12tGEU')
        bank_account.credit(amount: 1000) # Credit the bank account $10

    .. container:: tab-pane
      :name: credit-bank-python

      .. code-block:: python

        bank_account = balanced.BankAccount.find('/v1/bank_accounts/BA34SkYByn3BY564IK12tGEU')
        bank_account.credit(amount=1000)

    .. container:: tab-pane
      :name: credit-bank-php

      .. code-block:: php

        $bank_account = BalancedBankAccount::get("/v1/bank_accounts/BA34SkYByn3BY564IK12tGEU");
        $bank_account->credit(1000);

Debiting Bank Accounts
----------------------

Balanced allows you to debit from a bank account as well as credit. To debit from a bank account you must create two trial deposits
in the target bank. The owner of the account must then very the deposit amounts. Once this process is complete, you may debit from the bank account.

1. Create trial deposits
2. Customer verifies trial deposits
3. Debit bank account

.. container:: step

  **1. Create trial deposits**

  .. raw:: html

    <ul class="nav nav-tabs">
      <li class="active"><a href="#debit-bank-verification-ruby" data-toggle="tab">Ruby</a></li>
      <li><a href="#debit-bank-verification-python" data-toggle="tab">Python</a></li>
      <li><a href="#debit-bank-verification-php" data-toggle="tab">PHP</a></li>
    </ul>

  .. container:: tab-content

    .. container:: tab-pane active
      :name: debit-bank-verification-ruby

      .. code-block:: ruby

        bank_account = Balanced::BankAccount.find('/v1/bank_accounts/BA6czUjW6j4sMputedTuxXE6')
        verification = bank_account.verify

    .. container:: tab-pane
      :name: debit-bank-verification-python

      .. code-block:: python

        bank_account = balanced.BankAccount.find('/v1/bank_accounts/BA6czUjW6j4sMputedTuxXE6')
        verification = bank_account.verify()

    .. container:: tab-pane
      :name: debit-bank-verification-php

      .. code-block:: php

        $bank_account = Balanced\BankAccount::get("/v1/bank_accounts/BA6czUjW6j4sMputedTuxXE6");
        $verification = $bank_account->verify();

.. container:: step

  **2. Customer verifies trial deposits**

  .. raw:: html

    <ul class="nav nav-tabs">
      <li class="active"><a href="#confirm-bank-verification-ruby" data-toggle="tab">Ruby</a></li>
      <li><a href="#confirm-bank-verification-python" data-toggle="tab">Python</a></li>
      <li><a href="#confirm-bank-verification-php" data-toggle="tab">PHP</a></li>
    </ul>

  .. container:: tab-content

    .. container:: tab-pane active
      :name: confirm-bank-verification-ruby

      .. code-block:: ruby

        verification = Balanced::Verification.find('/v1/bank_accounts/BA6nZLdijPKzQ8RhJNnN1OD6/verifications/BZ6s3ghAmwY5BhnJIrCKSkUo')
        verification.amount_1 = 1
        verification.amount_2 = 1
        verification.save

    .. container:: tab-pane
      :name: confirm-bank-verification-python

      .. code-block:: python

        verification = balanced.BankAccountVerification.find('/v1/bank_accounts/BA6nZLdijPKzQ8RhJNnN1OD6/verifications/BZ6s3ghAmwY5BhnJIrCKSkUo')
        verification.amount_1 = 1
        verification.amount_2 = 1
        verification.save

    .. container:: tab-pane
      :name: confirm-bank-verification-php

      .. code-block:: php

        $verification = Balanced\BankAccountVerification::get("/v1/bank_accounts/BA6nZLdijPKzQ8RhJNnN1OD6/verifications/BZ6s3ghAmwY5BhnJIrCKSkUo");
        $verification->amount_1 = 1;
        $verification->amount_2 = 1;
        $verification->save();

.. container:: step

  **3. Debit bank account**

  .. raw:: html

    <ul class="nav nav-tabs">
      <li class="active"><a href="#debit-bank-account-ruby" data-toggle="tab">Ruby</a></li>
      <li><a href="#debit-bank-account-python" data-toggle="tab">Python</a></li>
      <li><a href="#debit-bank-account-php" data-toggle="tab">PHP</a></li>
    </ul>

  .. container:: tab-content

    .. container:: tab-pane active
      :name: debit-bank-account-ruby

      .. code-block:: ruby

        customer = Balanced::Customer.find('/v1/customers/CU7wGDVh8FjYMPfkPl9SzWAu')
        bank_account = Balanced::BankAccount.find('/v1/bank_accounts/BA6nZLdijPKzQ8RhJNnN1OD6/verifications/BZ6s3ghAmwY5BhnJIrCKSkUo')
        customer.debit(amount: '5000', source_uri: bank_account.uri)

    .. container:: tab-pane
      :name: debit-bank-account-python

      .. code-block:: python

        customer = balanced.Customer.find('/v1/customers/CU7wGDVh8FjYMPfkPl9SzWAu')
        bank_account = balanced.BankAccount.find('/v1/bank_accounts/BA6nZLdijPKzQ8RhJNnN1OD6/verifications/BZ6s3ghAmwY5BhnJIrCKSkUo')
        customer.debit(amount='5000', source_uri=bank_account.uri)

    .. container:: tab-pane
      :name: debit-bank-account-php

      .. code-block:: php

        $customer = Balanced\Customer::get("/v1/customers/CU7wGDVh8FjYMPfkPl9SzWAu")
        $bank_account = Balanced\BankAccount::get("/v1/bank_accounts/BA6nZLdijPKzQ8RhJNnN1OD6/verifications/BZ6s3ghAmwY5BhnJIrCKSkUo")
        $customer.debit("5000", null, null, null, $bank_account)

Collect Your Fee
----------------

Balanced is an ideal solution for marketplace businesses. Payment needs to be accepted from the buyer, a fee is taken by the marketplace, and the
remainder is transferred to the seller.

This can easily be accomplished with Balanced simply by leaving a percentage of each debit collected in
escrow, and transferring to the seller the remainder.

.. container:: step

  **1. Debit buyer**

  **Note**: When you debit the buyer, it's important for compliance reasons to designate the seller for whom the payment is intended.

  .. raw:: html

    <ul class="nav nav-tabs">
      <li class="active"><a href="#marketplace-debit-buyer-ruby" data-toggle="tab">Ruby</a></li>
      <li><a href="#marketplace-debit-buyer-python" data-toggle="tab">Python</a></li>
      <li><a href="#marketplace-debit-buyer-php" data-toggle="tab">PHP</a></li>
    </ul>

  .. container:: tab-content

    .. container:: tab-pane active
      :name: marketplace-debit-buyer-ruby

      .. code-block:: ruby

        card   = Balanced::Card.find('/v1/marketplaces/TEST-MP5FKPQwyjvVgTDt7EiRw3Kq/cards/CC6NiW8huZV4AxYTDJsjOd7k')
        seller = Balanced::Account.find('/v1/customers/CU12eUdTk8OgEj7VbJVFeP0q')
        debit = Balanced::Debit.new(source_uri: card.uri, amount: '1000', on_behalf_of_uri: seller.uri)
        debit.save

    .. container:: tab-pane
      :name: marketplace-debit-buyer-python

      .. code-block:: python

        card = balanced.Card.find('/v1/marketplaces/TEST-MP5FKPQwyjvVgTDt7EiRw3Kq/cards/CC6NiW8huZV4AxYTDJsjOd7k')
        debit = balanced.Debit.new(source_uri=card.uri, amount='1000')
        debit.save

    .. container:: tab-pane
      :name: marketplace-debit-buyer-php

      .. code-block:: php

        $card = Balanced\Card::get("/v1/marketplaces/TEST-MP5FKPQwyjvVgTDt7EiRw3Kq/cards/CC6NiW8huZV4AxYTDJsjOd7k");
        $debit = new Balanced\Debit(array(
          "source_uri" => $card.uri,
          "amount" => "1000"
        ))
        $debit->save()

