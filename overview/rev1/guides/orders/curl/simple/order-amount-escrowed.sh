# order_id: the id of the previously created order
curl https://api.balancedpayments.com/orders/:order_id \
     -H "Accept-Type: application/vnd.api+json;revision=1.1" \
     -u ak-test-1sKqYrBZG6WYpHphDAsM7ZXFEmJlAn1GE:

# examine amount_escrowed attribute