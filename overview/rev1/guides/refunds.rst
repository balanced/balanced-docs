Working with Refunds
======================

You can refund a debit up to its original amount, so that means you can partially
refund a debit as well.

In order for a refund to go through successfully, you *must* have enough money
in :ref:`implicit escrow <mp.escrow>` to cover your refund.

.. note::
  :header_class: alert alert-tab
  :body_class: alert alert-gray

  For credit cards it typically takes one business day for refunds to
  be reflected on a card statement, but it's possible for the issuing bank to
  take as many as five business days to process a refund.


Here are some scenarios:

Full Refund
~~~~~~~~~~~

Let's say you've debited an account for $20.00

* Your marketplace's `dashboard <https://dashboard.balancedpayments.com/#/marketplaces/>`_ escrow balance says $20.00
* You issue a refund for $20.00
* Your marketplace's `dashboard <https://dashboard.balancedpayments.com/#/marketplaces/>`_ escrow balance says $0.00


Partial Refund
~~~~~~~~~~~~~~

You can also perform multiple partial refunds up to the original amount.

Let's say you've debited an account for $20.00

* Your marketplace's `dashboard <https://dashboard.balancedpayments.com/#/marketplaces/>`_ escrow balance says $20.00
* You issue a refund for $10.00
* Your marketplace's `dashboard <https://dashboard.balancedpayments.com/#/marketplaces/>`_ escrow balance says $10.00
* You issue another refund for $5.00
* Your marketplace's `dashboard <https://dashboard.balancedpayments.com/#/marketplaces/>`_ escrow balance says $5.00

Not Enough Funds to Refund
~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's say you've debited an account for $20.00

* Your marketplace's `dashboard <https://dashboard.balancedpayments.com/#/marketplaces/>`_ escrow balance says $20.00
* You issue a refund for $30.00
* The API will return a **400** status code, similar to:

.. code-block:: bash

   Bad Request: 400: Invalid field [amount] - "3000" must be <= 2000