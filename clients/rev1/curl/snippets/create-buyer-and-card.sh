# create buyer
curl https://api.balancedpayments.com/customers \
     -H "Accept-Type: application/vnd.api+json;revision=1.1" \
     -u ak-test-1sKqYrBZG6WYpHphDAsM7ZXFEmJlAn1GE: \
     -d "name=John Buyer"

# create card
curl https://api.balancedpayments.com/cards \
     -H "Accept-Type: application/vnd.api+json;revision=1.1" \
     -u ak-test-1sKqYrBZG6WYpHphDAsM7ZXFEmJlAn1GE: \
     -d "expiration_month=12" \
     -d "security_code=123" \
     -d "number=5105105105105100" \
     -d "expiration_year=2020" \
     -d "name=John Buyer"

# associate card to customer.
# card_id: the id attribute of the card created previously
# customer_id: the id attribute of customer created previously
curl https://api.balancedpayments.com/cards/:card_id \
     -H "Accept-Type: application/vnd.api+json;revision=1.1" \
     -u ak-test-1sKqYrBZG6WYpHphDAsM7ZXFEmJlAn1GE: \
     -X PUT \
     -d "customer=/customers/:customer_id"