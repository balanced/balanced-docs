# :account_id is the id of the account to settle
# :bank_account_href is the href of the bank account to settle against
curl https://api.balancedpayments.com/accounts/:account_id/settlements \
     -H "Accept: application/vnd.api+json;revision=1.1" \
     -u ak-test-1GbtHCjTbxEnnmpNyQ52gpVGeUfCVRFZY: \
     -d "funding_instrument=:bank_account_href" \
     -d "description=A description"