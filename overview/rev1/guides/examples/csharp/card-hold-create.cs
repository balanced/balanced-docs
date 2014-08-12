// card_href is the stored href for the Card
Card card = Card.Fetch(card_href);
Dictionary<string, object> holdPayload = new Dictionary<string, object>();
holdPayload.Add("amount", 5000);
holdPayload.Add("description", "Some descriptive text for the debit in the dashboard");
CardHold cardHold = card.Hold(holdPayload);
cardHold.Save();