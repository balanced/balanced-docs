# :order_id is the stored id for the Order
curl https://api.balancedpayments.com/orders/:order_id \
     -H "Accept: application/vnd.api+json;revision=1.1" \
     -u ak-test-1AWMAkTOKhxG856Wht6MqswjstRas7VM4:

# amount is the original order amount
# amount_escrowed will increase by amount of reversed credit
