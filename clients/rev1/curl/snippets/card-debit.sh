# :card_id is the stored ID for the card
# :order_href is the stored href for the Order
curl https://api.balancedpayments.com/cards/:card_id/debits \
     -H "Accept: application/vnd.api+json;revision=1.1" \
     -u ak-test-h7F8F3u41y6LzCK4nZeVd5BafaWOUuZL: \
     -d "appears_on_statement_as=Statement text" \
     -d "amount=5000" \
     -d "description=Some descriptive text for the debit in the dashboard" \
     -d "order=:order_href"