curl https://api.balancedpayments.com/customers \
     -H "Accept-Type: application/vnd.api+json;revision=1.1" \
     -u ak-test-1sKqYrBZG6WYpHphDAsM7ZXFEmJlAn1GE: \
     -d "name=Henry Ford" \
     -d "dob_year=1963" \
     -d "dob_month=7" \
     -d "address[postal_code]=48120"