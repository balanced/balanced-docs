Holds
=====

- `Create a Hold`_
- `Retrieve a Hold`_
- `List all Holds`_
- `Update a Hold`_
- `Capture a Hold`_
- `Void a Hold`_

Fields
------

.. pez:: balanced_service.controllers.views:Hold
   :exclude: invoice_uri fee
   
   - account
     See `Account <./accounts.rst>`_.

   - source
     See `Card <./cards.rst>`_.

   - debit
     See `Debit <./debits.rst>`_.
     
Deprecated
~~~~~~~~~~

.. view:: hold
   :include: fee

Create a Hold
-------------

.. dcode:: endpoint holds.create

Request
~~~~~~~

.. dcode:: form holds.create
   :exclude: card_uri account_uri

.. dcode:: scenario holds.create
   :include: request.*

Response
~~~~~~~~

.. dcode:: scenario holds.create
   :include: response.*

Retrieve a Hold
---------------

.. dcode:: endpoint holds.show
   :exclude-method: HEAD
   
.. dcode:: scenario holds.show
   :section-chars: ~^
   :section-depth: 1
   :include: response.*

List all Holds
--------------

.. dcode:: endpoint holds.index
   :exclude-method: HEAD
   
.. dcode:: scenario holds.index
   :section-chars: ~^
   :section-depth: 1
   :include: response.*

Update a Hold
-------------

.. dcode:: endpoint holds.update

Request
~~~~~~~

.. pilo:: balanced_service.forms:HoldUpdateForm
   :exclude: is_void appears_on_statement_as

.. dcode:: scenario holds.update
   :include: request.*

Response
~~~~~~~~

.. dcode:: scenario holds.update
   :include: response.*

Capture a Hold
--------------

Use ``hold_uri`` when `creating a debit <./debits.rst#create-a-debit>`_.

.. dcode:: scenario holds.capture
   :section-chars: ~^
   :section-depth: 1

Void a Hold
-----------

.. dcode:: endpoint holds.update

Request
~~~~~~~

.. dcode:: form balanced_service.forms:HoldUpdateForm
   :include: is_void appears_on_statement_as

.. dcode:: scenario holds.void
   :include: request.*

Response
~~~~~~~~

.. dcode:: scenario holds.void
   :include: response.*
