# bank_account_id is the ID of the bank account to settle against
curl https://api.balancedpayments.com/accounts/:account_id/settlements \
     -H "Accept: application/vnd.api+json;revision=1.1" \
     -u ak-test-1GbtHCjTbxEnnmpNyQ52gpVGeUfCVRFZY: \
     -d "funding_instrument=/bank_accounts/:bank_account_id" \
     -d "description=A description"