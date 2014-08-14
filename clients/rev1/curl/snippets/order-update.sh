# order_id: the id from a previously created order
curl https://api.balancedpayments.com/orders/:order_id \
     -H "Accept-Type: application/vnd.api+json;revision=1.1" \
     -u ak-test-1sKqYrBZG6WYpHphDAsM7ZXFEmJlAn1GE: \
     -X PUT \
     -d "description=Item description" \
     -d "meta[item_url]=https://neatitems.com/12342134123" \