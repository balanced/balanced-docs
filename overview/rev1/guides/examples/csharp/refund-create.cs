// debit_href is the stored id for the Debit
Debit debit = Debit.Fetch(debit_href);
Dictionary<string, string> payload = new Dictionary<string, string>();
payload.Add("amount", 3000);
payload.Add("description", "Refund for Order #1111");
Refund refund = debit.Refund(payload);