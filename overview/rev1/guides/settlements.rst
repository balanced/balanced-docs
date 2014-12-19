.. _guides.settlements:

Settlements
=======================

A ``Settlement`` represents the settlement of an ``Account`` balance
against a bank account. If the account balance is positive, funds will be
credited from the account to the specific bank account. If the account
balance is negative, sufficient funds to settle the balance to 0 will be
debited from the bank account to the account.

Marketplaces are advised to utilize a ``Callback`` (webhook) and listen for
``Events`` to be notified of status changes.

Settlements have a ``status`` attribute representing the current status of the
settlement process. There are three possible ``status`` values:
``pending``, ``succeeded``, ``failed``

|

.. admonition:: References
  :header_class: alert alert-tab full-width alert-tab-persianBlue60
  :body_class: alert alert-green alert-persianBlue20 references
  
  .. cssclass:: mini-header
  
    API Reference

  - `Create a Settlement </1.1/api/debits/#create-a-settlement>`_
  - `Create a Credit to an Account </1.1/api/credits/#create-a-credit-to-an-account>`_
  - `Create a Reversal </1.1/api/refunds/#create-a-reversal>`_

  .. cssclass:: mini-header

    API Specification

  - `Settlements Collection <https://github.com/balanced/balanced-api/blob/bulk-credits-sweep-account/fixtures/settlements.json>`_
  - `Settlement Resource <https://github.com/balanced/balanced-api/blob/bulk-credits-sweep-account/fixtures/_models/settlement.json>`_
  - `Accounts Collection <https://github.com/balanced/balanced-api/blob/bulk-credits-sweep-account/fixtures/accounts.json>`_
  - `Account Resource <https://github.com/balanced/balanced-api/blob/bulk-credits-sweep-account/fixtures/_models/account.json>`_
  - `Credits Collection <https://github.com/balanced/balanced-api/blob/master/fixtures/credits.json>`_
  - `Credit Resource <https://github.com/balanced/balanced-api/blob/master/fixtures/_models/credit.json>`_
  - `Reversals Collection <https://github.com/balanced/balanced-api/blob/master/fixtures/refunds.json>`_
  - `Reversal Resource <https://github.com/balanced/balanced-api/blob/master/fixtures/_models/refund.json>`_

|

.. admonition:: Requirements
  :header_class: alert alert-tab full-width alert-tab-yellow
  :body_class: alert alert-green alert-yellow

  Marketplaces are responsible for settling negative account balances.

|


Settle an Account balance
----------------------------

Begin by fetching the ``Account`` to be settled.

.. snippet:: merchant-payable-account-fetch

When funds should be moved from an ``Account`` to a bank account, create a ``Settlement``.
``funding_instrument`` is the bank account against which the balance will be settled. If the
account balance is positive, the account balance will be credited to the specified bank
account.

.. snippet:: settlement-create


There are times when a marketplace needs to reverse a credit that's been issued. Credits to
accounts can be reversed as normal. However, reversing a credit can cause the account balance
to go negative. When this occurs, the marketplace should create another ``Settlement``. This
time, since the balance is negative, the bank account specified in ``funding_instrument`` will
be debited for the amount necessary to settle the account balance to 0.

.. snippet:: settlement-create

|


Settlement status flow
-----------------------

Positive account balance settlement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cssclass:: float-right diagram-subsection

  .. image:: https://www.balancedpayments.com/images/payouts/payouts_status-2x-37d77a93.png
    :width: 570px
    :height: 400px

``Settlements`` have a ``status`` attribute representing the current status of the settlement
process.

.. cssclass:: dl-horizontal dl-params dl-param-values dd-noindent dd-marginbottom

  ``pending``
    As soon as the settlement is created through the API, the status attribute shows
    as ``pending``. This indicates that Balanced received the information for the
    settlement and will begin processing. The ACH network itself processes transactions
    in a batch format. Batch submissions are processed at 3:30 PM Pacific Time on business days.
    If the settlement is created after 3:30 PM Pacific Time, it will not be submitted for
    processing until **3:30 PM Pacific Time the next business day**.
  ``succeeded``
    One business day after the batch submission, the status will change to
    ``succeeded``. That is the *expected* status of the settlement. If the bank account
    number and routing number were entered correctly, the account balance should be
    adequately settled. However, there is no immediate confirmation
    regarding the success of the transaction.
  ``failed``
    The merchant's bank has up to three business days from when the money *should*
    be available to indicate a rejection along with the rejection reason.
    Unfortunately, not all banks comply with ACH network policies and may respond
    after three business days with a rejection. As soon as Balanced receives the
    rejection, the status is updated to ``failed``.


Negative account balance settlement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|

|

.. cssclass:: float-right diagram

  .. image:: https://www.balancedpayments.com/images/ach-debits/ach_debits_payment_status-01-2x-70527870.png
    :width: 570px
    :height: 400px

``Settlements`` have a ``status`` attribute representing the current status of the settlement
process.

.. cssclass:: dl-horizontal dl-params dl-param-values dd-noindent dd-marginbottom

  ``pending``
    As soon as the settlement is created through the API, the ``status`` attribute shows
    as ``pending``. This indicates that Balanced received the information for the
    settlement and will begin processing. The ACH network itself processes transactions
    in a batch format. Batch submissions are processed at 3:30 PM Pacific Time on business days.
    If the settlement is created after 3:30 PM Pacific Time, it will not be submitted for
    processing until **3:30 PM Pacific Time the next business day**.
  ``succeeded``
    After 3-4 days, the status will change to ``succeeded`` and the account balance will be
    settled. Note, even after a succeeded status, the status may still transition to failed,
    even after a few weeks.
  ``failed``
    After 3-4 days, the status will change to ``failed`` if the transaction was
    not successful due to a problem such as an incorrect bank account number
    or insufficient funds.

.. note::
  :header_class: alert alert-tab-yellow
  :body_class: alert alert-yellow

  After a succeeded status, the status may still transition to failed, even
  after a few weeks.

|