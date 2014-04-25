Map<String, Object> payload = new HashMap<String, Object>();
payload.put("number", "6500000000000002");
payload.put("expiration_month", 12);
payload.put("expiration_year", 2020);
payload.put("cvv", "123");

Card card = new Card(payload);
try {
    card.save();
}
catch (HTTPError e) {}