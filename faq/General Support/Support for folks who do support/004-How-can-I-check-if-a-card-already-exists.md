---

layout: faq
author: Ryan Loomba
title: How can I check if a card already exists?
category: api
tags:
- balanced
- payments
- faq
- api
- customer
- card


---

If you are adding a customer's card and want to check to see if it exists already, you can check the `hash` attribute of the card. If the hash of the card matches another card's hash on file, then that card has already been aded.
