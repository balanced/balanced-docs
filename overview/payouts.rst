.. _payouts:

Balanced Payouts
================

Balanced Payouts is a stand-alone service for sending money to your seller's
bank account via the ACH network. You can use Balanced Payouts with your
existing processing solution without needing to switch or you may want to
integrate :ref:`Balanced Processing <processing>`.

Tutorial
--------

At a high level, we're going to implement the credit-a-merchant endpoint and
here's how we're going to accomplish this:

* Securely collecting bank account information with ``balanced.js``
* Securely submitting that information to Balanced

Collecting bank account information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. the outline here is to show how to tokenize the fi

.. note::
   :header_class: alert alert-tab
   :body_class: alert alert-gray

   We have a fully implemented `sample page`_ for you, that you can use to get
   started immediately. At any point during this tutorial you feel overwhelmed
   or you want help, please use any of the :ref:`support channels <support>` we
   have available.

Follow the steps for :ref:`including <getting_started.including>` and
:ref:`initializing<getting_started.init>` ``balanced.js``.

We're going to use the :ref:`bank account sample form <getting_started.bank_account.form>`
from the :ref:`tokenization` section as it will do very basic information
collection for us.

.. todo:: get this form in a fully functioning state :)

For convenience, we've rendered the html into a fully functioning form:

.. container::
   :name: ba-form

   .. raw:: html
      :file: forms/ba-form.html



To collect the information from the form, we're going to enlist the help
of some simple javascript:

.. code-block:: javascript

   // TODO: Replace this with your marketplace URI
   var marketplaceUri = '{YOUR-MARKETPLACE-URI}';
   var $form = $('#bank-account-form');

   // collect the data from the form.
   var bankAccountData = {
       name: $form.find('.ba-name').val(),
       account_number: $form.find('.ba-an').val(),
       routing_number: $form.find('.ba-rn').val(),
       type: $form.find('select').val()
   };

Now, let's handle the response from Balanced using a simple callback:

.. code-block:: javascript

   function responseCallbackHandler(response) {
      switch (response.status) {
        case 400:
            // missing or invalid field - check response.error for details
            console.log(response.error);
            break;
        case 404:
            // your marketplace URI is incorrect
            console.log(response.error);
            break;
        case 201:
            // WOO HOO! MONEY!
            // response.data.uri == URI of the bank account resource you
            // should store this bank account URI to later credit it
            console.log(response.data);
            $.post('your-marketplace.tld/bank_accounts', response.data);
        }
    }

.. note::
   :header_class: alert alert-tab
   :body_class: alert alert-gray

   ``$.post('your-marketplace.tld/bank_accounts', response.data);`` is used
   as an example above. However, what you should do is iterate through the
   ``response.data`` object and add hidden form fields to submit alongside
   the form. Let us know if you need :ref:`any assistance <support>`, we're
   happy to help.

   You can find out more about the :ref:`callback here <getting_started.callback>`.

Now, let's submit it!

.. code-block:: javascript

   balanced.bankAccount.create(bankAccountData, responseCallbackHandler);


Operating on a Stored Bank Account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. operations we can perform on a bank account that we have previously created

So you're done tokenizing a bank account? Congratulations! There are several
operations that are now available to you.

Issuing a credit
''''''''''''''''
.. how to retrieve the bank account after storing it

You can issue a next-day credit/deposit/payout to this stored bank account.

.. dcode:: scenario bank_account_find_and_credit

Unstoring a bank account
''''''''''''''''''''''''

Your customers might request their bank account information deleted from your
servers and consequently, ours.

.. dcode:: scenario bank_account_find_and_delete

.. todo:: link to the bank account view on github

.. todo:: write more shit about how to handle failure

Existing credits to this bank account will still have the bank account's
``fingerprint`` associated with them because we understand that the real world
doesn't cascade and you might want to group these credits again.

However, you and your customers can rest assured that this bank account
has been deleted from our systems.


Credit's Status Field
---------------------

Credits have a ``status`` field representing the current status of the credit
through the payout process.

.. dcode:: scenario credit-show

There are three possible values for the ``status`` field on a credit:

``pending``
  As soon as the credit is created through the API, the status shows
  as ``pending``. This indicates that Balanced received the information for the
  credit and will begin processing. The ACH network itself processes transactions
  in a batch format. Batch submissions are processed at 3pm PST on business days.
  If the credit is created after 3pm PST, it will not be submitted for processing
  until 3pm PST the next business day.

``paid``
  One business day after the batch submission, the status will change to
  ``paid``. That is the _expected_ status of the credit. If the account number and
  routing number were entered correctly, the money should in fact be available to
  the seller. However, there is no immediate confirmation regarding the
  transaction showing up in the seller's account successfully

``failed``
  The seller's bank has up to three business days from when the money
  _should_ be available to indicate a rejection along with the rejection reason.
  Unfortunately, not all banks comply with ACH network policies and may respond
  after three business days with a rejection. As soon as Balanced receives the
  rejection, the status is updated to ``failed``


Payout Methods
--------------

Currently Balanced only supports payouts to bank accounts via ACH but we will
add more. All of this is publicly tracked via github issues. For example:

* `Payouts via Check <https://github.com/balanced/balanced-api/issues/69>`_
* `Pushing to Cards <https://github.com/balanced/balanced-api/issues/32>`_

Comment on those that would be useful to you or create issues for ones you'd
like to see supported!


Canceling Credits
-----------------

Canceling a credit is currently under active development and discussion on
`github issue #151`_ - it's not very straightforward due to the asynchronous
nature of ACH.

If you require immediately canceling of a credit, please contact us via any
of our :ref:`support channels <support>` and we will attempt to cancel the
credit.

When referencing a specific credit, please provide the credit's ``uri`` so that
we may quickly proceed with fulfilling your request.


Pre-funding Your Account
------------------------

Any payout issued requires maintaining sufficient money in your Balanced account.

If you do not have a sufficient balance, Balanced will return a ``409`` http
status code, stating that you do not have sufficient funds to cover your
desired ACH operation.

As a result, you will have to add funds from your bank account to your account
via the Balanced `dashboard`_.

.. tip::

   We advise that you transfer a large amount in your Balanced account or you
   may request that Balanced always keep a constant amount in your account for
   you. We're publically tracking this on `github issue #132`_ and appreciate your input

Transfers may take 2-5 days for the funds to become available; alternatively, you
may fund your account **instantly** with :ref:`Balanced Processing! <processing>`






Examples
~~~~~~~~

simulating erroneous routing numbers
''''''''''''''''''''''''''''''''''''

.. dcode:: scenario bank-account-invalid-routing-number

simulating pending status
'''''''''''''''''''''''''

.. dcode:: scenario credit_pending_state

simulating paid status
''''''''''''''''''''''

.. dcode:: scenario credit_paid_state

simulating failed status
''''''''''''''''''''''''

.. dcode:: scenario credit_failed_state


.. _payouts.cutoff:

Submission & Delivery times
---------------------------

The cutoff for submitting payouts is **3:00 PM Pacific (PT)** time. Payouts will *not* be
delivered on weekends or `bank holidays`_:

==================================== =========== =========== =========== ============ ===========
holiday                              2012        2013        2014        2015         2016
==================================== =========== =========== =========== ============ ===========
New Year's Day                       January 2   January 1   January 1   January 1    January 1
Birthday of Martin Luther King, Jr.  January 16  January 21  January 20  January 19   January 18
Washington's Birthday                February 20 February 18 February 17 February 16  February 15
Memorial Day                         May 28      May 27      May 26      May 25       May 30
Independence Day                     July 4      July 4      July 4      July 4 [*]_  July 4
Labor Day                            September 3 September 2 September 1 September 7  September 5
Columbus Day                         October 8   October 14  October 13  October 12   October 10
Veterans Day                         November 12 November 11 November 11 November 11  November 11
Thanksgiving Day                     November 22 November 28 November 27 November 26  November 24
Christmas Day                        December 25 December 25 December 25 December 25  December 26
==================================== =========== =========== =========== ============ ===========

.. [*] Saturday

Here's some common scenarios for payouts. Remember, the next-day cut off is
at **3:00 PM Pacific (PT)**.

.. list-table:: Common Payout Scenarios
   :widths: 20 35 20
   :header-rows: 1

   * - Type of Scenario
     - Example Submission Date
     - Available When? [*]_
   * - Most common
     - Tuesday @ 1:45PM PT
     - Wednesday @ 9:00AM PT
   * - `Bank holidays`_
     - July 3rd @ 1:30PM PT
     - July 5th @ 9:00AM PT
   * - Late submission
     - Friday @ 3:30PM PT
     - Tuesday @ 3:30PM PT

.. [*] Assumes that day is a working business day -- does not fall on a
       weekend or a `federal reserve holiday <bank holidays>`_.


#. Set your customer's expectation that payments might be delayed by up to
   (3) three to (5) five business days if incorrect information is provided.

#. Highlight to your customers that *wire transfer numbers* are **NOT** the same
   as the routing number, and they are **NOT** the same as the bank account
   number. Be sure to clarify this when asking your users for their information.


.. _sample page: https://gist.github.com/2662770
.. _balanced.js: https://js.balancedpayments.com/v1/balanced.js
.. _testing documentation: /docs/testing#simulating-card-failures
.. _jQuery: http://www.jquery.com
.. _dashboard: https://www.balancedpayments.com/dashboard
.. _issues: https://github.com/balanced/balanced-api/issues
.. _bank holidays: <http://www.federalreserve.gov/aboutthefed/k8.htm>
.. _FedACH directory: https://www.fededirectory.frb.org
.. _github issue #151: https://github.com/balanced/balanced-api/issues/151
.. _github issue #70: https://github.com/balanced/balanced-api/issues/70
.. _github issue #132: https://github.com/balanced/balanced-api/issues/132
