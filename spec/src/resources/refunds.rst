Refunds
=======

- `Refund an Account`_
- `Retrieve a Refund`_
- `List All Refunds`_
- `Update a Refund`_

Fields
------

.. dcode:: view refund
   :exclude: invoice_uri fee
   
Deprecated
~~~~~~~~~~

.. decode:: view refund
   :include: fee

Refund an Account
----------------

.. dcode:: endpoint refunds.create
   :exclude-method: HEAD

Request
~~~~~~~

.. dcode:: form refunds.create
   :exclude: account_uri

.. dcode:: scenario refunds.create
   :include: request.*

Response
~~~~~~~~

.. dcode:: scenario refunds.create
   :include: response.*

Retrieve a Refund
----------------

.. dcode:: endpoint refunds.show
   :exclude-method: HEAD

.. dcode:: scenario refunds.show
   :section-chars: ~^
   :section-depth: 1
   :include: response.*


List All refunds
---------------

.. dcode:: endpoint refunds.index
   :exclude-method: HEAD

.. dcode:: scenario refunds.index
   :section-chars: ~^
   :section-depth: 1

Update a Refund
--------------

.. dcode:: endpoint refunds.update
   :exclude-method: HEAD


Request
~~~~~~~

.. dcode:: form refunds.update


.. dcode:: scenario refunds.update
   :include: request.*


Response
~~~~~~~~

.. dcode:: scenario refunds.update
   :include: response.*
