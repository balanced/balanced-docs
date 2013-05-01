.. _holds:

holds
=====

Holds are a type of authorization that reserves (i.e. holds) a dollar amount
on the customer's credit card, usually within 7 days.

A successful hold can be captured, and as a result, creates a
:ref:`debit <debits>`.

.. cssclass:: method-section

create a new hold
-----------------

Creates a hold against a card. Returns a ``uri`` that can later be used to
create a debit, up to the full amount of the hold.

.. container:: method-description

  .. dcode:: form debits.create

.. container:: method-examples

  .. dcode:: scenario hold_create


.. cssclass:: method-section

retrieve a hold
---------------

Retrieves the details of a hold that you've previously created. Use the
``uri`` that was previously returned, and the corresponding hold
information will be returned.

.. container:: method-description

  .. no request

.. container:: method-examples

   .. dcode:: scenario hold_show


.. cssclass:: method-section

list all holds
--------------

Returns a list of holds you've previously created. The holds are returned
in sorted order, with the most recent holds appearing first.

.. container:: method-description

  ``limit``
      *optional* integer. Defaults to ``10``.

  ``offset``
      *optional* integer. Defaults to ``0``.

.. container:: method-examples

   .. dcode:: scenario hold_list


.. cssclass:: method-section

list all holds for an account
-----------------------------

Returns a list of holds you've previously created against a specific account.
The holds are returned in sorted order, with the most recent holds appearing
first.

.. container:: method-description

  ``limit``
      *optional* integer. Defaults to ``10``.

  ``offset``
      *optional* integer. Defaults to ``0``.

.. container:: method-examples

   .. dcode:: scenario hold_account_list


.. cssclass:: method-section

update a hold
-------------

Updates information about a hold

.. container:: method-description

  .. dcode:: form debits.update

.. container:: method-examples

   .. dcode:: scenario hold_update


.. cssclass:: method-section

capture a hold
--------------

Captures a hold. This creates a :ref:`debit <debits>`.

.. container:: method-description

   Use ``hold_uri`` when :ref:`creating a debit <debits.create>`.

.. container:: method-examples

   .. dcode:: scenario hold_capture


.. cssclass:: method-section

void a hold
-----------

Voids a hold. This cancels the hold. After voiding, the hold can no longer
be captured. This operation is irreversible.

.. container:: method-description

  .. dcode:: form holds.update
     :includes: is_void appears_on_statement_as

.. container:: method-examples

   .. dcode:: scenario hold_void
