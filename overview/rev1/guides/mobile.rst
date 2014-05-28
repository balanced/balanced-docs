Mobile
===========

Balanced provides libraries for `iOS`_ and `Android`_ development.

**Mobile libraries provide only the ability to tokenize funding instruments in Balanced.**

In most cases, mobile devices should communicate with your servers for all operations other
than tokenization and not directly with Balanced for several reasons. First, most of the
Balanced API requires authenticated requests. Therefore, your API key must be supplied
for each such request and should not be stored on mobile devices, even in compiled code.
Funding instrument tokenization is one of the only API requests that doesn't require
authentication. Second, data persistence on mobile devices is often unreliable, insecure,
and ephemeral. You’ll likely want information stored in a central location, your servers,
where you can ensure its integrity from an authoritative source. Tokenizing funding
instruments from a mobile device directly to Balanced ensures the sensitive information
never touches your servers, thereby lessening your PCI compliance burden.

The flow for mobile tokenization should be implemented as in this manner:

.. cssclass:: list-noindent

  - \- Add the Balanced mobile library for the device's platform
  - \- Obtain funding instrument information via a simple form view
  - \- Send funding instrument information from mobile device to Balanced API
  - \- Obtain the ``href`` from the successful tokenization response
  - \- Send the href to your server
  - \- Perform an authenticated request on the funding instrument href to claim it for your marketplace. This can be a simple GET/fetch or associate it to a Customer.

|

.. image:: //static/img/mobile-tokenization-flow.png

|

|

.. admonition:: References
  :header_class: alert alert-tab full-width alert-tab-persianBlue60
  :body_class: alert alert-green alert-persianBlue20
  
  .. cssclass:: mini-header
  
    API

  .. cssclass:: list-noindent

    - `Create a Card </1.1/api/cards/#create-a-card-direct>`_
    - `Create a Bank Account </1.1/api/bank-accounts/#create-a-bank-account-direct>`_

|


balanced-ios
---------------------------

balanced-ios is an iOS static library for tokenizing funding instruments in Balanced.

Supported OS versions:

- >= iOS 6.1

Support architectures:

- Simulator
- armv7
- armv7s
- arm64

|

.. admonition:: Requirements
  :header_class: alert alert-tab full-width alert-tab-yellow
  :body_class: alert alert-green alert-yellow

  .. cssclass:: list-noindent no-border

    - ARC
    - CoreTelephony.framework

|

Setup
~~~~~~~~~~

.. cssclass:: list-noindent

  - \- `Download the latest pre-built library`_ and extract it
  - \- Copy ``balanced.a`` to your project and add it to Build Phases -> Link Binary With Libraries
  - \- Add ``CoreTelephony.framework`` to Build Phases -> Link Binary With Libraries
  - \- Copy the include folder to your project (or include/balanced to your existing include folder). Drag the folder to your project to add the references. The includes folder is automatically included in the project's header search path. **If you copy the files to a location other than includes you'll need to add the path to User Header Search Paths in your project settings.**

|

Next, import the headers:

.. code-block:: objc

  #import "Balanced.h"
  #import "BPBankAccount.h"
  #import "BPCard.h"


Now create a Balanced instance:

.. code-block:: objc

  Balanced *balanced = [[Balanced alloc] init];


Create (tokenize) a card
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Example request:

.. code-block:: objc

  NSDictionary *address = @{
                            @"line1":@"123 Main Street",
                            @"postal_code":@"11111"
                           };
  NSDictionary *optionalFields = @{
                                   @"address":address,
                                   @"cvv":@"123",
                                   @"name":@"Johann Bernoulli"
                                  };
  Balanced *balanced = [[Balanced alloc] init];
  [balanced createCardWithNumber:@"4242424242424242"
                 expirationMonth:8
                  expirationYear:2025
                       onSuccess:^(NSDictionary *response) {
                         // handle success
                       }
                         onError:^(NSError *error) {
                           // handle failure
                         }
                  optionalFields:optionalFields];


Example response (NSDictionary):

.. code-block:: javascript

  {
      cards =     (
                  {
              href = "/cards/CC4EyXaOirNaK9wSuynsh8VB";
              id = CC4EyXaOirNaK9wSuynsh8VB;
              links =             {
              };
          }
      );
      links =     {
      };
      status = 201;
  }


On a successful response, obtain the card href:

.. code-block:: objc

  NSString *cardHref = [[[response objectForKey:@"cards"] objectAtIndex:0] valueForKey:@"href"];


Now send the href to your server and claim it with an authenticated request such as a GET,
or associate it to a ``Customer``.


Create (tokenize) a bank account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Example request:

.. code-block:: objc

  NSDictionary *optionalFields = @{
                                   @"meta":@{
                                            @"invoice_id":@"2154687864"
                                           }
                                   };
  [balanced createBankAccountWithRoutingNumber:@"053101273"
                                 accountNumber:@"111111111111"
                                   accountType:BPBankAccountTypeChecking
                                          name:@"Johann Bernoulli"
                                     onSuccess:^(NSDictionary *responseParams) {
                                       // handle success
                                     }
                                       onError:^(NSError *error) {
                                         // handle error
                                       }
                                optionalFields:optionalFields];


Example response (NSDictionary):

.. code-block:: javascript

  {
      bank_accounts =     (
                  {
              href = "/bank_accounts/BA7uJx0yPIqAZXxpiKq5LY2y";
              id = BA7uJx0yPIqAZXxpiKq5LY2y;
              links =             {
              };
          }
      );
      links =     {
      };
      status = 201;
  }


balanced-android
----------------------------

balanced-android is an `Android Library Project`_ for tokenizing funding instruments in Balanced.


.. admonition:: Requirements
  :header_class: alert alert-tab full-width alert-tab-yellow
  :body_class: alert alert-green alert-yellow

  .. cssclass:: list-noindent

    - `gson 2.2.4`_
    - `httpclient 4.2.1`_
    
    These are installable via maven.


Setup
~~~~~~~

Since editor usage and project setup varies, follow the recommended procedure for adding an Android
Library Project in your application.

Next, import the headers:

.. code-block:: android

  import com.balancedpayments.android.Balanced; // Tokenizing methods
  import com.balancedpayments.android.Card; // Credit cards
  import com.balancedpayments.android.BankAccount; // Bank accounts
  import com.balancedpayments.android.exception.*; // Exceptions


Now create a Balanced instance:

.. code-block:: android

  // appContext is an instance of android.content.Context from getContext()
  Balanced balanced = new Balanced(appContext);


Create (tokenize) a card
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Example request:

.. code-block:: android

  Map<String, Object> response = null;

  HashMap<String, String> address = new HashMap<String, String>();
  optionalFields.put("line1", "123 Street");
  optionalFields.put("state", "CA");
  optionalFields.put("city", "San Francisco");
  optionalFields.put("postal_code", "94102");

  HashMap<String, Object> optionalFields = new HashMap<String, String>();
  optionalFields.put("name", "Johann Bernoulli");
  optionalFields.put("cvv", "123");
  optionalFields.put("address", address);
  
  try {
     response = balanced.createCard("4242424242424242", 9, 2014, optionalFields);
  }
  catch (CreationFailureException e) {}
  catch (FundingInstrumentNotValidException e) {}


Example response:

.. code-block:: javascript

  {
      "cards": [
          {
              "href": "/cards/CC2sx82S4zn4ECxbOloIRDxS",
              "id": "CC2sx82S4zn4ECxbOloIRDxS",
              "links": {}
          }
      ],
      "links": {},
      "status_code": 201
  }


On a successful response, obtain the card href:

.. code-block:: android

  Map<String, Object> cardResponse = (Map<String, Object>) ((ArrayList)response.get("cards")).get(0);
  String cardHref = cardResponse.get("href");


Now send the href to your server and claim it with an authenticated request such as a GET,
or associate it to a ``Customer``.


Create (tokenize) a bank account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Example request:

.. code-block:: android

  Map<String, Object> response = null;

  HashMap<String, String> address = new HashMap<String, String>();
  optionalFields.put("line1", "123 Street");
  optionalFields.put("state", "CA");
  optionalFields.put("city", "San Francisco");
  optionalFields.put("postal_code", "94102");

  HashMap<String, Object> optionalFields = new HashMap<String, String>();
  optionalFields.put("name", "Johann Bernoulli");
  optionalFields.put("cvv", "123");
  optionalFields.put("address", address);

  try {
     response = balanced.createBankAccount("021000021", "9900000002",
       AccountType.CHECKING, "Johann Bernoulli", optionalFields);
  }
  catch (CreationFailureException e) {}
  catch (FundingInstrumentNotValidException e) {}


Example response:

.. code-block:: javascript

  {
      "bank_accounts": [
          {
              "href": "/bank_accounts/BA7uJx0yPIqAZXxpiKq5LY2y",
              "id": "BA7uJx0yPIqAZXxpiKq5LY2y",
              "links": {}
          }
      ],
      "links": {},
      "status_code": 201
  }


On a successful response, obtain the card href:

.. code-block:: android

  Map<String, Object> bankAccountResponse = (Map<String, Object>) ((ArrayList)response.get("bank_accounts")).get(0);
  String bankAccountHref = bankAccountResponse.get("href");


Now send the href to your server and claim it with an authenticated request such as a GET,
or associate it to a ``Customer``.


.. _Download the latest pre-built library: https://github.com/balanced/balanced-ios/releases
.. _iOS: https://github.com/balanced/balanced-ios
.. _Android: https://github.com/balanced/balanced-android
.. _Android Library Project: https://developer.android.com/tools/projects/index.html#LibraryProjects
.. _gson 2.2.4: http://code.google.com/p/google-gson/
.. _httpclient 4.2.1: http://hc.apache.org/