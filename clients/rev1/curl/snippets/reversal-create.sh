# :credit_id is the stored id for the Credit
# :order_href is the stored href for the Order
curl https://api.balancedpayments.com/credits/:credit_id/reversals \
     -H "Accept: application/vnd.api+json;revision=1.1" \
     -u ak-test-h7F8F3u41y6LzCK4nZeVd5BafaWOUuZL: \
     -d "amount=100000" \
     -d "description=Reversal for Order #1111" \
     -d "meta[merchant.feedback]=positive" \
     -d "meta[user.refund_reason]=not happy with product" \
     -d "meta[fulfillment.item.condition]=OK" \
     -d "order=:order_href"