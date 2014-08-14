Refund an Order
-----------------

.. admonition:: References
  :header_class: alert alert-tab full-width alert-tab-persianBlue60
  :body_class: alert alert-persianBlue20

  .. cssclass:: mini-header

    API Specification

  .. cssclass:: list-noindent

    - `Reversals Collection <https://github.com/balanced/balanced-api/blob/master/fixtures/reversals.json>`_
    - `Reversal Resource <https://github.com/balanced/balanced-api/blob/master/fixtures/_models/reversal.json>`_
    - `Refunds Collection <https://github.com/balanced/balanced-api/blob/master/fixtures/refunds.json>`_
    - `Refund Resource <https://github.com/balanced/balanced-api/blob/master/fixtures/_models/refund.json>`_

  .. cssclass:: mini-header

    API Reference

  .. cssclass:: list-noindent

    - `Create a Reversal </1.1/api/reversals/#create-a-reversal>`_
    - `Create a Refund </1.1/api/refunds/#create-a-refund>`_


Begin by finding the Order you wish to refund.

.. snippet:: order-fetch



Next, reverse any credits that need to be reversed.

.. snippet:: credit-reverse


Once the credit has been reversed, the Order's ``amount_escrowed`` will
increase by the amount of the credit. Note that a reversal can take several
days depending on the bank where the account resides.

.. snippet:: examine-order-after-reversal


Next, refund the original debit.

.. snippet:: debit-refund


Once the debit has been refunded, the ``amount_escrowed`` will decrease by the
amount of the refund.

.. snippet:: examine-order-after-refund
