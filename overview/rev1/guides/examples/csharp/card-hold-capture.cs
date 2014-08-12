// card_hold_href is the stored href for the CardHold
CardHold cardHold = CardHold.fetch(card_hold_href);
Dictionary<string, object> debitPayload = new Dictionary<string, object>();
debitPayload.Add("appears_on_statement_as", "ShowsUpOnStmt");
debitPayload.Add("description", "Some descriptive text for the debit in the dashboard");
Debit debit = cardHold.Capture(debitPayload);