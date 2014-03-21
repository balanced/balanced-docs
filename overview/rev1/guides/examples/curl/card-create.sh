curl https://api.balancedpayments.com/cards \
     -H "Accept: application/vnd.api+json;revision=1.1" \
     -u ak-test-h7F8F3u41y6LzCK4nZeVd5BafaWOUuZL: \
     -d "expiration_month=12" \
     -d "security_code=123" \
     -d "number=5105105105105100" \
     -d "expiration_year=2020"