.. _cards:

Cards
=====

You'll eventually want to be able to charge credit/debit cards without
having to ask your users for their information over and over again. To do
this, you'll need to create a card resource.

To actually charge cards, you must :ref:`debit an account <debits>`.

.. cssclass:: method-section

tokenize a card
---------------
Creates a new card

.. container:: method-description

   .. dcode:: form cards.create


.. container:: method-examples

  .. dcode:: scenario card_create


.. cssclass:: method-section

retrieve a card
---------------

Retrieves the details of a card that has previously been created.
Supply the ``uri`` that was returned from your previous request, and
the corresponding card information will be returned. The same
information is returned when creating the card.

.. container:: method-description

  .. no request

.. container:: method-examples

  .. dcode:: scenario card_show

.. cssclass:: method-section


list all cards
--------------

Returns a list of cards that you've created.

.. container:: method-description

  ``limit``
      *optional* integer. Defaults to ``10``.

  ``offset``
      *optional* integer. Defaults to ``0``.

.. container:: method-examples

  .. dcode:: scenario card_list

.. cssclass:: method-section

update a card
-------------

Update information in a card

.. container:: method-description

  .. no request

.. container:: method-examples

  .. dcode:: scenario card_update

.. cssclass:: method-section

invalidating a card
-------------------

Invalidating a card will mark the card as invalid, so it may not be charged.

.. container:: method-description

  .. no request

.. container:: method-examples

  .. dcode:: scenario card_invalidate

.. cssclass:: method-section

charging a card
----------------

Charging a card requires that you :ref:`debit an account <debits>`

.. container:: method-description

  .. no request

.. container:: method-examples

  .. no request
