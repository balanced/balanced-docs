Events
======

.. _events:

Events are published via an HTTP ``GET`` or ``POST`` request to the endpoint of your
choice via a :ref:`callbacks <callbacks>`.

.. note::
   :header_class: alert alert-tab-red
   :body_class: alert alert-gray

   Balanced may deliver more than one event with the same payload, but with a
   different event id.


Event types
-----------

All transactional resources (customers, holds, credits etc) are evented.
The format of the type field is ``resource.event_type`` where ``event_type`` is
one of ``created``, ``updated``, ``deleted``, as well as some transaction
specific event types ``succeeded``, ``failed``, and ``canceled``.

Transactional Events
~~~~~~~~~~~~~~~~~~~~

  .. dcode:: enum audit_event_type
     :include: credit.* debit.* hold.* refund.* reversal.*

Funding Instrument Events
~~~~~~~~~~~~~~~~~~~~~~~~~

.. dcode:: enum audit_event_type
   :include: card.* bank_account.* bank_account_verification.*


Retrieve an Event
-----------------

.. _events.show:

Retrieves the details of an event that was previously created.

.. container:: code-white

    .. dcode:: scenario event_show


List all Events
---------------

.. container:: code-white

  .. dcode:: scenario event_list
