curl https://api.balancedpayments.com/callbacks \
     -H "Accept: application/vnd.api+json;revision=1.1" \
     -u ak-test-2BCjYRbHBrAzdEhef6ZqWkAjHW47E2q3X: \
     -d "url=http://www.example.com/callback" \
     -d "method=post"