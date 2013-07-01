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

.. dcode:: endpoint marketplaces/cards.create
   :exclude-method: HEAD

Request
~~~~~~~

.. dcode:: form card.create
   :exclude: region state

.. dcode:: scenario cards.tokenize
   :section-include: request

Response
~~~~~~~~

.. dcode:: scenario cards.tokenize
   :section-include: response

Retrieve a Card
---------------

.. dcode:: endpoint marketplaces/cards.show
   :exclude-method: HEAD

Response
~~~~~~~~

.. dcode:: scenario cards.show
   :section-include: response

List All Cards
--------------

.. dcode:: endpoint marketplaces/cards.index
   :exclude-method: HEAD

Request
~~~~~~~

``limit``
    *optional* integer. Defaults to ``10``.

``offset``
    *optional* integer. Defaults to ``0``.

.. dcode:: scenario cards.index
   :section-include: response

List All Cards for an Account
-----------------------------

.. dcode:: endpoint accounts/cards.index
   :exclude-method: HEAD

Request
~~~~~~~

``limit``
    *optional* integer. Defaults to ``10``.

``offset``
    *optional* integer. Defaults to ``0``.

.. dcode:: scenario account_cards.index
   :section-include: response

Update a Card
-------------

.. dcode:: endpoint marketplaces/cards.update

Request
~~~~~~~

.. dcode:: form card.update
   :exclude: account_uri account

.. dcode:: scenario cards.update
   :section-include: request

Response
~~~~~~~~

.. dcode:: scenario cards.update
   :section-include: response

Associate a Card with an Account
--------------------------------

.. dcode:: endpoint marketplaces/cards.update

Request
~~~~~~~

.. dcode:: form cards.update
   :include: account_uri

.. dcode:: scenario cards.associate
   :section-include: request

Response
~~~~~~~~

.. dcode:: scenario cards.associate
   :section-include: response


Delete a Card
---------------------

Request
~~~~~~~

.. dcode:: endpoint bank_accounts.delete

.. dcode:: scenario bank_accounts.delete
   :section-include: response

