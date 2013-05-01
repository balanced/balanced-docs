.. dcode-default::
    :cache:

.. dcode-default:: view
    :script: ./rst.py view

.. dcode-default:: form
    :script: ./rst.py form

.. dcode-default:: endpoint
    :script: ./rst.py endpoint

.. dcode-default:: error
    :script: ./rst.py error

.. dcode-default:: scenario
    :script: ./scenario.py -c scenario.cache
    :section-chars: ~^

.. dcode-default:: enum
    :script: ./rst.py enum


.. container:: langbar

  Clients:

  * curl
  * ruby
  * python
  * php

.. contents::
   :depth: 3
   :backlinks: none
   :class: hidden navnav


=============
API reference
=============

The API conforms to the design principles of Representational State Transfer
(REST). It supports only the JSON data format.

* Methods to retrieve data from the Balanced API require an HTTP ``GET`` request.
* Methods that submit data to the Balanced API require an HTTP ``POST`` request.
* Methods that change data in the Balanced API require an HTTP ``PUT`` request.
* Methods that destroy data in the Balanced API require an HTTP ``DELETE`` request.


.. include:: authentication.rst.inc
.. include:: errors.rst.inc
.. include:: bank_accounts.rst.inc
.. include:: bank_account_verifications.rst.inc
.. include:: cards.rst.inc
.. include:: accounts.rst.inc
.. include:: credits.rst.inc
.. include:: debits.rst.inc
.. include:: holds.rst.inc
.. include:: refunds.rst.inc
.. include:: events.rst.inc
_.. include:: callbacks.rst.inc
