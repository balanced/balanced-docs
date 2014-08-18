# :card_id is the stored id for the Card
curl https://api.balancedpayments.com/cards/:card_id/card_holds \
     -H "Accept: application/vnd.api+json;revision=1.1" \
     -u ak-test-h7F8F3u41y6LzCK4nZeVd5BafaWOUuZL: \
     -d "amount=5000" \
     -d "description=Some descriptive text for the debit in the dashboard"