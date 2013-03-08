bank accounts
=============

You'll eventually want to be able to credit bank accounts without having to
ask your users for their information over and over again. To do this, you'll
need to create a bank account object.

**NOTE** To debit a bank account you must first :ref:`verify it <bank-account-verifications>`.

.. cssclass:: method-section

creating a new bank account
---------------------------

Creates a new bank account.

.. container:: method-description

  ``name`` 
      *required* **string**. Name on the bank account. Length must be **>=** ``2``. 
   
  ``account_number`` 
      *required* **string**. Bank account number. Length must be **>=** ``1``. 
   
  ``routing_number`` 
      *required* **string**. Bank account code. Length must be **=** ``9``. 
   
  ``type`` 
      *required* **string**. ``checking`` or ``savings``. 
   
  ``meta`` 
      *optional* **object**. Single level mapping from string keys to string values. 
   

.. container:: method-examples

  .. dcode:: bank_account_create


.. cssclass:: method-section

retrieve a bank account
-----------------------

Retrieves the details of a bank account that has previously been created.
Supply the ``uri`` that was returned from your previous request, and
the corresponding bank account information will be returned. The same
information is returned when creating the bank account.

.. container:: method-description

  .. no request

.. container:: method-examples

  .. dcode:: bank_account_show


.. cssclass:: method-section

list all bank accounts
----------------------

Returns a list of bank accounts that you've created but haven't deleted.

.. container:: method-description

  ``limit``
      *optional* integer. Defaults to ``10``.

  ``offset``
      *optional* integer. Defaults to ``0``.

.. container:: method-examples

  .. dcode:: bank_account_list


.. cssclass:: method-section

delete a bank account
---------------------

Permanently delete a bank account. It cannot be undone. All associated credits
with a deleted bank account will not be affected.

.. container:: method-description

  .. no request

.. container:: method-examples

  .. dcode:: bank_account_delete
