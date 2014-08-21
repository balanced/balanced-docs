Refunding an Order
=======================

.. admonition:: References
  :header_class: alert alert-tab full-width alert-tab-persianBlue60
  :body_class: alert alert-persianBlue20

  .. cssclass:: mini-header

    API Reference

  .. cssclass:: list-noindent

    - `Create a Reversal </1.1/api/reversals/#create-a-reversal>`_
    - `Create a Refund </1.1/api/refunds/#create-a-refund>`_
    - `Fetch an Order </1.1/api/orders/#fetch-an-order>`_

  .. cssclass:: mini-header

    API Specification

  .. cssclass:: list-noindent

    - `Orders Collection <https://github.com/balanced/balanced-api/blob/master/fixtures/orders.json>`_
    - `Order Resource <https://github.com/balanced/balanced-api/blob/master/fixtures/_models/order.json>`_
    - `Reversals Collection <https://github.com/balanced/balanced-api/blob/master/fixtures/reversals.json>`_
    - `Reversal Resource <https://github.com/balanced/balanced-api/blob/master/fixtures/_models/reversal.json>`_
    - `Refunds Collection <https://github.com/balanced/balanced-api/blob/master/fixtures/refunds.json>`_
    - `Refund Resource <https://github.com/balanced/balanced-api/blob/master/fixtures/_models/refund.json>`_

  

Reverse credits
~~~~~~~~~~~~~~~~

Before we can issue refunds to the buyers we must reverse any credits necessary to have funds
available in the Order escrow.

Begin by finding the Order you wish to refund.

.. snippet:: order-fetch


Next, retrieve all the credits for the ``Order``.

.. snippet:: order-credits-fetch


Determine which credits you wish to reverse and reverse each of them.

.. snippet:: credit-reverse


You may also issue a partial reversal. Just supply an amount parameter in the request.


Once the credit has been reversed, the Order's ``amount_escrowed`` will
increase by the amount of the credit. Note that a reversal can take several
days depending on the bank where the account resides. Marketplaces should utilize
a ``Callback`` to listen for ``Events`` from Balanced to be notified of ACH transaction
state changes. Please refer to the :doc:`Events <../events>` guide for more information.

.. snippet:: order-amount-escrowed


Refund debits
~~~~~~~~~~~~~~~~

Retrieve all the debits for the ``Order``.

.. snippet:: order-debits-fetch


Determine which debits you wish to refund and refund each of them.

.. snippet:: debit-refund


Once the debit has been refunded, the ``amount_escrowed`` will decrease by the
amount of the refund.

.. snippet:: order-amount-escrowed

|

.. container:: box-left

 .. icon-box-widget::
   :box-classes: box box-block box-blue
   :icon-classes: icon icon-arrow-left

   :doc:`Crediting the Marketplace <credit-marketplace>`

|
