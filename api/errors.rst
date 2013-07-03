errors
======

Standard HTTP status codes are used to communicate the success or
failure of a request. A code in the ``2xx`` range indicates success, ``4xx``
indicates an error that resulted from the provided information (e.g. a
required parameter was missing, a bank account failed tokenization, etc),
``5xx`` indicates an error with Balanced's servers.

.. cssclass:: dl-horizontal dl-params

   .. dcode:: view http_exception


.. container:: bg-white

  .. container:: header3 spaced-out

      HTTP Status Codes

  .. cssclass:: spaced-out

     **200** ok: resource(s) retrieved successfully.

