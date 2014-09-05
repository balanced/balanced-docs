.. _resources:

Resources
=========

.. _resources.test-credit-cards:

Test credit card numbers
------------------------

.. note::
  :header_class: alert alert-tab
  :body_class: alert alert-green

  These cards will be accepted in our system only for a **TEST** marketplace.
  **Do not use these card numbers in Production marketplaces.**

.. note::
  :header_class: alert alert-tab-yellow
  :body_class: alert alert-yellow

  Validation of cards does not occur until an authenticated operation is performed against it.
  Therefore, simulated results will not be reflected during tokenization.

.. cssclass:: table

  ============== =========================== ================ ==============================
   Card Brand          Number                       CVV         Result
  ============== =========================== ================ ==============================
  ``VISA``        ``4111111111111111``            ``123``       Success
  ``MasterCard``  ``5105105105105100``            ``123``       Success
  ``AMEX``        ``341111111111111``             ``1234``      Success
  ``VISA``        ``4342561111111118``            ``123``       Creditable Card
  ``VISA``        ``4444444444444448`` [#]_       ``123``       Processor Failure
  ``VISA``        ``4222222222222220`` [#]_       ``123``       Tokenization Error
  ``MasterCard``  ``5112000200000002``            ``200``       CVV Match Fail
  ``VISA``        ``4457000300000007``            ``901``       CVV Unsupported
  ``Discover``    ``6500000000000002``            ``123``       Disputed Charge
  ============== =========================== ================ ==============================

.. [#] Simulate a card which can be tokenized but will not be accepted for creating
       holds or debits. This type of failure is what you would expect if you try to
       create a hold on a card with insufficient funds.
.. [#] To simulate a card which cannot be tokenized but passes a LUHN check. You could
       expect this failure when a user tried to enter in a credit card which used to
       work but has been canceled.


.. _resources.test-bank-accounts:

Test bank account numbers
-------------------------

Balanced provides various utilities to aid you in testing your :ref:`guides.credits`
integration.

When integrating payouts, it's worth noting that incorrect bank routing numbers
are a very commonly encountered error as Balanced does real-time checks against
the `FedACH directory`_.

To aid you while integrating, Balanced provides special routing and
account numbers that can simulate various scenarios that can go wrong.

.. list-table::
   :widths: 15 20 40
   :header-rows: 1
   :class: table

   * - Routing Number
     - Account Number
     - Scenario
   * - ``100000007``
     - ``8887776665555``
     - Invalid Routing Number
   * - ``111111118``
     - ``8887776665555``
     - Invalid Routing Number
   * - ``021000021``
     - ``9900000000``
     - Transitions status to ``pending``
   * - ``321174851``
     - ``9900000001``
     - Transitions status to ``pending``
   * - ``021000021``
     - ``9900000002``
     - Transitions status to ``succeeded``
   * - ``321174851``
     - ``9900000003``
     - Transitions status to ``succeeded``
   * - ``021000021``
     - ``9900000004``
     - Transitions status to ``failed``
   * - ``321174851``
     - ``9900000005``
     - Transitions status to ``failed``


.. _resources.test-identity-verification:

Customer identity verification
---------------------------------------

Merchants (sellers) to whom you wish to pay out must be underwritten as per `KYC regulations`_.
``Customer`` resources have a ``merchant_status`` attribute for determining
the Customer's underwritten status.

``merchant_status`` will be one of: ``underwritten``, ``need-more-information``,
or ``rejected``.

.. cssclass:: dl-horizontal dl-params dl-param-values dd-noindent dd-marginbottom

  ``underwritten``
    An identity match was found.
  ``need-more-information``
    Based on the information supplied, an identity match was not found. Try supplying more information.
  ``rejected``
    The identity is restricted from transacting.


Testing merchant status
~~~~~~~~~~~~~~~~~~~~~~~~~~

Supply address and date of birth information to trigger an ``underwritten`` response.

The following will set ``merchant_status`` to ``underwritten``

.. code-block:: javascript

  {
      "name": "Henry Ford",
      "dob_month": 07,
      "dob_year": 1985,
      "address": {
          "postal_code": "48120"
      }
  }


The following will set ``merchant_status`` to ``need-more-information``

.. code-block:: javascript

  {
      "name": "Henry Ford",
      "dob_month": 07,
      "dob_year": 1985
  }



Funding Instrument Fingerprint
--------------------------------

Every ``Card`` and ``BankAccount`` resource has a ``fingerprint`` attribute
that can be used to check if a card has already been tokenized.

For credit cards, ``fingerprint`` is calculated using ``card_number`` and the
card expiration date.

For bank accounts, ``fingerprint`` is calculated using ``account_number``,
``routing_number``, ``name``, and ``type``.


.. _resources.address-verification-service:

Address Verification Service (AVS)
-----------------------------------

AVS, Address Verification Service, provides a means to verify that the address
supplied during card tokenization matches the address of the credit card.

Supplying an ``address`` object containing at least a ``postal_code`` attribute
during tokenization will initiate an AVS check. Supplying ``line1`` in the address
object will also initiate a street match check.

Additionally, ``avs_result`` may be examined to ascertain more detailed
information about the address verification attempt. 

.. note::
  :header_class: alert alert-tab-yellow
  :body_class: alert alert-yellow

  - ``postal_code`` is required when supplying an address object.
  - AVS is not reliable outside the U.S.


``avs_street_match`` will be one of: ``yes``, ``no``, ``unsupported``

.. cssclass:: dl-horizontal dl-params dl-param-values dd-noindent dd-marginbottom

  ``yes``
    The supplied street address matched the credit card's street address.
  ``no``
    The supplied street address did not match the credit card's street address.
  ``unsupported``
    No street address was supplied or a street address match was not supported.


``avs_postal_match`` will be one of: ``yes``, ``no``, ``unsupported``

.. cssclass:: dl-horizontal dl-params dl-param-values dd-noindent dd-marginbottom

  ``yes``
    The supplied postal code matched the credit card's postal code.
  ``no``
    The supplied postal code did not match the credit card's postal code.
  ``unsupported``
    No postal code was supplied or a postal code match was not supported.


Test Postal Codes
~~~~~~~~~~~~~~~~~~~~

Postal code test values:

.. cssclass:: table

  ============== ====================================
   Postal Code    Result                    
  ============== ====================================
  ``94301``        AVS Postal code matches      
  ``90210``        AVS Postal code does not match
  ``90211``        AVS Postal code is unsupported
  ============== ====================================


Test AVS Addresses
~~~~~~~~~~~~~~~~~~~~~

.. cssclass:: table

  =================== ================== ===========================
  Address line1        Postal Code        Result             
  =================== ================== ===========================
  ``965 Mission St``   ``94103``          AVS street matches
  ``21 Jump St``       ``90210``          AVS street does not match
  =================== ================== ===========================



.. _resources.card-verification-value:

Card Verification Value (CVV)
-------------------------------

``Card`` resources have a ``cvv_match`` attribute containing the CVV check result,
which provides a means to verify that the ``cvv`` supplied during card tokenization
matches the CVV for the credit card. It's strongly recommended you do
not process transactions with cards that fail this check.

Any authenticated request performed for the first time on a tokenized ``Card`` claims
the ``Card`` to the marketplace and triggers verifications for the ``Card``. If you wish to check
the CVV match result before attempting to charge the ``Card``, first perform an authenticated request
such as a ``GET`` request on the ``Card``, or associate the ``Card`` to a ``Customer`` resource.

Additionally, ``cvv_result`` can be examined to ascertain more detailed information about the match attempt.

``cvv_match`` will be one of: ``yes``, ``no``, ``unsupported``

.. cssclass:: dl-horizontal dl-params dl-param-values dd-noindent dd-marginbottom

  ``yes``
    The supplied CVV matched the credit card's CVV.
  ``no``
    The supplied CVV did not match the credit card's CVV.
  ``unsuported``
    No CVV was supplied or a CVV match was not supported.



.. _FedACH directory: https://www.fededirectory.frb.org
.. _KYC regulations: https://en.wikipedia.org/wiki/Know_your_customer