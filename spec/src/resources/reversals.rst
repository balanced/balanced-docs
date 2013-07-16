Reversals
=========

- `Reverse a Credit`_
- `Retrieve a Refund`_
- `List All Refunds`_
- `Update a Refund`_

Fields
------

.. dcode:: view reversal
   :exclude: invoice_uri fee

Deprecated
~~~~~~~~~~

.. dcode:: view reversal
   :include: fee

Reversal a Credit
-----------------

.. dcode:: endpoint reversals.create
   :exclude-method: HEAD

Request
~~~~~~~

.. dcode:: form reversals.create
   :exclude: account_uri

.. dcode:: scenario reversals.create
   :section-include: request

Response
~~~~~~~~

.. dcode:: scenario reversals.create
   :section-include: response

Retrieve a Reversal
-------------------

.. dcode:: endpoint reversals.show
   :exclude-method: HEAD

Response
~~~~~~~~

.. dcode:: scenario reversals.show
   :section-include: response


List All Reversals
------------------

.. dcode:: endpoint reversals.index
   :exclude-method: HEAD

.. dcode:: scenario reversals.index

Update a Reversal
---------------

.. dcode:: endpoint reversals.update
   :exclude-method: HEAD


Request
~~~~~~~

.. dcode:: form reversals.update

.. dcode:: scenario reversals.update
   :section-include: request


Response
~~~~~~~~

.. dcode:: scenario reversals.update
   :section-include: response
