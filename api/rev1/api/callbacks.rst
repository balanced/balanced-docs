Callbacks
=========

Callbacks are a means of registering to receive payloads of information
to a specific URL of your choice. You may create multiple callbacks.
Events will be sent to each callback URL. In the event that a 20x response
is not received when the payload is sent to the callback URL, the callback
will be retried up to 10 times with 10 minutes between each attempt.

|

.. container:: header3

  Available Query Filters

.. cssclass:: dl-horizontal dl-params filters

  .. dcode:: query Callbacks


.. note::
  :header_class: alert alert-tab
  :body_class: alert alert-gray

  Callbacks can be added through the Dashboard via the Webhooks area on the marketplace Settings
  page.


.. _callbacks.create:

Create a Callback
-----------------

Create a ``Callback`` to which events will be sent.

.. cssclass:: dl-horizontal dl-params

  .. dcode:: form callbacks.create

.. container:: code-white

    .. dcode:: scenario callback_create


.. _callbacks.fetch:

Fetch a Callback
-------------------

.. container:: code-white

    .. dcode:: scenario callback_show


.. _callbacks.list:

List all Callbacks
------------------

.. cssclass:: dl-horizontal dl-params

  ``limit``
      *optional* integer. Defaults to ``10``.

  ``offset``
      *optional* integer. Defaults to ``0``.

.. container:: code-white

    .. dcode:: scenario callback_list


.. _callbacks.delete:

Delete a Callback
-----------------

.. container:: code-white

    .. dcode:: scenario callback_delete