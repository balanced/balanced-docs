credits
=======

To credit a bank account, you must create a new credit resource.


.. cssclass:: method-section

credit a new bank account
-------------------------

To credit a new bank account, you simply pass the amount along with the bank
account details. We do not store this bank account when you create a credit
this way, so you can safely assume that the information has been deleted.

.. container:: method-description

  ``amount`` 
      *required* **integer**. USD cents. You must have ``amount`` funds transferred to cover the 
      credit. 
   
  ``bank_account`` 
      .. cssclass:: nested1 
   
      *required* **object**.  
          ``name`` 
              *required* **string**. Name on the bank account. Length must be **>=** ``2``. 
   
          ``account_number`` 
              *required* **string**. Bank account number. Length must be **>=** ``1``. 
   
          ``bank_code`` 
              *required* **string**. Bank account code. Length must be **=** ``9``. 
   
          ``routing_number`` 
              *required* **string**. Bank account code. Length must be **=** ``9``. 
   
          ``type`` 
              *required* **string**. ``checking`` or ``savings``. 
   
          ``meta`` 
              *optional* **object**. Single level mapping from string keys to string values. 
   
   
  ``description`` 
      *optional* **string** or **null**. Sequence of characters. 
   

.. container:: method-examples

  .. dcode:: credit_create_new_bank_account

.. cssclass:: method-section

credit an existing bank account
-------------------------------

To credit an existing bank account, you simply pass the amount to the
nested credit endpoint of a bank account. The ``credits_uri`` is a convenient
uri provided so that you can simply issue a ``POST`` with the amount and a
credit shall be created.


.. container:: method-description

  ``amount`` 
      *required* **integer**. USD cents. You must have ``amount`` funds transferred to cover the 
      credit. 
   
  ``description`` 
      *optional* **string** or **null**. Sequence of characters. 
   

.. container:: method-examples

  .. dcode:: credit_create_existing_bank_account


.. cssclass:: method-section

retrieve a credit
-----------------

Retrieves the details of a credit that you've previously created. Use the
``uri`` that was previously returned, and the corresponding credit
information will be returned.

.. container:: method-description

  .. no request

.. container:: method-examples

  .. dcode:: credit_show


.. cssclass:: method-section

list all credits
----------------

Returns a list of credits you've previously created. The credits are returned
in sorted order, with the most recent credits appearing first.

.. container:: method-description

  ``limit``
      *optional* integer. Defaults to ``10``.

  ``offset``
      *optional* integer. Defaults to ``0``.

.. container:: method-examples

  .. dcode:: credit_list


.. cssclass:: method-section

list all credits for a bank account
-----------------------------------

Returns a list of credits you've previously created to a specific bank account.
The ``credits_uri`` is a convenient uri provided so that you can simply issue
a ``GET`` to the ``credits_uri``. The credits are returned in sorted order,
with the most recent credits appearing first.

.. container:: method-description

  ``limit``
      *optional* integer. Defaults to ``10``.

  ``offset``
      *optional* integer. Defaults to ``0``.

.. container:: method-examples

  .. dcode:: credit_bank_account_list


.. cssclass:: method-section

creating a new credit for an account
------------------------------------

.. container:: method-description

  ``amount`` 
      *required* **integer**. USD cents. Must be **>=** your minimum credit amount but **<=** your maximum credit amount. 
   
  ``description`` 
      *optional* **string** or **null**. Sequence of characters. 
   
  ``meta`` 
      *optional* **object**. Single level mapping from string keys to string values. 
   
  ``appears_on_statement_as`` 
      *optional* **string**. Text that will appear on the buyer's statement. Characters that can be 
      used are limited to: 
   
      - ASCII letters (``a-z`` and ``A-Z``) 
      - Digits (``0-9``) 
      - Special characters (``.<>(){}[]+&!$*;-%_?:#@~='" ^\`|``) 
   
      Any other characters will be rejected. Length must be **<=** ``22``. 
   
  ``destination_uri`` 
      *optional* **string**.  
   
  ``bank_account_uri`` 
      *optional* **string**.  
   

.. container:: method-examples

  .. dcode:: credit_account_merchant_create


.. cssclass:: method-section

listing all credits for an account
----------------------------------

.. container:: method-description

  ``limit``
      *optional* integer. Defaults to ``10``.

  ``offset``
      *optional* integer. Defaults to ``0``.

.. container:: method-examples

  .. dcode:: credit_account_list
