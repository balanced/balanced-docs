Going Live Checklist
======================

Each marketplace will be reviewed for business risk, sustainability, and
compliance. Even if your use case is not specifically prohibited, Balanced
reserves the right to reject or shut down the marketplace. The review
process can take up to **3 business days**. Please be sure to take this into account
for your development time and launch date. Email support@balancedpayments.com
regarding any questions related to supporting your use case.

Requirements
-------------------
**Prior to applying for production access please ensure all the steps listed
below have been completed.** Failure to do so can and will likely result in
your marketplace being shut down.

- Review the following terms and agreements:

  - `Terms & Conditions <https://www.balancedpayments.com/terms/>`_
  - `Marketplace Agreement <https://www.balancedpayments.com/terms/marketplaceagreement>`_
  - `Seller Agreement <https://www.balancedpayments.com/terms/selleragreement>`_
  - `Prohibited Use Cases <https://support.balancedpayments.com/hc/en-us/articles/200712784-What-businesses-are-prohibited-from-using-Balanced->`_
  - `Privacy Policy <https://www.balancedpayments.com/privacy>`_

- Deploy a live site, neither in private beta or behind a password wall
- Clearly convey your business model on your website
- Host your site over SSL (HTTPS) with a valid, non self-signed certificate
- Use :ref:`balanced.js <use_balanced_js>` to tokenize funding instruments
- Use the :ref:`Orders <guides.orders>` resource for all transactions
- Comply with `KYC <http://en.wikipedia.org/wiki/Know_your_customer>`_ requirements by :ref:`underwriting all merchants (sellers) <resources.test-identity-verification>` prior to issuing payouts to them
- Include client terms snippet (#5) from `marketplace agreement <https://www.balancedpayments.com/terms/marketplaceagreement>`__ in your client terms and conditions

When the above listed steps have been satisfied and you're ready to go live, you
can register for a production marketplace by signing into your dashboard,
visiting https://dashboard.balancedpayments.com/#/marketplaces, and
clicking the "Register" button at the bottom of the page.

Recommendations
-------------------
- Verify the use of :ref:`best practices <best_practices>`
- Utilize the Customer resource by always associating funding instruments to them
- Use callbacks to listen for marketplace `events </1.1/guides/events/>`_
- Supply full names when tokenizing cards
- Ensure you are using the most up-to-date, official API client version
- Review the :ref:`Disputes <guides.disputes>` guide to ensure your
  understanding of how they work and how to properly deal with them should they
  occur