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

  ``card_number`` 
      *required* **string**. The digits of the credit card number. 
   
  ``expiration_year`` 
      *required* **integer**. Expiration year. The current year or later. Value must be **<=** ``9999``. 
   
  ``expiration_month`` 
      *required* **integer**. Expiration month (e.g. 1 for January). If ``expiration_year`` is the current year then current month or later, 
      otherwise 1. Value must be **<=** ``12``. 
   
  ``security_code`` 
      *optional* **string**. The 3-4 digit security code for the card. 
   
  ``name`` 
      *optional* **string**. Sequence of characters. Length must be **<=** ``128``. 
   
  ``phone_number`` 
      *optional* **string**. E.164 formatted phone number. Length must be **<=** ``15``. 
   
  ``city`` 
      *optional* **string**. City. 
   
  ``region`` 
      *optional* **string**. Region (e.g. state, province, etc). This field has been 
      **deprecated**. 
   
  ``state`` 
      *optional* **string**. US state. This field has been **deprecated**. 
   
  ``postal_code`` 
      *required* **string**. Postal code. This is known as a zip code in the USA. 
      *requires* ``country_code``. 
   
  ``street_address`` 
      *required* **string**. Street address. 
      *requires* ``postal_code``. 
   
  ``country_code`` 
      *optional* **string**. `ISO-3166-3 
      <http://www.iso.org/iso/home/standards/country_codes.htm#2012_iso3166-3>`_ 
      three character country code. 
   
  ``meta`` 
      *optional* **object**. Single level mapping from string keys to string values. 
   
  ``is_valid`` 
      *optional* **boolean**. Indicates whether the card is active (``true``) or has been deactivated 
      (``false``). 
   

.. container:: method-examples

  .. dcode:: card_create


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

  .. dcode:: card_show

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

  .. dcode:: card_list


.. cssclass:: method-section

update a card
-------------

Update information in a card

.. container:: method-description

  .. no request

.. container:: method-examples

  .. dcode:: card_update

.. cssclass:: method-section

invalidating a card
-------------------

Invalidating a card will mark the card as invalid, so it may not be charged.

.. container:: method-description

  .. no request

.. container:: method-examples

  .. dcode:: card_invalidate

.. cssclass:: method-section

charging a card
----------------

Charging a card requires that you :ref:`debit an account <debits>`

.. container:: method-description

  .. no request

.. container:: method-examples

  .. no request
