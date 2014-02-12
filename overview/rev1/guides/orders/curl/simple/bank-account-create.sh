# create bank account
curl https://api.balancedpayments.com/bank_accounts \
     -H "Accept-Type: application/vnd.api+json;revision=1.1" \
     -u ak-test-1sKqYrBZG6WYpHphDAsM7ZXFEmJlAn1GE: \
     -d "routing_number=121000358" \
     -d "type=checking" \
     -d "name=Henry Ford" \
     -d "account_number=9900000001"

# associate bank account to customer
# bank_account_id: use id attribute from bank account created previously
curl https://api.balancedpayments.com/bank_accounts/:bank_account_id \
     -H "Accept-Type: application/vnd.api+json;revision=1.1" \
     -u ak-test-1sKqYrBZG6WYpHphDAsM7ZXFEmJlAn1GE: \
     -X PUT \
     -d "customer=/customers/CU54L5eAjiumsNS6RMzbEedW"