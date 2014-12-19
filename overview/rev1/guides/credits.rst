.. _guides.credits:

Credits
=====================

A credit (payout) is a transaction where funds are sent to a bank account with
ACH direct deposit. Funds are deposited the next business day for U.S.
bank accounts and the same business day for Wells Fargo accounts.

Credits have a ``status`` attribute representing the current status of the credit
throughout the payout process. There are three possible ``status`` values:
``pending``, ``succeeded``, ``failed``


Balanced currently supports payouts to:

- Bank accounts via ACH
- Debit cards

|

.. admonition:: References
  :header_class: alert alert-tab full-width alert-tab-persianBlue60
  :body_class: alert alert-green alert-persianBlue20 references
  
  .. cssclass:: mini-header
  
    API Reference

  - `Create a Credit to a Bank Account </1.1/api/credits/#create-a-credit-to-a-bank-account>`_
  - `Create a Credit to a Card </1.1/api/credits/#create-a-credit-to-a-card>`_
  - `Create a Reversal </1.1/api/reversals/#create-a-reversal>`_
  
  .. cssclass:: mini-header

    API Specification

  - `Orders Collection <https://github.com/balanced/balanced-api/blob/master/fixtures/orders.json>`_
  - `Order Resource <https://github.com/balanced/balanced-api/blob/master/fixtures/_models/order.json>`_
  - `Credits Collection <https://github.com/balanced/balanced-api/blob/master/fixtures/credits.json>`_
  - `Credit Resource <https://github.com/balanced/balanced-api/blob/master/fixtures/_models/credit.json>`_
  - `Reversals Collection <https://github.com/balanced/balanced-api/blob/master/fixtures/reversals.json>`_
  - `Reversal Resource <https://github.com/balanced/balanced-api/blob/master/fixtures/_models/reversal.json>`_

|

.. admonition:: Requirements
  :header_class: alert alert-tab full-width alert-tab-yellow
  :body_class: alert alert-green alert-yellow

  Funds must be paid to merchants within 30 days of the charge.

|


Create a credit to a BankAccount
---------------------------------

Let's issue a credit to the bank account. Note that bank accounts to which you only wish to credit
do not need to be verified.

.. snippet:: credit-create


Create a credit to a Card
-----------------------------

Initiating a credit (payout) to a card is simple, but there are a few requirements to be aware of.

.. admonition:: Requirements
  :header_class: alert alert-tab full-width alert-tab-yellow
  :body_class: alert alert-green alert-yellow

  - ``name`` must have been supplied on card tokenization.
  - ``card_type`` must be ``debit``
  - ``card_category`` cannot be ``prepaid``. Pre-paid cards are not supported.

  The maximum amount per transaction is $2,500.

|

Assuming we have an existing and creditable ``Card`` we can do the following:

.. snippet:: card-credit


Create a credit to an Account
---------------------------------

Let's issue a credit to an account.

.. snippet:: order-credit-merchant-payable-account


Statement descriptor
--------------------------

Balanced allows marketplaces to specify the text that appears on statements for
a transaction. This is referred to as the soft descriptor and is set by
specifying the ``appears_on_statement_as`` field when creating a credit.


.. admonition:: Requirements
  :header_class: alert alert-tab full-width alert-tab-yellow
  :body_class: alert alert-green alert-yellow

  Characters that can be used are limited to the following (any other characters
  will be rejected):

  .. cssclass:: list-indent

    - ASCII letters (a-z and A-Z)
    - Digits (0-9)
    - Special characters (``.<>(){}[]+&!$;-%_?:#@~='"^\`|``)

  Descriptor length limit:

  .. cssclass:: list-indent

    - ACH credits: 14 characters. ACH credits do not have a prefix.
    - Card credits: 12 characters.


Example usage:

.. snippet:: credit-soft-descriptor


Payout status flow
-------------------

.. cssclass:: float-right diagram

  .. image:: https://www.balancedpayments.com/images/payouts/payouts_status-2x-37d77a93.png
    :width: 570px
    :height: 400px

Credits have a ``status`` attribute representing the current status of the credit
throughout the payout process.

.. cssclass:: dl-horizontal dl-params dl-param-values dd-noindent dd-marginbottom

  ``pending``
    As soon as the credit is created through the API, the status shows
    as ``pending``. This indicates that Balanced received the information for the
    credit and will begin processing. The ACH network itself processes transactions
    in a batch format. Batch submissions are processed at 3:30 PM Pacific Time on business days.
    If the credit is created after 3:30 PM Pacific Time, it will not be submitted for processing
    until **3:30 PM Pacific Time the next business day**.
  ``succeeded``
    One business day after the batch submission, the status will change to
    ``succeeded``. That is the *expected* status of the credit. If the account
    number and routing number were entered correctly, the money should in fact
    be available to the seller. However, there is no immediate confirmation
    regarding the transaction showing up in the seller's account successfully.
  ``failed``
    The seller's bank has up to three business days from when the money *should*
    be available to indicate a rejection along with the rejection reason.
    Unfortunately, not all banks comply with ACH network policies and may respond
    after three business days with a rejection. As soon as Balanced receives the
    rejection, the status is updated to ``failed``.


Reversing credits
-------------------

In the event that you need to cancel a payout, e.g. a user is not
satisfied with the product, you can create a ``Reversal``.


Reverse a credit
~~~~~~~~~~~~~~~~~~~~~

.. snippet:: reversal-create

.. note::
  :header_class: alert alert-tab-red
  :body_class: alert alert-red
  
  Reversing a batch credit may cause an the Account balance to go negative.
  Marketplaces are responsible for settling negative account balances.

In the event that reversing a batched credit causes the Account balance to go negative,
create a ``Settlement`` to settle the account balance to 0.

.. snippet:: settlement-create


Reversal status flow
~~~~~~~~~~~~~~~~~~~~~~~

.. cssclass:: float-right diagram-subsection

  .. image:: https://www.balancedpayments.com/images/payouts/payouts_reversal_status-2x-6fa384aa.png
    :width: 570px
    :height: 400px

``Reversals`` have a ``status`` attribute representing the current status of the reversal process.

Credits may also be reversed from the `Dashboard`_.


.. cssclass:: dl-horizontal dl-params dl-param-values dd-noindent dd-marginbottom

  ``pending``
    As soon as the reversal is created through the API, the ``status`` attribute shows
    as ``pending``. This indicates that Balanced received the information for the
    refund and will begin processing. The ACH network itself processes transactions
    in a batch format. Batch submissions are processed at 3:30 PM Pacific Time on business days.
    If the refund is created after 3:30 PM Pacific Time, it will not be submitted for processing
    until **3:30 PM Pacific Time the next business day**.
  ``succeeded``
    A ``succeeded`` status is displayed as the expected state of the deposit one day after payout submission;
    however, there is no immediate confirmation regarding the success of the payout.
  ``failed``
    If a credit fails due to incorrect account information, Balanced will be notified in 1–4 business days.
    The status will update from ``pending`` to ``failed`` or ``succeeded`` to ``failed`` depending on when the failed
    notice is received.



.. _Dashboard: https://dashboard.balancedpayments.com/