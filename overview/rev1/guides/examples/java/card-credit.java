// cardHref is the stored href for the card
Card card = new Card(cardHref);

HashMap<String, Object> payload = new HashMap<String, Object>();
payload.put("amount", 5000);
payload.put("description", "Some descriptive text for the debit in the dashboard");
payload.put("appears_on_statement_as", "Some text");

try {
    Credit credit = card.credit(payload);
}
catch (FundingInstrumentNotCreditable e) {}
catch (HTTPError e) {}