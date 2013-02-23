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

credit.canceled 
    Occurs whenever a credit is canceled. 
 
credit.created 
    Occurs whenever a new credit is created. 
 
credit.failed 
    Occurs whenever a credit is rejected. 
 
credit.succeeded 
    Occurs whenever a credit is successfully captured or deposited. 
 
credit.updated 
    Occurs whenever a credit is updated. 
 
debit.canceled 
    Occurs whenever a debit is canceled. 
 
debit.created 
    Occurs whenever a new debit is created. 
 
debit.failed 
    Occurs whenever a debit is rejected. 
 
debit.succeeded 
    Occurs whenever a debit is successfully captured or deposited. 
 
debit.updated 
    Occurs whenever a debit is updated. 
 
hold.canceled 
    Occurs whenever a hold is canceled. 
 
hold.created 
    Occurs whenever a new hold is created. 
 
hold.failed 
    Occurs whenever a hold is rejected. 
 
hold.succeeded 
    Occurs whenever a hold is successfully captured or deposited. 
 
hold.updated 
    Occurs whenever a hold is updated. 
 
refund.canceled 
    Occurs whenever a refund is canceled. 
 
refund.created 
    Occurs whenever a new refund is created. 
 
refund.failed 
    Occurs whenever a refund is rejected. 
 
refund.succeeded 
    Occurs whenever a refund is successfully captured or deposited. 
 
refund.updated 
    Occurs whenever a refund is updated. 
 

Funding Instrument Events
~~~~~~~~~~~~~~~~~~~~~~~~~

card.created 
    Occurs whenever a new card is created. 
 
card.deleted 
    Occurs whenever a card is deleted. 
 
card.updated 
    Occurs whenever a card is updated. 
 
bank_account.created 
    Occurs whenever a new bank_account is created. 
 
bank_account.deleted 
    Occurs whenever a bank_account is deleted. 
 
bank_account.updated 
    Occurs whenever a bank_account is updated. 
 

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

    .. dcode:: event_show


.. cssclass:: method-section

list all events
---------------

.. container:: method-description

  ``limit``
    *optional* integer. Defaults to ``10``.

  ``offset``
    *optional* integer. Defaults to ``0``.

.. container:: method-examples

  .. dcode:: event_list
