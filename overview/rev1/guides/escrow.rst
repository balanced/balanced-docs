.. _guides.disputes:

Escrow
======================

Every marketplace has a single escrow. This escrow account is essentially like a
pool of funds. Debits bring funds into the marketplace escrow. Credits take
funds out of the marketplace escrow. Transactions involving Orders do not involve
the marketplace escrow.

Marketplaces have complete control over how funds are disbursed from escrow.
Funds in escrow may be distributed to recipients as desired. There is inherently
no time limit for the duration funds may sit in escrow. Best practice is to
refrain from releasing funds until after merchant fulfillment has occurred,
confirmation of a shipped product or completion of a service for example. Escrow
is not meant as a means of extended withholding. Holding funds in escrow for
extended periods of time often leads to an increased number in chargebacks and
customer dissatisfaction.

|

.. note::
  :header_class: alert alert-tab
  :body_class: alert alert-green

  Balanced does not collect interest of any kind on funds in escrow.
  Transactions involving bank accounts associated to the marketplace owner
  customer are free of charge.

|


Determine Escrow balance
-------------------------

.. snippet:: marketplace-in-escrow


Pre-funding Escrow
------------------------

Any payout issued requires maintaining sufficient money in your Balanced escrow.

If you do not have a sufficient balance, Balanced will return a ``409`` http
status code, stating that you do not have sufficient funds to cover your
desired ACH operation. You will have to add funds to your marketplace escrow
from a credit card or bank account attached to your marketplace. This may be
done via the API or via the Balanced `dashboard`_. To do this via the API:

.. snippet:: debit-marketplace-escrow


Transfers may take 2-5 days for the funds to become available; alternatively, you
may fund your account **instantly** by debiting a credit card associated to your
marketplace.


Obtaining funds from Escrow
---------------------------

To transfer funds from your marketplace escrow to your marketplace bank account,
issue a credit:

.. snippet:: credit-marketplace-escrow


Credits can take 1-3 days for the funds to become available depending on
the target bank.


.. _dashboard: https://dashboard.balancedpayments.com/
.. _billy issue #1: https://github.com/balanced/billy/issues/1