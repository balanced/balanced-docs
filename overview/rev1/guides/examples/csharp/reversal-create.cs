// credit_href is the stored href for the Credit
Credit credit = Credit.Fetch(credit_href);
Dictionary<string, string> payload = new Dictionary<string, string>();
payload.Add("amount", "3000");
payload.Add("description", "Reversal for Order #1111");
Reversal reversal = credit.Reverse(payload);