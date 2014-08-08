Dictionary<string, object> creditPayload = new Dictionary<string, object>();
creditPayload.Add("amount", 5000);
Credit credit = order.CreditTo(bankAccount, creditPayload);