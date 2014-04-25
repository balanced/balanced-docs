curl https://api.balancedpayments.com/cards \
     -H "Accept: application/vnd.api+json;revision=1.1" \
     -u ak-test-1PPfI4CmXSaOHFgIYzWdA5fpdkYe9mvLL: \
     -d "expiration_month=12" \
     -d "cvv=123" \
     -d "number=6500000000000002" \
     -d "expiration_year=2020"