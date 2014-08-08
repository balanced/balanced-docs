# time has elapsed, so find the BankAccountVerification
BankAccountVerification verification = BankAccountVerification.Fetch("/verifications/BZ2Sy2Z4Bp2mARnCLztiu2VG");
verification.Confirm(1, 1);