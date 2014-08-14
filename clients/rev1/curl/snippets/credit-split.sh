# :bank_account_id_a is the stored id for the BankAccount for Person A
curl https://api.balancedpayments.com/bank_accounts/:bank_account_id_a/credits \
        -H "Accept: application/vnd.api+json;revision=1.1" \
        -u ak-test-h7F8F3u41y6LzCK4nZeVd5BafaWOUuZL: \
        -d "amount=50000" \
        -d "description=Payout for order #1111"

# :bank_account_id_b is the stored id for the BankAccount for Person B
curl https://api.balancedpayments.com/bank_accounts/:bank_account_id_b/credits \
        -H "Accept: application/vnd.api+json;revision=1.1" \
        -u ak-test-h7F8F3u41y6LzCK4nZeVd5BafaWOUuZL: \
        -d "amount=50000" \
        -d "description=Payout for order #1111"