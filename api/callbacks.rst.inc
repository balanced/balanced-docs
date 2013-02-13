callbacks
=========

.. _callbacks:

Callbacks are publicly accessible URLs that once created will receive
notification of :ref:`event <events>` (changes to resources) via a HTTP POST
request to the ``url`` specified on the callback.
:ref:`Example payload <events.show>`

.. cssclass:: method-section

creating a new callback
-----------------------

Creates a new callback.

.. container:: method-description

  ``url`` 
      *required* **string**.  
   

.. container:: method-examples

  .. dcode:: callback_create


.. cssclass:: method-section

retrieve a callback
-------------------

Retrieves the details of a callback that was previously created. Use the
``uri`` that was previously returned, and the corresponding callback
information will be returned.

.. container:: method-examples

  .. dcode:: callback_show


.. cssclass:: method-section

list all callbacks
------------------

.. container:: method-description

  ``limit``
      *optional* integer. Defaults to ``10``.

  ``offset``
      *optional* integer. Defaults to ``0``.

.. container:: method-examples

  .. dcode:: callback_list


.. cssclass:: method-section

delete a callback
-----------------

Permanently delete a callback. It cannot be undone. It will no longer receive
any new events.

.. container:: method-description

    .. no request

.. container:: method-examples

    .. dcode:: callback_delete
