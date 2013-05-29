---

layout: faq
author: Shawnee
title: What kind of insight do we get as to the reason for credit card charge failures?
tags:
- balanced
- payments
- faq
- developer

---

Q:   What kind of insight do we get as to the reason for credit card charge failures?  Will we know whether it was because the card expired, was canceled, had insufficient funds, etc, or will just be a general failure message?

A:  We do not expose the reason for declination if the bank declines. It's success or failure.  You get a 400 if the card is expired, card number is malformed, etc.  We also specify if the bank declined or if we rejected.

There are 3 types of errors that yield a declination:

**Malformed** - We can catch the error without even send to our processor: expired, wrong security code or the card brand, etc.

**Bank Declines** --  if the bank declines, the bank declines and we don't know if it was for insuffient funds, etc., as it depends on the issuing bank

**PoundPay** rejection -- If we reject, it has to do with risk; our goal is to minimize false positives
