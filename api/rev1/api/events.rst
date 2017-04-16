Events
======

An ``Event`` resource represents Balanced systemic events to which applications
may subscribe via a :ref:`callback <callbacks.create>`. Events are published via
an HTTP ``GET`` or ``POST`` request to the endpoint of your choice.

.. note::
   :header_class: alert alert-tab
   :body_class: alert alert-green

   Balanced may deliver more than one event with the same payload, but with a
   different event id.


.. container:: header3

  Available Query Filters

.. cssclass:: dl-horizontal dl-params filters

  .. dcode:: query Events


.. container:: header2

  Event Types

.. container:: header3

  Transactional Events

.. cssclass:: dl-horizontal dl-params filters

  .. dcode:: enum audit_event_type
    :include: credit.* debit.* hold.* refund.* reversal.*


.. container:: header3

  Funding Instrument Events

.. cssclass:: dl-horizontal dl-params filters

  .. dcode:: enum audit_event_type
    :include: card.* bank_account.* bank_account_verification.*


.. container:: header3

  Other Events

.. cssclass:: dl-horizontal dl-params filters

  .. dcode:: enum audit_event_type
    :include: account.* order.* dispute.* settlement.*


Fetch an Event
-----------------

.. _events.show:

Fetches the details of an event that was previously created.

.. container:: code-white

    .. dcode:: scenario event_show


List all Events
---------------

.. cssclass:: dl-horizontal dl-params

  ``limit``
      *optional* integer. Defaults to ``10``.

  ``offset``
      *optional* integer. Defaults to ``0``.

.. container:: code-white

  .. dcode:: scenario event_list