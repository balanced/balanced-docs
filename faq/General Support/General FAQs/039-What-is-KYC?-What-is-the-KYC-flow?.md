---

layout: faq
author: Shawnee
title: What is KYC? What is the KYC flow?
category: legal
tags:
- balanced
- payments
- faq
- developer
- kyc
- confirmation
- customer
- flow
- form
- identity
- know

---

KYC stands for "Know Your Customer".  This integration is part of our PCI compliance, and it greatly reduces the potential of chargebacks and fraud.

Have a look at [https://www.balancedpayments.com/docs/api#requests-for-more-information](https://www.balancedpayments.com/docs/api#requests-for-more-information)

If we cannot identify a merchant based on the information you provide we'll give you a 300 response; you can either provide more info or redirect them to us for identity confirmation.

Here is the form we use - [https://www.balancedpayments.com/marketplaces/TEST-MP1MmWUUrOf9LdUeYrampzsZ/kyc?redirect_uri=123&merchant[type]=person](https://www.balancedpayments.com/marketplaces/TEST-MP1MmWUUrOf9LdUeYrampzsZ/kyc?redirect_uri=123&merchant[type]=person)
