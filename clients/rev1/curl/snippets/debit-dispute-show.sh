# :debit_id is the stored ID of the debit
curl https://api.balancedpayments.com/debits/:debit_id \
     -H "Accept: application/vnd.api+json;revision=1.1" \
     -u ak-test-aUV295IugdhWSNx2JFckYBCSvfY2ibgq:

# :dispute_id is the ID from the the debit response
curl https://api.balancedpayments.com/disputes/:dispute_id \
     -H "Accept: application/vnd.api+json;revision=1.1" \
     -u ak-test-aUV295IugdhWSNx2JFckYBCSvfY2ibgq: