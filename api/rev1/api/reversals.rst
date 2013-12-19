.. _reversals:

Reversals
==========


Create a Reversal
-----------------

Initiates a reversal for a credit for the full amount of the credit. 

.. cssclass:: dl-horizontal dl-params

  .. dcode:: form reversals.create

.. container:: code-white

  .. dcode:: scenario reversal_create


Retrieve a Reversal
-------------------

Retrieve a previously created reversal.

.. container:: method-description

  .. no request

.. container:: code-white

   .. dcode:: scenario reversal_show


Update a Reversal
-----------------

Updates information on a reversal.

.. cssclass:: dl-horizontal dl-params

   .. dcode:: form reversals.update

.. container:: code-white

   .. dcode:: scenario reversal_update


List All Reversals
------------------

Returns a list of all previously created reversal. The reversals are returned
in sorted order, with the most recent reversals appearing first.

.. cssclass:: dl-horizontal dl-params

  ``limit``
      *optional* integer. Defaults to ``10``.

  ``offset``
      *optional* integer. Defaults to ``0``.

.. container:: code-white

   .. dcode:: scenario reversal_list


.. List All Reversals For a Customer
.. ---------------------------------
.. 
.. Returns a list of reversals you've previously created against a specific account.
.. The reversals are returned in sorted order, with the most recent reversals
.. appearing first.
.. 
.. .. cssclass:: dl-horizontal dl-params
.. 
..   ``limit``
..       *optional* integer. Defaults to ``10``.
.. 
..   ``offset``
..       *optional* integer. Defaults to ``0``.
.. 
.. .. container:: code-white
.. 
..    .. dcode:: scenario reversal_customer_list

