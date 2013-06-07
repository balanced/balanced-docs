---

layout: faq
author: Richard Serna
title: Can I use Balanced for recurring or subscription billing?
category: processing
tags:
- balanced
- payments
- faq

---

Balanced is great for your recurring and subscription billing. When you store credit card information in the Balanced server, it stays stored there indefinitely, and you can make an API call to debit that user again whenever it makes sense for your business model (i.e. for later purchases, on some recurring schedule, etc).

Currently you have to explicitly make an API call each time you want to make another debit, so this takes some logic on your end. We’re working on a way of automating various sorts of recurring payments. Please add your voice to the [GitHub issue](https://github.com/balanced/balanced-api/issues/40) about the subject, if you’d like to see such a feature.
