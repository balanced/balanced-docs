Errors
======

Fields
------

.. pez:: balanced_service.controllers.views:HTTPException

Status Codes
------------

**200** OK - Resource(s) retrieved successfully.

**201** Created - Resource created.

**204** No Content - Resource deleted.

**400** Bad Request - Request is improper.

**401** Unauthorized - HTTP Authentication must be used to access the requested URI.

**404** Not Found - Requested URI doesn't exist.

**405** Method Not Allowed - HTTP method used is not allowed for the requested URI.

**500, 502, 503, 504** Internal Server Error - Something went wrong on Balanced's side.

Category Types
--------------

**request** - Malformed requests.

**banking** - Errors related to banking/payment processing.

**logical** - Errors related to requests that are well-formed, but logically inconsistent.

Category Codes
--------------

.. dcode:: error
    :sort: category_type category_code
