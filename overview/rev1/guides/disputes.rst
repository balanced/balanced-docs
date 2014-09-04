.. _guides.disputes:

Disputes
==========

A dispute, otherwise known as a chargeback, is the result of a customer protesting
a charge made on their credit card. A customer contacts their card provider and states
they did not authorize the transaction, which results in a dispute.

Fortunately, a marketplace may challenge the dispute by providing evidence of a legitimate
transaction.


.. admonition:: References
  :header_class: alert alert-tab full-width alert-tab-persianBlue60
  :body_class: alert alert-persianBlue20 references

  .. cssclass:: mini-header

    API Specification

  - `Disputes Collection <https://github.com/balanced/balanced-api/blob/master/fixtures/disputes.json>`_
  - `Dispute Resource <https://github.com/balanced/balanced-api/blob/master/fixtures/_models/dispute.json>`_

  .. cssclass:: mini-header

    API Reference

  - `Create a Card </1.1/api/cards/#create-a-card-direct>`_
  - `Create a Card Debit </1.1/api/debits/#create-a-card-debit>`_
  - `Fetch a Debit Dispute </1.1/api/debits/#fetch-a-debit-dispute>`_
  - `Fetch a Dispute </1.1/api/disputes/#fetch-a-dispute>`_
  - `List All Disputes </1.1/api/disputes/#list-all-disputes>`_

|


Reducing the number of chargebacks
------------------------------------

Not all disputes are intentional. Chargebacks are often the result of a customer seeing
a charge that they don’t recognize or don’t remember on their credit card statement.

Some helpful tips to prevent chargebacks:

- Use an easily identifiable statement descriptor by setting ``appears_on_statement_as``
- Set expectations regarding shipping times for physical goods and contact your customers right away if you’re alerted to any delays
- Clearly state refund policies on your website
- Make it very easy for customers to contact you, and respond in a timely fashion


Dispute fees
---------------

There is a non-refundable $15 fee for each dispute **regardless of the outcome of the dispute**.

The day Balanced receives notice of a dispute the marketplace's verified bank account
will be invoiced for the amount of the dispute and the $15 fee. Dispute charges are itemized
in Invoices assessed to the marketplace.

.. note::
  :header_class: alert alert-tab
  :body_class: alert alert-green
  
  Invoices are also accessible via the `Dashboard`_.


Refunding a disputed charge
-------------------------------

Balanced does not allow disputed debits to be refunded, as this opens the marketplace
to potentially losing these funds twice, once for the refund, and again for the dispute
itself. If challenging the dispute is undesired, rather than issuing a refund, contact
support@balancedpayments.com and ask that the dispute be accepted on your behalf, which
will effectively refund the customer.


Challenging a Dispute
----------------------
Once you receive notification of a chargeback it’s important to reach out directly to
the customer and find out why they are initiating the dispute. Often times customers
will forget making a particular charge and contest it. In this case, reaching out to
the customer will remind them of the charge, and call their card provider to cancel
the chargeback.

.. note::
  :header_class: alert alert-tab-yellow
  :body_class: alert alert-yellow
  
  The $15 dispute fee will still be assessed even if the customer cancels the dispute.


Unfortunately, not all disputes are as easily resolved. If you are unable to reach a
customer, or they are not being cooperative, the next steps are to gather as much
documentation as possible to demonstrate fulfillment of the transaction and send it
to support@balancedpayments.com. Balanced will use the supplied documentation to
fight the dispute on your behalf directly with the credit card provider. The
following types of documentation can help you win a chargeback:


- Tracking information for goods that are physically delivered, such as a Fedex/UPS tracking number, etc.
- A PDF of any email exchanges between yourself and the customer where you remind them of the initial charge
- Receipts of purchase emailed to the cardholder upon completion of the purchase process

This information may be provided only in the following formats:

- pdf
- docx
- jpg

Even if a customer agrees to cancel the chargeback, Balanced recommends
submitting documentation of transaction fulfillment so the dispute is contested
on your behalf so you’re protected in the event the customer forgets to cancel
the dispute!

Once documentation has been submitted, Balanced will fight the chargeback on your
behalf. The card provider will decide to either rule in favor of the marketplace
or the customer, which status will be indicated by a transition from a value of
``pending`` to one of ``won`` or ``lost``. 


Dispute Notifications
-------------------------

When your marketplace has chargebacks, in addition to them being visible in your `Dashboard`_,
Balanced will also send an email to your marketplace email address to advise you of them.

.. code-block:: text

  Greetings, 

  You have received 2 disputes in the past seven days. 

  You may view further details at the following link:   
  https://dashboard.balancedpayments.com/#/marketplaces/MP5G864SDF86S4jy8qsdf4zK/activity/disputes 

  Once you receive notification of a new chargeback please reach out to the 
  customer and remind them of the charge, and ask them to rescind the 
  chargeback if they recognize and accept the charge. Additionally, please 
  send supporting documentation to support@balancedpayments.com so that we 
  can fight the chargeback on your behalf. This documentation may include: 

  - An email exchange between yourself and the customer where they recognize 
  and accept the charges, and promise to cancel the chargeback 
  - A receipt emailed to the cardholder upon purchase of the good or service 
  - Delivery tracking information, such as Fedex/UPS shipping numbers. 

  If you have any questions about how to respond to a specific chargeback 
  please don't hesitate to ask us at support@balancedpayments.com. 

  Thanks, 
  Balanced


Viewing Disputes
---------------------

Disputes may be retrieved in three ways.

Retrieve via the ``Debit``:

.. snippet:: debit-dispute-show


Retrieve by href:

.. snippet:: dispute-show


You may also list all disputes:

.. snippet:: dispute-list


.. note::
  :header_class: alert alert-tab
  :body_class: alert alert-green
  
  Disputes are also accessible via the `Dashboard`_.


Testing Disputes
------------------

In test marketplaces, creating a ``Card`` with the number ``6500000000000002``, will create a dispute for
any debit created with the card.


.. snippet:: card-create-dispute


Now debit the card.

.. snippet:: card-debit


After some time has passed, a dispute will be associated to the ``Debit``.




.. _Dashboard: https://dashboard.balancedpayments.com/

