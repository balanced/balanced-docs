.. _resources:

Resources
=========

.. _resources.test_credit_cards:

Test credit card numbers
------------------------

These cards will be accepted in our system only for a **TEST** marketplace.

.. cssclass:: table

  ============== =========================== ================ ==============================
   Card Brand          Number                  Security Code     Result
  ============== =========================== ================ ==============================
  ``VISA``        ``4111111111111111``            ``123``       SUCCESS
  ``MasterCard``  ``5105105105105100``            ``123``       SUCCESS
  ``AMEX``         ``341111111111111``           ``1234``       SUCCESS
  ``VISA``        ``4444444444444448`` [#]_       ``123``       SIMULATE PROCESSOR FAILURE
  ``VISA``        ``4222222222222220`` [#]_       ``123``       SIMULATE TOKENIZATION ERROR
  ============== =========================== ================ ==============================

.. [#] Simulate a card which can be tokenized but will not be accepted for creating
       holds or debits. This type of failure is what you would expect if you try to
       create a hold on a card with insufficient funds.
.. [#] To simulate a card which cannot be tokenized but passes a LUHN check. You could
       expect this failure when a user tried to enter in a credit card which used to
       work but has been canceled.

.. _resources.test_bank_accounts:

Test bank account numbers
-------------------------

Balanced provides various utilities to aid you in testing your :ref:`payouts`
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
     - Transitions state to ``pending``
   * - ``321174851``
     - ``9900000001``
     - Transitions state to ``pending``
   * - ``021000021``
     - ``9900000002``
     - Transitions state to ``paid`` (credits) or ``succeeded`` (debits)
   * - ``321174851``
     - ``9900000003``
     - Transitions state to ``paid`` (credits) or ``succeeded`` (debits)
   * - ``021000021``
     - ``9900000004``
     - Transitions state to ``failed``
   * - ``321174851``
     - ``9900000005``
     - Transitions state to ``failed``


.. _resources.test-identity-verification:

Test identity verification
--------------------------

``Customer`` resources have an ``is_identity_verified`` attribute.

Omit address data to trigger a ``false`` response. Supply address data
to trigger a ``true`` response.

The following will set ``is_identity_verified`` to ``true``

.. code-block:: javascript

  {
      'name': 'Henry Ford',
      'dob': '1863-07',
      'address': {
          'postal_code': '48120'
      }
  }


The following will set ``is_identity_verified`` to ``false``

.. code-block:: javascript

  {
      'name': 'Henry Ford',
      'dob': '1863-07'
  }


.. _resources.request-logs:

Request Logs
------------

As you integrate and test :ref:`payouts`, you may find it useful to view
all your sanitized API request logs. They are viewable via the logs section
in the `dashboard`_

.. _dashboard: https://dashboard.balancedpayments.com/

.. SUBHEADERS
   glossary / terms
   client library reference
   api reference
   balanced.js
   testing


The Hash Attribute
------------------

Every ``Card`` and ``BankAccount`` resource has an attribute than can be used
to check if the same card is being added again.

For credit cards, this is the ``hash`` attribute. This is calculated using
``card_number`` and the expiration.

For bank accounts, this is the ``fingerprint`` attribute. This is calculated using
``account_number``, ``routing_number``, ``name``, and ``type``.


.. _resources.address-verification-service:

Address Verification Service
----------------------------

AVS, **A**\ ddress **V**\ erification **S**\ ervice, provides a means to
verify that the postal_code supplied during card tokenization matches the
billing zip code of the credit card.

Supplying a ``postal_code`` during tokenization initiates the AVS check.
The ``Card`` will have a ``postal_code_check`` attribute containing the
AVS check result.

``postal_code_check`` will be one of: ``passed``, ``failed``, ``unknown``


.. _resources.card-security-code:

Card Security Code
------------------

CSC, **C**\ ard **S**\ ecurity **C**\ ode, provides a means to verify that the
``security_code`` supplied during card tokenization matches the security_code
for the credit card. The ``Card`` will have a ``security_code_check``
attribute containing the CSC check result. It's strongly recommended you do
not process transactions with cards that fail this check.

``security_code_check`` will be one of: ``passed``, ``failed``, ``unknown``


.. _FedACH directory: https://www.fededirectory.frb.org
