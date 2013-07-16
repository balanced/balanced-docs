.. _reversals:

Reversals
=========

.. cssclass:: method-section

Issue a Reversal
----------------

Issues a reversal from a credit. You can either reverse the full amount of the
credit or you can issue a partial reversal, where the amount is less than the
charged amount.

.. cssclass:: dl-horizontal dl-params

  .. dcode:: form reversals.create
     :exclude: account_uri

.. container:: code-white

  .. dcode:: scenario reversals_create

.. todo:: partial reversal

.. cssclass:: method-section

Retrieve a Reversal
-------------------

Retrieves the details of a reversal that you've previously created. Use the
``uri`` that was previously returned, and the corresponding reversal
information will be returned.

.. container:: method-description

  .. no request

.. container:: code-white

   .. dcode:: scenario reversals_show


.. cssclass:: method-section

List All Reversal
-----------------

Returns a list of reversals you've previously created. The reversals are returned
in sorted order, with the most recent reversals appearing first.

.. cssclass:: dl-horizontal dl-params

  ``limit``
      *optional* integer. Defaults to ``10``.

  ``offset``
      *optional* integer. Defaults to ``0``.

.. container:: code-white

   .. dcode:: scenario reversals_list


.. cssclass:: method-section

List All Reversals For an Customer
----------------------------------

Returns a list of reversals you've previously created against a specific customer.
The reversals are returned in sorted order, with the most recent reversals
appearing first.

.. cssclass:: dl-horizontal dl-params

  ``limit``
      *optional* integer. Defaults to ``10``.

  ``offset``
      *optional* integer. Defaults to ``0``.

.. container:: code-white

   .. dcode:: scenario reversals_customer_list


.. cssclass:: method-section

Update a Reversals
------------------

Updates information about a reversal

.. cssclass:: dl-horizontal dl-params

   .. dcode:: form reversals.update

.. container:: code-white

   .. dcode:: scenario reversals_update
