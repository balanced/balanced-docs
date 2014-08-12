// bank_account_href is the stored href for the BankAccount
BankAccount bankAccount = BankAccount.Fetch(bank_account_href);
Dictionary<string, object> creditPayload = new Dictionary<string, object>();
creditPayload.Add("amount", 5000 );
Credit credit = bankAccount.Credit(creditPayload);