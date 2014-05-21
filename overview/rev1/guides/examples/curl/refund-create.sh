# :debit_id is the stored id for the Debit
curl https://api.balancedpayments.com/debits/:debit_id/refunds \
     -H "Accept: application/vnd.api+json;revision=1.1" \
     -u ak-test-h7F8F3u41y6LzCK4nZeVd5BafaWOUuZL: \
     -d "amount=3000" \
     -d "description=Refund for Order #1111" \
     -d "meta[merchant.feedback]=positive" \
     -d "meta[user.refund_reason]=not happy with product" \
     -d "meta[fulfillment.item.condition]=OK"