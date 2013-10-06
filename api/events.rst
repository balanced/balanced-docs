Events
======

.. _events:

You can configure events to be published via a ``POST`` to the endpoint of your
choice via callbacks. Once configured, events are accessible via the
:ref:`events <events>` endpoint.

.. note::
   :header_class: alert alert-tab-red
   :body_class: alert alert-gray

   Balanced may deliver more than one event with the same payload, but with a
   different event id.
   

Event types
-----------

All transactional resources (accounts, holds, credits etc) are evented.
The format of the type field is ``resource.event_type`` where ``event_type`` is
one of ``created``, ``updated``, ``deleted``, as well as some transaction
specific event types ``succeeded``, ``failed``, and ``canceled``.

Transactional Events
~~~~~~~~~~~~~~~~~~~~

.. cssclass:: dl-horizontal dl-params

  .. dcode:: enum audit_event_type
     :include: credit.* debit.* hold.* refund.* reversal.*

Funding Instrument Events
~~~~~~~~~~~~~~~~~~~~~~~~~

.. cssclass:: dl-horizontal dl-params

.. dcode:: enum audit_event_type
   :include: card.* bank_account.* bank_account_verification.*


.. cssclass:: method-section

Retrieve an Event
-----------------

.. _events.show:

Retrieves the details of an event that was previously created. Use the
``uri`` that was previously returned, and the corresponding event
information will be returned.

.. container:: method-description

    .. no request

.. container:: code-white

    .. dcode:: scenario event_show


.. cssclass:: method-section

List all Events
---------------

.. cssclass:: dl-horizontal dl-params:

  ``limit``
    *optional* integer. Defaults to ``10``.

  ``offset``
    *optional* integer. Defaults to ``0``.

.. cssclass:: dl-horizontal dl-params:

.. container:: code-white

  .. dcode:: scenario event_list
