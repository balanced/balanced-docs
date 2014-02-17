.. The entry point to the documentation, this is where all the table of
   content files are generated (and as a consequence displayed on the left
   hand side of our navigation menu) x

.. the table of content tree is hidden here because we want to control its
   layout by using the global toctree function provided by sphinx to the
   Jinja2 templates. You can check this out in _templates/layout.html
.. toctree::
  :hidden:
  :glob:

  api/authentication
  api/bank-accounts
  api/bank-account-verifications
  api/cards
  api/credits
  api/customers
  api/debits
  api/events
  api/holds
  api/accounts


API reference
=============

.. container:: header3

   The API conforms to the design principles of Representational State Transfer
   (REST). It supports only the JSON data format.


Using REST
----------

.. container:: compact

  Methods to retrieve data from the Balanced API require an HTTP ``GET`` request.

  Methods that submit data to the Balanced API require an HTTP ``POST`` request.

  Methods that change data in the Balanced API require an HTTP ``PUT`` request.

  Methods that destroy data in the Balanced API require an HTTP ``DELETE`` request.

