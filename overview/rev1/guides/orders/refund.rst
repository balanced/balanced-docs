Refund an Order
-----------------

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