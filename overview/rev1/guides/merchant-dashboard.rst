Merchant Dashboard
====================

Balanced provides you with a Merchant Dashboard that allows anyone on your
Marketplace with a Balanced account to view their transactions. You must
explicitly grant access for each user when you want them to access the
Dashboard each time.

Authentication
-----------------

To allow access to the dashboard you must create a login token for the account
of the user and then redirect them to the ``token_uri`` Balanced provides.
All Dashboard activity takes place on **souq.balancedpayments.com**.

Creating a login token
------------------------

.. code-block:: bash

  curl https://souq.balancedpayments.com/v1/logins -X POST \
      -u c99d7a80826f11e18004024f5cb9b783: \ 
      -H 'Content-Type: application/json' \ 
      -d "redirect_uri=https://marketplace.com" \
      -d "account_uri=/v1/marketplaces/TEST-MP903-257-0160/accounts/AC268-579-0932"

The response will look similar to:

.. code-block:: bash

  {
    "token_uri": "https://souq.balancedpayments.com/v1/marketplaces/TEST-MP903-257-0160/accounts/AC268-579-0932?token=MT3fd958daa12011e1a633026ba7c46bae",
    "created_at": "2012-05-18T19:32:48.006955Z",
    "redirect_uri": "https://marketplace.com",
    "account_uri": "/v1/marketplaces/TEST-MP903-257-0160/accounts/AC268-579-0932",
    "expires_at": "2012-05-18T19:42:47.812302Z"
  }

.. note::
  :header_class: alert alert-tab
  :body_class: alert alert-gray

  You must pass your API key secret using basic authentication.

Two parameters must be supplied in the payload:

* ``redirect_uri`` - Where you want us to send the user when they log out of the dashboard.
* ``account_uri`` - The URI of the Balanced account for which you are requesting access.

The two important pieces of information in the response are ``token_uri`` and
``expires_at``. You must redirect the user to ``token_uri`` before the URI expires.

Once the login token has been used, it cannot be used by another user. If your
user wants to access the dashboard again you must generate another token for them.
Once they are on the Merchant Dashboard site their login will exist until they
close their browser window.

Error codes
--------------

The initial creation of the login token will respond with standard HTTP error codes;
400, 401 etc. When you redirect the user to ``token_uri`` the dashboard may
immediately redirect them to the originally supplied ``redirect_uri`` with a
query parameter called ``error``.

The ``error`` parameter will contain the reason for the redirection. Two errors
are possible, these are:

* ``merchant-token-expired`` returned when the token has already expired.
    Balanced will expire the token 10 minutes after creation.
* ``merchant-token-used`` return if the token has already been used. Balanced
    marks the token as used once the user has been redirected to ensure security.