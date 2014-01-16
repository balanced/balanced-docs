API Keys
============

An ``APIKey`` resource represents the API key secret used to perform
authenticated requests with the Balanced API.


Create an API Key
-----------------

Create a new API key.

.. container:: code-white

  .. dcode:: scenario api_key_create


Retrieve an API Key
--------------------

Get an existing API key.

.. container:: code-white

  .. dcode:: scenario api_key_show


List all API Keys
-----------------

List all API keys for the marketplace.

.. cssclass:: dl-horizontal dl-params

  ``limit``
      *optional* integer. Defaults to ``10``.

  ``offset``
      *optional* integer. Defaults to ``0``.

.. container:: code-white

  .. dcode:: scenario api_key_list


Delete an API Key
-----------------

Delete an API key.

.. container:: code-white

  .. dcode:: scenario api_key_delete