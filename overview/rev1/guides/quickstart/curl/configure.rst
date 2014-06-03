There is no client library for curl. To "configure", just supply your
API key secret as basic auth (-u) in the header of each request as follows:

.. code-block:: bash

  curl https://api.balancedpayments.com/ \
       -H "Accept: application/vnd.api+json;revision=1.1" \
       -u ak-test-2aTAxvFwPKI8rhEpoVuRAXXnmgX1mLDm9: