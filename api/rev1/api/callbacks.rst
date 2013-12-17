Callbacks
=========

.. _callbacks:

Callbacks are a means of registering to receive payloads of information to a specific URL of your choice.
You may create multiple callbacks. Events will be sent to each callback URL. In the event that a 20x response
is not received when the payload is sent to the callback URL, the callback will be retried at increasing 
intervals and will eventually expire after several tries.


Create a Callback
-----------------

.. _callbacks.create:


.. cssclass:: dl-horizontal dl-params

  .. dcode:: form callbacks.create

.. container:: code-white

    .. dcode:: scenario callback_create


Retrieve a Callback
-------------------

.. _callbacks.retrieve:


.. container:: code-white

    .. dcode:: scenario callback_show


.. cssclass:: method-section


List all Callbacks
------------------

.. _callbacks.list:


.. container:: code-white

    .. dcode:: scenario callback_list


.. cssclass:: method-section


Delete a Callback
-----------------

.. _callbacks.delete:


.. container:: code-white

    .. dcode:: scenario callback_delete
