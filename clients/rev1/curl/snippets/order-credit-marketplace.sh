# Get the marketplace
curl https://api.balancedpayments.com/marketplaces \
   -H "Accept: application/vnd.api+json;revision=1.1" \
   -u ak-test-h7F8F3u41y6LzCK4nZeVd5BafaWOUuZL:

# Determine owner customer from marketplaces.owner_customer link and get its bank accounts
curl https://api.balancedpayments.com/customers/CU1U8FEqP5FsisYD0D5G6aS4/bank_accounts \
   -H "Accept: application/vnd.api+json;revision=1.1" \
   -u ak-test-h7F8F3u41y6LzCK4nZeVd5BafaWOUuZL:

# Determine the debits href from the bank_accounts.debits link and create a credit
curl https://api.balancedpayments.com/bank_accounts/BA1VKlrw3m7lNyouaU5h8Xba/credits \
   -H "Accept: application/vnd.api+json;revision=1.1" \
   -u ak-test-h7F8F3u41y6LzCK4nZeVd5BafaWOUuZL: \
   -d "amount=2000"