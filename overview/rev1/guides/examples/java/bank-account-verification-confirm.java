// verificationHref is the stored href for the bank account verification
BankAccountVerification verification = new BankAccountVerification(verificationHref);
try {
    verification.confirm(1, 1);
}
catch (HTTPError e) {}