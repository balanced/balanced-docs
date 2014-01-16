.. _reversals:

Reversals
==========

A ``Refund`` resource represents a refund of a ``Debit`` transaction.

|

.. container:: header3

  Available Query Filters

.. cssclass:: dl-horizontal dl-params filters

  .. dcode:: query Reversals


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


Update a Reversal
-----------------

Updates information on a reversal.

.. cssclass:: dl-horizontal dl-params

   .. dcode:: form reversals.update

.. container:: code-white

   .. dcode:: scenario reversal_update