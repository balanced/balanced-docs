// bankAccountHref is the stored href for the bank account
BankAccount bankAccount = new BankAccount(bankAccountHref);

HashMap<String, Object> payload = new HashMap<String, Object>();
payload.put("amount", 100000);
payload.put("description", "Payout for order #1111");
payload.put("appears_on_statement_as", "GoodCo #1111");

try {
    Credit credit = bankAccount.credit(payload);
}
catch (HTTPError e) {}