Authentication
==============

Authenticating to Balanced
--------------------------

To authenticate with Balanced, you will need the API key ``secret`` provided
from the `dashboard`_. You have to use `http basic access
authentication`_. Your key has to be set as the username. A password
is not required for simplicity.

.. note::
   :header_class: alert alert-tab
   :body_class: alert alert-gray

   Please keep your private keys secure and do **NOT** share them with anyone.

   For security concerns regarding submitted data, all your requests **MUST**
   occur via `https`_.

   When asking for help in the IRC channel, **NEVER** give out your api key's
   ``secret``.


.. _https:
.. _http basic access authentication: http://en.wikipedia.org/wiki/HTTP_Secure
.. _dashboard: https://www.balancedpayments.com/dashboard
