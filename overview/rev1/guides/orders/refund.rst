Refund an Order
-----------------

Begin by finding the Order you wish to refund.

.. container:: section-ruby

  .. literalinclude:: ruby/find-order.rb
     :language: ruby

.. container:: section-python

..  .. include:: python/library-setup.rst

.. container:: section-java

..  .. include:: java/library-setup.rst
  


Next, reverse any credits that need to be reversed.

.. container:: section-ruby

  .. literalinclude:: ruby/reverse-credit.rb
     :language: ruby

.. container:: section-python

..  .. include:: python/library-setup.rst

.. container:: section-java

..  .. include:: java/library-setup.rst

  

Once the credit has been reversed, the Order's ``amount_escrowed`` will
increase by the amount of the credit. Note that a reversal can take several
days depending on the bank where the account resides.

.. container:: section-ruby

  .. literalinclude:: ruby/examine-order-after-reversal.rb
     :language: ruby

.. container:: section-python

  .. include:: python/library-setup.rst

.. container:: section-java

..  .. include:: java/library-setup.rst

  

Next, refund the original debit.

.. container:: section-ruby

  .. literalinclude:: ruby/refund-debit.rb
     :language: ruby

.. container:: section-python

  .. include:: python/library-setup.rst

.. container:: section-java

..  .. include:: java/library-setup.rst



Once the debit has been refunded, the ``amount_escrowed`` will decrease by the
amount of the refund.

.. container:: section-ruby

  .. literalinclude:: ruby/examine-order-after-refund.rb
     :language: ruby

.. container:: section-python

  .. include:: python/library-setup.rst

.. container:: section-java

..  .. include:: java/library-setup.rst

