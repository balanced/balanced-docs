.. _debits:

Debits
======

Currently, Balanced supports only card transactions (`info on ACH debits`_) for
debits. To debit an account, i.e. charge a card, you must create a new debit
resource.


.. cssclass:: method-section

.. _debits.create:

create a new debit
------------------

.. todo:: debit an account with different cards
.. todo:: debit an owner account

Debits an account. Returns a ``uri`` that  can later be used to reference this
debit.

Successful creation of a debit using a card will return an associated ``hold``
mapping as part of the response. This :ref:`hold <holds>` was created and
captured behind the scenes automatically. For ACH debits there is no
corresponding hold.

.. container:: method-description

  ``amount`` 
      *optional* **integer**. If the resolving URI references a hold then this is hold amount. You can 
      always capture less than the hold amount (e.g. a partial capture). 
      Otherwise its the maximum per debit amount for your marketplace. Value must be >= the minimum per debit ``amount`` for *your* 
      marketplace. Value must be <= the maximum per debit ``amount`` for *your* 
      marketplace. 
   
  ``appears_on_statement_as`` 
      *optional* **string**. Text that will appear on the buyer's statement. Characters that can be 
      used are limited to: 
   
      - ASCII letters (``a-z`` and ``A-Z``) 
      - Digits (``0-9``) 
      - Special characters (``.<>(){}[]+&!$*;-%_?:#@~='" ^\`|``) 
   
      Any other characters will be rejected. Length must be **<=** ``22``. 
   
  ``meta`` 
      *optional* **object**. Single level mapping from string keys to string values. 
   
  ``description`` 
      *optional* **string**. Sequence of characters. 
   
  ``account_uri`` 
      *optional* **string**.  
   
  ``on_behalf_of_uri`` 
      *optional* **string**. The account of a merchant, usually a seller or service provider, that 
      is associated with this card charge or bank account debit. 
   
  ``merchant_uri`` 
      *optional* **string**.  
   
  ``hold_uri`` 
      *optional* **string**. If no ``hold`` is provided one my be generated and captured if the 
      funding source is a card. 
   
  ``source_uri`` 
      *optional* **string**.  
   
  ``bank_account_uri`` 
      *optional* **string**.  
   
  ``card_uri`` 
      *optional* **string**.  
   

.. container:: method-examples

  .. dcode:: debit_create


.. cssclass:: method-section

retrieve a debit
----------------

Retrieves the details of a created debit.

.. container:: method-description

  .. no request

.. container:: method-examples

  .. dcode:: debit_show


.. cssclass:: method-section

list all debits
---------------

Returns a list of debits you've previously created. The debits are returned
in sorted order, with the most recent debits appearing first.

.. container:: method-description

  ``limit``
      *optional* integer. Defaults to ``10``.

  ``offset``
      *optional* integer. Defaults to ``0``.

.. container:: method-examples

  .. dcode:: debit_list


.. cssclass:: method-section

list all debits for an account
------------------------------

Returns a list of debits you've previously created against a specific account.
The ``debits_uri`` is a convenient uri provided so that you can simply issue
a ``GET`` to the ``debits_uri``. The debits are returned in sorted order,
with the most recent debits appearing first.

.. container:: method-description

  ``limit``
      *optional* integer. Defaults to ``10``.

  ``offset``
      *optional* integer. Defaults to ``0``.

.. container:: method-examples

  .. dcode:: debit_account_list


.. cssclass:: method-section

update a debit
--------------

Updates information about a debit

.. container:: method-description

  ``meta`` 
      *optional* **object**. Single level mapping from string keys to string values. 
   
  ``description`` 
      *optional* **string**. Sequence of characters. 
   

.. container:: method-examples

  .. dcode:: debit_update


.. cssclass:: method-section

refund a debit
--------------

Issues a refund for a particular debit. This creates a :ref:`refund <refunds>`.

.. container:: method-description

   Use the ``refund_uri`` on a :ref:`debit object <debits>`.

.. container:: method-examples

   .. dcode:: debit_refund


.. _info on ACH debits: http://github.com/balanced/balanced-api/issues/2
