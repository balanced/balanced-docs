# :credit_id is the stored id for the Credit
# :order_id is the stored id for the Order
curl https://api.balancedpayments.com/credits/:credit_id/reversals \
     -H "Accept: application/vnd.api+json;revision=1.1" \
     -u ak-test-1AWMAkTOKhxG856Wht6MqswjstRas7VM4: \
     -d "amount=5000" \
     -d "description=Reversal for Order #1111" \
     -d "meta[merchant.feedback]=positive" \
     -d "meta[user.refund_reason]=not happy with product" \
     -d "meta[fulfillment.item.condition]=OK" \
     -d "order=:order_id"
