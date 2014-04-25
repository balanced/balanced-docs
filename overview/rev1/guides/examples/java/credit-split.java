// bankAccountHrefA is the stored href for the bank account for Person A
BankAccount bankAccountA = new BankAccount(bankAccountHrefA);

HashMap<String, Object> payloadA = new HashMap<String, Object>();
payloadA.put("amount", 50000);
payloadA.put("description", "Payout for order #1111");

try {
    Credit credit = bankAccountA.credit(payloadA);
}
catch (HTTPError e) {}


// bankAccountHrefB is the stored href for the bank account for Person A
BankAccount bankAccountB = new BankAccount(bankAccountHrefB);

HashMap<String, Object> payloadB = new HashMap<String, Object>();
payloadB.put("amount", 50000);
payloadB.put("description", "Payout for order #1111");

try {
    Credit credit = bankAccountB.credit(payloadB);
}
catch (HTTPError e) {}