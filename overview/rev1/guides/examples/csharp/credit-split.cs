// bank_account_href_a is the stored href for the BankAccount for Person A
BankAccount bank_account_person_a = BankAccount.Fetch(bank_account_href_a);
Dictionary<string, object> creditPayload = new Dictionary<string, object>();
creditPayload.Add("amount", 5000);
creditPayload.Add("description", "Payout for order #1111");
Credit credit = bank_account_person_a.Credit(creditPayload);

// bank_account_href_b is the stored href for the BankAccount for Person B
BankAccount bank_account_person_b = BankAccount.Fetch(bank_account_href_b);
Dictionary<string, object> creditPayload = new Dictionary<string, object>();
creditPayload.Add("amount", 5000);
creditPayload.Add("description", "Payout for order #1111");
Credit credit = bank_account_person_b.Credit(creditPayload);