# credit from the order
# bank_account_id: the id of a bank_account to be credited
# order_id: the id of the order to associate the credit
curl https://api.balancedpayments.com/bank_accounts/:bank_account_id/credits \
     -H "Accept-Type: application/vnd.api+json;revision=1.1" \
     -u ak-test-1sKqYrBZG6WYpHphDAsM7ZXFEmJlAn1GE: \
     -d "amount=8000" \
     -d "order=/orders/:order_id"