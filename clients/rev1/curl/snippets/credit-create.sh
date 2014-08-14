# :bank_account_id is the stored id for the BankAccount
curl https://api.balancedpayments.com/bank_accounts/:bank_account_id/credits \
        -H "Accept: application/vnd.api+json;revision=1.1" \
        -u ak-test-h7F8F3u41y6LzCK4nZeVd5BafaWOUuZL: \
        -d "amount=100000" \
        -d "description=Payout for order #1111"