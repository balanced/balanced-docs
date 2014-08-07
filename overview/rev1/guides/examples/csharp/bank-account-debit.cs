# bank_account_href is the stored href for the BankAccount
BankAccount bankAccount = BankAccount.Fetch(bank_account_href);
Dictionary<string, object> payload = new Dictionary<string, object>();
payload.Add("amount", 5000);
payload.Add("appears_on_statement_as", "Statement text");
payload.Add("description", "Some descriptive text for the debit in the dashboard");
Debit debit = bankAccount.Debit(payload);