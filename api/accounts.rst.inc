accounts
========

Accounts help facilitate managing multiple credit cards, debit cards,
and bank accounts along with different financial transaction operations, i.e.
refunds, debits, credits.

.. cssclass:: method-section

creating an account
-------------------

.. container:: method-description

  .. no request

.. container:: method-examples

  .. dcode:: account_create


.. cssclass:: method-section

adding a card to an account
---------------------------

Adding a card to an account activates the ability to debit an account, more
specifically, charging a card.

You can add multiple cards to an account.

Balanced associates a ``buyer`` role to signify whether or not an account
has a valid credit card, to acquire funds from.

.. container:: method-description

  .. no request

.. container:: method-examples

  .. dcode:: account_add_card


.. cssclass:: method-section

adding a bank account to an account
-----------------------------------

Adding a bank account to an account activates the ability to credit an
account, or in this case, initiate a next-day ACH payment.

Balanced **does not** associate a role to signify whether or not an account
has a valid bank account to send money to.

.. container:: method-description

  .. no request

.. container:: method-examples

  .. dcode:: account_create_merchant


.. cssclass:: method-section

underwriting an individual
--------------------------

A person, or an individual, is a US based individual or a sole proprietor.

Balanced associates a ``merchant`` role to signify whether or not an account
has been underwritten.

.. container:: method-description

  ``type`` 
      *required* **string**. Merchant type. It should be one of: ``person`` or ``business``. 
   
  ``phone_number`` 
      *required* **string**. E.164 formatted phone number. Length must be **<=** ``15``. 
   
  ``email_address`` 
      *optional* **string** or **null**. RFC-2822 formatted email address. 
   
  ``meta`` 
      *optional* **object**. Single level mapping from string keys to string values. 
   
  ``tax_id`` 
      *optional* **string**. Length must be **between** ``4`` and ``9``. 
   
  ``dob`` 
      *optional* **string**. Date-of-birth formatted as ``YYYY-MM-DD``. 
   
  ``name`` 
      *optional* **string**. Sequence of characters. Length must be **<=** ``128``. 
   
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
   

.. container:: method-examples

  .. dcode:: account_underwrite_person


.. cssclass:: method-section

underwriting a business
-----------------------

Balanced associates a ``merchant`` role to signify whether or not an account
has been underwritten.

.. container:: method-description

  ``type`` 
      *required* **string**. Merchant type. It should be one of: ``person`` or ``business``. 
   
  ``name`` 
      *required* **string**. Sequence of characters. Length must be **<=** ``128``. 
   
  ``phone_number`` 
      *required* **string**. E.164 formatted phone number. Length must be **<=** ``15``. 
   
  ``email_address`` 
      *optional* **string** or **null**. RFC-2822 formatted email address. 
   
  ``meta`` 
      *optional* **object**. Single level mapping from string keys to string values. 
   
  ``tax_id`` 
      *optional* **string**. Length must be **between** ``4`` and ``9``. 
   
  ``dob`` 
      *optional* **string**. Date-of-birth formatted as ``YYYY-MM-DD``. 
   
  ``person`` 
      .. cssclass:: nested1 
   
      *optional* **object**.  
          ``name`` 
              *required* **string**. Sequence of characters. 
   
          ``dob`` 
              *required* **string**. Date-of-birth formatted as ``YYYY-MM-DD``. 
   
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
   
          ``tax_id`` 
              *optional* **string**. Length must be **between** ``4`` and ``9``. 
   
   
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
   

.. container:: method-examples

  .. dcode:: account_underwrite_business
