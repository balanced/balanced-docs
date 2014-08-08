# card_href is the stored href for the Card
Card card = Card.Fetch(card_href);
Dictionary<string, object> creditPayload = new Dictionary<string, object>();
creditPayload.Add("amount", 5000);
creditPayload.Add("description", "Some descriptive text for the debit in the dashboard");
Credit credit = card.Credit(creditPayload);