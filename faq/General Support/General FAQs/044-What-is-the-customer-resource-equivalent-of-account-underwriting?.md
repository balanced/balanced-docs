---

layout: faq
author: Ryan Loomba, Patrick Cieplak
title: What is the customer resource equivalent of account underwriting?
category: api
tags:
- balanced
- payments
- faq
- underwriting
- customer
- account


---

Unlike the account resource, you do not explicitly underwrite the customer resource. Rather, the customer resource has an attribute called "is_identity_verified", which will be set to true once enough optional properties on the customer have been set.
