.. initial feedback:
  hard to go back in the doc

.. dcode-default::
    :cache: dcode.cache

.. dcode-default:: scenario
    :script: scripts/lang-scenario.py -d scenarios -c scenario.cache
    :section-include: request
    :section-chars: ~^
<<<<<<< HEAD
..     :lang: python ruby php node
=======
    :lang: python ruby php node java
>>>>>>> 0f932982ea0ca45c3d7e4b0d42265c4a43a7500d

.. contents::
  :depth: 2
  :backlinks: none

.. container:: langbar

  Clients:

  * curl
  * ruby
  * python
  * php
  * node
  * java

.. include:: includes/overview.rst

.. include:: includes/tokenization.rst

.. include:: includes/payouts.rst

.. include:: includes/processing.rst

.. include:: includes/bank_account_debits.rst

.. include:: includes/marketplaces.rst

.. include:: includes/reference.rst

.. include:: includes/bestpractices.rst
