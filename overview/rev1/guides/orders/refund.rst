Refund an Order
-----------------

.. admonition:: References
  :header_class: alert alert-tab full-width alert-tab-persianBlue60
  :body_class: alert alert-persianBlue20

  .. cssclass:: mini-header

    API Specification

  .. cssclass:: list-noindent

    - `Reversals Collection <https://github.com/balanced/balanced-api/blob/master/fixtures/reversals.json>`_
    - `Reversal Resource <https://github.com/balanced/balanced-api/blob/master/fixtures/_models/reversal.json>`_
    - `Refunds Collection <https://github.com/balanced/balanced-api/blob/master/fixtures/refunds.json>`_
    - `Refund Resource <https://github.com/balanced/balanced-api/blob/master/fixtures/_models/refund.json>`_

  .. cssclass:: mini-header

    API Reference

  .. cssclass:: list-noindent

    - `Create a Reversal </1.1/api/reversals/#create-a-reversal>`_
    - `Create a Refund </1.1/api/refunds/#create-a-refund>`_


Begin by finding the Order you wish to refund.

.. container:: section-ruby

  .. literalinclude:: ruby/refund/order-fetch.rb
    :language: ruby

.. container:: section-python

  .. literalinclude:: python/refund/order-fetch.py
    :language: python

.. container:: section-bash

  .. literalinclude:: curl/refund/order-fetch.sh
    :language: bash

.. container:: section-php

  .. literalinclude:: php/refund/order-fetch.php
    :language: php

.. container:: section-csharp

  .. literalinclude:: csharp/refund/order-fetch.cs
    :language: csharp


Next, reverse any credits that need to be reversed.

.. container:: section-ruby

  .. literalinclude:: ruby/refund/credit-reverse.rb
    :language: ruby

.. container:: section-python

  .. literalinclude:: python/refund/credit-reverse.py
    :language: python

.. container:: section-bash

  .. literalinclude:: curl/refund/credit-reverse.sh
     :language: bash

.. container:: section-php

  .. literalinclude:: php/refund/credit-reverse.php
    :language: php

.. container:: section-csharp

  .. literalinclude:: csharp/refund/credit-reverse.cs
    :language: csharp


Once the credit has been reversed, the Order's ``amount_escrowed`` will
increase by the amount of the credit. Note that a reversal can take several
days depending on the bank where the account resides.

.. container:: section-ruby

  .. literalinclude:: ruby/refund/examine-order-after-reversal.rb
    :language: ruby

.. container:: section-python

  .. literalinclude:: python/refund/examine-order-after-reversal.py
    :language: python

.. container:: section-bash

  .. literalinclude:: curl/refund/examine-order-after-reversal.sh
    :language: bash

.. container:: section-php

  .. literalinclude:: php/refund/examine-order-after-reversal.php
    :language: php

.. container:: section-csharp

  .. literalinclude:: csharp/refund/examine-order-after-reversal.cs
    :language: csharp

Next, refund the original debit.

.. container:: section-ruby

  .. literalinclude:: ruby/refund/debit-refund.rb
    :language: ruby

.. container:: section-python

  .. literalinclude:: python/refund/debit-refund.py
    :language: python

.. container:: section-bash

  .. literalinclude:: curl/refund/debit-refund.sh
    :language: bash

.. container:: section-php

  .. literalinclude:: php/refund/debit-refund.php
    :language: php

.. container:: section-csharp

  .. literalinclude:: csharp/refund/debit-refund.cs
    :language: csharp


Once the debit has been refunded, the ``amount_escrowed`` will decrease by the
amount of the refund.

.. container:: section-ruby

  .. literalinclude:: ruby/refund/examine-order-after-refund.rb
    :language: ruby

.. container:: section-python

  .. literalinclude:: python/refund/examine-order-after-refund.py
    :language: python

.. container:: section-bash

  .. literalinclude:: curl/refund/examine-order-after-refund.sh
    :language: bash

.. container:: section-php

  .. literalinclude:: php/refund/examine-order-after-refund.php
    :language: php

.. container:: section-csharp

  .. literalinclude:: csharp/refund/examine-order-after-refund.cs
    :language: csharp