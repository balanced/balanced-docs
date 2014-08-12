// card_href is the stored href for the Card
Card card = Card.Fetch(card_href);
Dictionary<string, object> debitPayload = new Dictionary<string, object>();
debitPayload.Add("amount", 5000);
debitPayload.Add("description", "Some descriptive text for the debit in the dashboard");
debitPayload.Add("appears_on_statement_as", "Statement text");
Debit debit = card.Debit(debitPayload);