curl https://api.balancedpayments.com/cards/:card_id \
     -H "Accept: application/vnd.api+json;revision=1.1" \
     -u ak-test-LyNyq2mVSxYSNIpvnKCDlbrZCOksWpIk: \
     -X PUT \
     -d "customer=:customer_href"