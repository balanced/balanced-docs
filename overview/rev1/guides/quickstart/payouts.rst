Issuing Payouts
=================

A credit (payout) is a transaction where funds are sent to a bank account with
ACH direct deposit. Funds are deposited the next business day for U.S.
bank accounts and the same business day for Wells Fargo accounts.

Credits have a ``status`` attribute representing the current status of the credit
throughout the payout process. There are three possible ``status`` values:
``pending``, ``succeeded``, ``failed``


.. admonition:: References
  :header_class: alert alert-tab full-width alert-tab-persianBlue60
  :body_class: alert alert-persianBlue20 references

  .. cssclass:: mini-header

    API Specification

  - `Credits Collection <https://github.com/balanced/balanced-api/blob/master/fixtures/credits.json>`_
  - `Credit Resource <https://github.com/balanced/balanced-api/blob/master/fixtures/_models/credit.json>`_

  .. cssclass:: mini-header

    API Reference

  - `Create a Credit </1.1/api/credits/#create-a-credit>`_

|

Topic overview
-----------------

By the end of this topic, you should understand how to do following:

- Create a ``Credit``
- Create several ``Credits`` to a split payment to multiple recipient bank accounts


Initiating a credit
--------------------

Initiating a credit (payout) is simple. Assuming we have an existing ``BankAccount`` we can
do the following:

.. snippet:: credit-create


.. note::
  :header_class: alert alert-tab
  :body_class: alert alert-green
  
  Credits may also be initiated via the `Dashboard`_.


Splitting Payments
--------------------

Splitting payments is accomplished by simply initiating a separate credit to each recipient's bank account:

.. snippet:: credit-split


Checkpoint
-----------

You should understand how to do following:

.. cssclass:: list-noindent list-style-none

  - ✓ Create a ``Credit``
  - ✓ Create several ``Credits`` to a split payment to multiple recipient bank accounts

Ensure you have met these points before proceeding.

For additional information, read :doc:`Working with Credits <../credits>`.


|

.. container:: box-left

  .. icon-box-widget::
     :box-classes: box box-block box-blue
     :icon-classes: icon icon-arrow-left

     :doc:`Charging Funding Instruments <charging-funding-instruments>`

.. container:: box-right

  .. read-more-widget::
    :box-classes: box box-block box-blue right
    :icon-classes: icon icon-arrow

    :doc:`Return to Overview <../quickstart>`
 
  .. clear::

|


.. _Dashboard: https://dashboard.balancedpayments.com/