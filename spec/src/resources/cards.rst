Cards
=====

- `Tokenize a Card`_
- `Retrieve a Card`_
- `List All Cards`_
- `List All Cards for an Account`_
- `Update a Card`_
- `Associate a Card with an Account`_

Fields
------

.. dcode:: view card

   - account
     See `Accounts <./accounts.rst>`_.


Tokenize a Card
---------------

.. dcode:: endpoint marketplace_cards.create
   :exclude-method: HEAD

Request
~~~~~~~

.. dcode:: form card.create
   :exclude: region state

.. dcode:: scenario cards.tokenize
   :include: request.*

Response
~~~~~~~~

.. dcode:: scenario cards.tokenize
   :include: response.*

Retrieve a Card
---------------

.. dcode:: endpoint marketplace_cards.show
   :exclude-method: HEAD

Response
~~~~~~~~

.. dcode:: scenario cards.show
   :include: response.*

List All Cards
--------------

.. dcode:: endpoint marketplace_cards.index
   :exclude-method: HEAD

Request
~~~~~~~

``limit``
    *optional* integer. Defaults to ``10``.

``offset``
    *optional* integer. Defaults to ``0``.

.. dcode:: scenario cards.index
   :section-chars: ~^
   :section-depth: 1
   :include: response.*

List All Cards for an Account
-----------------------------

.. dcode:: endpoint account_cards.index
   :exclude-method: HEAD

Request
~~~~~~~

``limit``
    *optional* integer. Defaults to ``10``.

``offset``
    *optional* integer. Defaults to ``0``.

.. dcode:: scenario account_cards.index
   :section-chars: ~^
   :section-depth: 1
   :include: response.*

Update a Card
-------------

.. dcode:: endpoint marketplace_cards.update

Request
~~~~~~~

.. form:: card.update
   :exclude: account_uri account

.. dcode:: scenario cards.update
   :include: request.*

Response
~~~~~~~~

.. dcode:: scenario cards.update
   :include: response.*

Associate a Card with an Account
--------------------------------

.. dcode:: endpoint marketplace_cards.update

Request
~~~~~~~

.. dcode:: form cards.update
   :include: account_uri

.. dcode:: scenario cards.associate
   :include: request.*

Response
~~~~~~~~

.. dcode:: scenario cards.associate
   :include: response.*
