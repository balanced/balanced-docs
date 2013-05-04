events
======

.. _events:

You can configure events to be published via a ``POST`` to the endpoint of your
choice via callbacks. Once configured, events are accessible via the
:ref:`events <events>` endpoint.

Event types
-----------

All transactional resources (accounts, holds, credits etc) are evented.
The format of the type field is ``resource.event_type`` where ``event_type`` is
one of ``created``, ``updated``, ``deleted``, as well as some transaction
specific event types ``succeeded``, ``failed``, and ``canceled``.

Transactional Events
~~~~~~~~~~~~~~~~~~~~

.. dcode:: enum audit_event_type
   :include: credit.* debit.* hold.* refund.*

Funding Instrument Events
~~~~~~~~~~~~~~~~~~~~~~~~~

.. dcode:: enum audit_event_type
   :include: card.* bank_account.*


.. cssclass:: method-section

retrieve an event
-----------------

.. _events.show:

Retrieves the details of an event that was previously created. Use the
``uri`` that was previously returned, and the corresponding event
information will be returned.

.. container:: method-description

    .. no request

.. container:: method-examples

    .. dcode:: scenario event_show


.. cssclass:: method-section

list all events
---------------

.. container:: method-description

  ``limit``
    *optional* integer. Defaults to ``10``.

  ``offset``
    *optional* integer. Defaults to ``0``.

.. container:: method-examples

  .. dcode:: scenario event_list
