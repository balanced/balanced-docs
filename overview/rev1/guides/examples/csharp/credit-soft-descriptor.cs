// bank_account_href is the stored href for the BankAccount
BankAccount bankAccount = BankAccount.Fetch(bank_account_href);
Dictionary<string, object> creditPayload = new Dictionary<string, object>();
creditPayload.Add("amount", 5000);
creditPayload.Add("description", "Payout for order #1111");
creditPayload.Add("appears_on_statement_as", "GoodCo #1111");
Credit credit = bankAccount.Credit(creditPayload);