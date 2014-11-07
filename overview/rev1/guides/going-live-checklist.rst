Going Live Checklist
======================

- Review the `Terms & Conditions <https://www.balancedpayments.com/terms/>`_,
  `Marketplace Agreement <https://www.balancedpayments.com/terms/marketplaceagreement>`_,
  `Seller Agreement <https://www.balancedpayments.com/terms/selleragreement>`_,
  `Prohibited Use Cases <https://support.balancedpayments.com/hc/en-us/articles/200712784-What-businesses-are-prohibited-from-using-Balanced->`_,
  and `Privacy Policy <https://www.balancedpayments.com/privacy>`_. Email
  support@balancedpayments.com if you are unsure if your use case is supported
- Ensure servers use SSL
- Use :ref:`balanced.js <use_balanced_js>` to tokenize funding instruments
- Ensure you're using the :ref:`Orders <guides.orders>` resource for all transactions
- Verify the use of :ref:`best practices <best_practices>`
- Ensure that your workflow :ref:`underwrites merchants (sellers) <resources.test-identity-verification>` to whom you wish to pay out in accordance with KYC regulations
- Include client terms snippet (#5) from `marketplace agreement <https://www.balancedpayments.com/terms/marketplaceagreement>`__ in client terms and conditions
- Include the `credit card brand logos <http://www.quora.com/Balanced/I-am-in-the-process-of-adding-Balanced-to-my-site-and-want-to-use-the-Balanced-logo-Is-that-allowed>`__ on the checkout page
- Include a `"Secured by Balanced" badge <https://github.com/balanced/balanced-dashboard/issues/24#issuecomment-17952768>`__ on the site footer or checkout page
- `Register for a production marketplace <#obtain-a-production-marketplace>`_
- Register for a production marketplace by signing into your dashboard, visiting https://dashboard.balancedpayments.com/#/marketplaces, and clicking the register button at the bottom of the page
- Change API key to production API key
- Change application marketplace HREF to production marketplace HREF
