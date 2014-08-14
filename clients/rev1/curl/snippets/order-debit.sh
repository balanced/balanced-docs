# debit to the order
# card_id: the id of a card from the Customer to be charged
# ORDER_HREF: the id of the order to which the debit will be associated
curl https://api.balancedpayments.com/cards/:card_id/debits \
     -H "Accept-Type: application/vnd.api+json;revision=1.1" \
     -u ak-test-1sKqYrBZG6WYpHphDAsM7ZXFEmJlAn1GE: \
     -d "amount=10000"
     -d "order=ORDER_HREF"