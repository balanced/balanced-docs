.. SUBHEADERS
   glossary / terms
   client library reference
   api reference
   balanced.js
   testing

References
==========

.. _uri_vs_id:

Storing the URI vs ID
---------------------

Do you store the ``uri`` or the ``id`` in your database? \ **Always, always
store the uri**.

The ``uri`` stands for **u**\ niversal **r**\ esource **i**\ dentifier and it's
exactly what it is. An identifier.

Do not attempt to be clever and try to save a few bytes by storing the ``id``
and constructing the ``uri`` later.

This will almost always lead to disaster. A ``uri`` is opaque and Balanced
reserves the right to use HTTP semantics later to change them, so you
should **NEVER** store the ``id``.

Fun fact: our internal statistics show that client libraries that construct
the ``uri`` receive roughly 2 orders of magnitude more ``404`` status codes
from Balanced than clients which use the ``uri`` directly.


Old Documentation
-----------------

Our old documentation is located at `https://docs.balancedpayments.com/api?old <https://docs.balancedpayments.com/api?old>`_

API Reference
-------------

Our API reference is located at `https://docs.balancedpayments.com/api?<https://docs.balancedpayments.com/api?`_


.. Forms
.. steal recurly's form https://js.recurly.com/examples/one_time_transaction.php
.. modify it for processing as well

