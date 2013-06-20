---

layout: faq
author: Ryan
title: Where can I include text that will be displayed on a customer's credit card statement?
category: api
tags:
- balanced
- payments
- faq
- credit
- card
- statement
- soft descriptor

---

When creating a new debit, there is an optional field `appears_on_statement_as` that takes a string, please see [api reference for creating a new debit](https://docs.balancedpayments.com/current/api?#create-a-new-debit) for more info. The string can include ASCII letters(a-z and A-Z), digits(0-9) and special characters(.<>(){}[]+&!$*;-%_?:#@~='" ^\`|). All other characters will be rejected. Please note that the **length <= 22**. The `description` optional field is different and to be used internally for descriptions.
