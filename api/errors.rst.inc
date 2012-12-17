errors
======

Standard HTTP status codes are used to communicate the success or
failure of a request. A code in the ``2xx`` range indicates success, ``4xx``
indicates an error that resulted from the provided information (e.g. a
required parameter was missing, a bank account failed tokenization, etc),
``5xx`` indicates an error with Balanced's servers.

.. container:: method-section

  .. container:: method-description

    .. pez:: balanced_service.views:HTTPException

  .. container:: method-examples

    .. cssclass:: error-header

       http status codes

    **200** ok: resource(s) retrieved successfully.

    **201** created: resource created.

    **204** no content: resource deleted.

    **400** bad request: request is improper and/or malformed.

    **401** unauthorized: http authentication must be used to access the requested uri.

    **403** forbidden: not authorized to access the reosurce at the requested uri.

    **404** not found: requested uri doesn't exist.

    **405** method not allowed: http method used is not allowed for the requested uri.

    **500, 502, 503, 504** internal server error: something went wrong on Balanced's side.
