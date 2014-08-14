# customer_id: the id of the customer previously created
curl https://api.balancedpayments.com/customers/:customer_id/orders \
     -H "Accept-Type: application/vnd.api+json;revision=1.1" \
     -u ak-test-1sKqYrBZG6WYpHphDAsM7ZXFEmJlAn1GE: \
     -d "description=Order #12341234"