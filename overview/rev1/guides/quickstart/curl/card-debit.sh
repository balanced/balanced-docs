curl https://api.balancedpayments.com/cards/CC3een2nuWqIdotngtII70TS/debits \
     -H "Accept: application/vnd.api+json;revision=1.1" \
     -u ak-test-h7F8F3u41y6LzCK4nZeVd5BafaWOUuZL: \
     -d "appears_on_statement_as=Statement text" \
     -d "amount=5000" \
     -d "description=Some descriptive text for the debit in the dashboard"