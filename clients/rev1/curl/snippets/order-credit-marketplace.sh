# Get the marketplace
curl https://api.balancedpayments.com/marketplaces \
   -H "Accept: application/vnd.api+json;revision=1.1" \
   -u ak-test-h7F8F3u41y6LzCK4nZeVd5BafaWOUuZL:

# Determine owner customer from marketplaces.owner_customer link and get its bank accounts
curl https://api.balancedpayments.com/customers/:customer_id/bank_accounts \
   -H "Accept: application/vnd.api+json;revision=1.1" \
   -u ak-test-h7F8F3u41y6LzCK4nZeVd5BafaWOUuZL:

# Use the bank account id to create a credit
# Use the order id to associate the credit with the order
curl https://api.balancedpayments.com/bank_accounts/:bank_account_id/credits \
   -H "Accept: application/vnd.api+json;revision=1.1" \
   -u ak-test-h7F8F3u41y6LzCK4nZeVd5BafaWOUuZL: \
   -d "amount=2000" \
   -d "order=/orders/:order_id"