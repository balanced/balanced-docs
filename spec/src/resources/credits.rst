Credits
=======

- `Credit a New Bank Account`_
- `Credit an Existing Bank Account`_
- `Credit a Merchant`_
- `Retrieve a Credit`_
- `List All Credits`_
- `List All Credits for a Bank Account`_
- `List All Credits for a Merchant`_

Fields
------

.. dcode:: view credit
   :exclude: transaction_number available_at fee destination state invoice_uri
   
   - account
     `Accounts <./accounts.rst>`_. Present if the credit went to a merchant instead of directly to a bank account. 
   - bank_account
     `Bank Account <./bank_accounts.rst>`_.
    
Deprecated
~~~~~~~~~~

.. dcode:: view credit
   :include: transaction_number available_at fee destination state


Credit a New Bank Account
-------------------------

.. dcode:: endpoint credits.create

Request
~~~~~~~

.. dcode:: form credit.create

   - bank_account
     `BankAccount <./bank_accounts.rst>`_.

.. dcode:: scenario credits.create
   :include: request.*

Response
~~~~~~~~

.. dcode:: scenario credits.create
   :include: response.*


Credit an Existing Bank Account
-------------------------------

.. dcode:: endpoint bank_account_credits.create

Request
~~~~~~~

.. pilo:: balanced_service.forms:BankAccountCreditCreateForm

.. dcode:: scenario bank_account_credits.create
   :include: request.*

Response
~~~~~~~~

.. dcode:: scenario bank_account_credits.create
   :include: response.*


Credit a Merchant
-----------------

.. dcode:: endpoint account_credits.create


Request
~~~~~~~

.. pilo:: balanced_service.forms:AccountCreditCreateForm
   :exclude: account_uri bank_account_uri

.. dcode:: scenario account_credits.create
   :include: request.*


Response
~~~~~~~~

.. dcode:: scenario account_credits.create
   :include: response.*


Retrieve a Credit
-----------------

.. dcode:: endpoint credits.show
   :exclude-method: HEAD

.. dcode:: scenario credits.show
   :section-chars: ~^
   :section-depth: 1
   :include: response.*


List All Credits
----------------

.. dcode:: endpoint credits.index
   :exclude-method: HEAD
   
Request
~~~~~~~

``limit``
    *optional* integer. Defaults to ``10``. 
 
``offset``
    *optional* integer. Defaults to ``0``.

.. dcode:: scenario credits.index
   :section-chars: ~^
   :section-depth: 1


List All Credits for a Bank Account
-----------------------------------

.. dcode:: endpoint bank_account_credits.index
   :exclude-method: HEAD

Request
~~~~~~~

``limit``
    *optional* integer. Defaults to ``10``. 
 
``offset``
    *optional* integer. Defaults to ``0``.
   
.. dcode:: scenario bank_account_credits.index
   :section-chars: ~^
   :section-depth: 1


List All Credits for a Merchant
-------------------------------

.. dcode:: endpoint account_credits.index
   :exclude-method: HEAD
   
Request
~~~~~~~

``limit``
    *optional* integer. Defaults to ``10``. 
 
``offset``
    *optional* integer. Defaults to ``0``.

.. dcode:: scenario account_credits.index
   :section-chars: ~^
   :section-depth: 1
