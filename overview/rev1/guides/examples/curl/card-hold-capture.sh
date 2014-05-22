# :card_hold_id is the stored id for the CardHold
curl https://api.balancedpayments.com/card_holds/:card_hold_id/debits \
     -H "Accept: application/vnd.api+json;revision=1.1" \
     -u ak-test-h7F8F3u41y6LzCK4nZeVd5BafaWOUuZL: \
     -d "appears_on_statement_as=ShowsUpOnStmt" \
     -d "description=Some descriptive text for the debit in the dashboard"