// bankAccountHref is the stored href for the bank account
BankAccount bankAccount = new BankAccount(bankAccountHref);
try {
    bankAccount.verify();
}
catch (HTTPError e) {}