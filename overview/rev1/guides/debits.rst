.. _guides.debits:

Debits
=======================

A debit is a transaction where funds are obtained from a credit card or from a
bank account via the ACH Network. Funds obtained via credit card debits are
immediately available in escrow. Funds being obtained via ACH debits are
generally available in escrow in 3-4 business days. Currently Balanced supports
credit card debits as well as bank accounts debits via ACH. Marketplaces that
make use of ACH are advised to utilize a ``Callback`` (webhook) and listen for
``Events`` to be notified of status changes.

Debits have a ``status`` attribute representing the current status of the debit
throughout the payout process. There are three possible ``status`` values:
``pending``, ``succeeded``, ``failed``

|

.. admonition:: References
  :header_class: alert alert-tab full-width alert-tab-persianBlue60
  :body_class: alert alert-green alert-persianBlue20 references
  
  .. cssclass:: mini-header
  
    API Reference

  - `Create a Card Debit </1.1/api/debits/#create-a-card-debit>`_
  - `Create a Bank Account Debit </1.1/api/debits/#create-a-bank-account-debit>`_
  - `Create a Bank Account Verification </1.1/api/bank-account-verifications/#create-a-bank-account-verification>`_
  - `Create a Refund </1.1/api/refunds/#create-a-refund>`_

  .. cssclass:: mini-header

    API Specification

  - `Orders Collection <https://github.com/balanced/balanced-api/blob/master/fixtures/orders.json>`_
  - `Order Resource <https://github.com/balanced/balanced-api/blob/master/fixtures/_models/order.json>`_
  - `Debits Collection <https://github.com/balanced/balanced-api/blob/master/fixtures/debits.json>`_
  - `Debit Resource <https://github.com/balanced/balanced-api/blob/master/fixtures/_models/debit.json>`_
  - `Refunds Collection <https://github.com/balanced/balanced-api/blob/master/fixtures/refunds.json>`_
  - `Refund Resource <https://github.com/balanced/balanced-api/blob/master/fixtures/_models/refund.json>`_

|

.. admonition:: Requirements
  :header_class: alert alert-tab full-width alert-tab-yellow
  :body_class: alert alert-green alert-yellow

  Funds must be paid to merchants within 30 days of the charge.

|


Debit a credit card
----------------------

Let's go ahead and debit the buyer's card. First we'll fetch the buyer's card then debit (charge)
it for an ``Order``.

.. snippet:: card-debit


Debit a bank account
----------------------

Debiting a bank account (ACH) is very similar to debiting a credit card.

.. admonition:: Requirements
  :header_class: alert alert-tab full-width alert-tab-yellow
  :body_class: alert alert-green alert-yellow
  
  Bank accounts you wish to debit must first `be verified`_.


We'll first fetch the buyer's verified bank account then debit (charge) it for an ``Order``.

.. snippet:: bank-account-debit


|


ACH debit status flow
-----------------------

.. cssclass:: float-right diagram

  .. image:: https://www.balancedpayments.com/images/ach-debits/ach_debits_payment_status-01-2x-70527870.png
    :width: 570px
    :height: 400px

``Debits`` have a ``status`` attribute representing the current status of the debit process.

.. cssclass:: dl-horizontal dl-params dl-param-values dd-noindent dd-marginbottom

  ``pending``
    As soon as the debit is created through the API, the ``status`` attribute shows
    as ``pending``. This indicates that Balanced received the information for the
    debit and will begin processing. The ACH network itself processes transactions
    in a batch format. Batch submissions are processed at 3:30 PM Pacific Time on business days.
    If the debit is created after 3:30 PM Pacific Time, it will not be submitted for processing
    until **3:30 PM Pacific Time the next business day**.
  ``succeeded``
    After 3-4 days, the status will change to ``succeeded`` and the funds will be
    available in escrow. Note, even after a succeeded status, the status may still
    transition to failed even after a few weeks.
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



Refunding a debit
-------------------

In the event that you need to cancel a payout, e.g. a user is not satisfied with
the product, you can create a ``Refund``.

A ``Refund`` resource represents a refund of a ``Debit`` transaction. The
amount of the refund may be any value up to the amount of the original
``Debit``. Refunds generally process in one day or less.


.. snippet:: refund-create


Refund status flow
------------------------

.. cssclass:: float-right diagram

  .. image:: https://www.balancedpayments.com/images/ach-debits/ach_debits_refund_status-01-2x-37d77a93.png
    :width: 570px
    :height: 400px

``Refunds`` have a ``status`` attribute representing the current status of the refund process.

A Debit may also be refunded from the `Dashboard`_.

.. cssclass:: dl-horizontal dl-params dl-param-values dd-noindent dd-marginbottom

  ``pending``
    As soon as the refund is created through the API, the ``status`` attribute shows
    as ``pending``. This indicates that Balanced received the information for the
    refund and will begin processing. The ACH network itself processes transactions
    in a batch format. Batch submissions are processed at 3:30 PM Pacific Time on business days.
    If the refund is created after 3:30 PM Pacific Time, it will not be submitted for processing
    until **3:30 PM Pacific Time the next business day**.
  ``succeeded``
    A ``succeeded`` status is displayed as the expected state of the refund one day after refund submission;
    however, there is no immediate confirmation regarding the success of the refund.
  ``failed``
    If the refund fails, Balanced will be notified in 1–4 business days. The status will update from
    ``pending`` to ``failed`` or ``succeeded`` to ``failed`` depending on when the failed notice is received.




.. _be verified: /1.1/api/bank-account-verifications
.. _Dashboard: https://dashboard.balancedpayments.com/