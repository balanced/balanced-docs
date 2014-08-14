curl https://api.balancedpayments.com/bank_accounts \
     -H "Accept: application/vnd.api+json;revision=1.1" \
     -u ak-test-h7F8F3u41y6LzCK4nZeVd5BafaWOUuZL: \
     -d "routing_number=121000358" \
     -d "type=checking" \
     -d "name=Johann Bernoulli" \
     -d "account_number=9900000001"