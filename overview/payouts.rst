.. _payouts:

Balanced Payouts
================

Balanced Payouts is a stand-alone service for sending money to your seller's
bank account via the ACH network. You can use Balanced Payouts with your
existing processing solution without needing to switch or you may want to
integrate :ref:`Balanced Processing <processing>`.

Credits
-------

.. container:: span6

   .. container:: header3

      Tutorials

   .. icon-box-widget::
     :box-classes: box box-block box-blue
     :icon-classes: icon icon-page

     :ref:`Collect bank account info <getting_started.collecting_bank_info>`

   .. icon-box-widget::
     :box-classes: box box-block box-blue
     :icon-classes: icon icon-page

     :ref:`Credit bank account <getting_started.credit_bank_account>`


.. container:: span6

   .. container:: header3

     Form Building

   .. icon-box-widget::
     :box-classes: box box-block box-turquoise
     :icon-classes: icon icon-page

     Sample bank account form


.. container:: span6

   .. container:: header3

     Testing

   .. icon-box-widget::
     :box-classes: box box-block box-purple
     :icon-classes: icon icon-page

     :ref:`Test bank account numbers <resources.test_bank_accounts>`

.. clear::

Credit's Status Field
---------------------

Credits have a ``status`` field representing the current status of the credit
through the payout process.

.. dcode:: scenario credit-show
  :section-include: response

There are three possible values for the ``status`` field on a credit:

``pending``
  As soon as the credit is created through the API, the status shows
  as ``pending``. This indicates that Balanced received the information for the
  credit and will begin processing. The ACH network itself processes transactions
  in a batch format. Batch submissions are processed at 3pm PST on business days.
  If the credit is created after 3pm PST, it will not be submitted for processing
  until **3pm PST** the next business day.

``succeded``
  One business day after the batch submission, the status will change to ``succeeded``
  ("Paid" in the dashboard). That is the *expected* status of the credit. If the account number and
  routing number were entered correctly, the money should in fact be available to
  the seller. However, there is no immediate confirmation regarding the
  transaction showing up in the seller's account successfully

``failed``
  The seller's bank has up to three business days from when the money
  *should* be available to indicate a rejection along with the rejection reason.
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
of our :ref:`support channels <overview.support>` and we will attempt to cancel the
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
  :header_class: alert alert-tab
  :body_class: alert alert-gray

  We advise that you transfer a large amount in your Balanced account or you
  may request that Balanced always keep a constant amount in your account for
  you. We're publicly tracking this on `github issue #132`_ and appreciate your input

Transfers may take 2-5 days for the funds to become available; alternatively, you
may fund your account **instantly** with :ref:`Balanced Processing! <processing>`


.. _payouts.cutoff:

Submission & Delivery times
---------------------------

.. container:: table-header

   The cutoff for submitting payouts is **3:00 PM Pacific (PT)** time. Payouts will *not* be
   delivered on weekends or `bank holidays`_:

.. cssclass:: table table-hover

  ==================================== =========== =========== =========== ============ ===========
  Holiday                              2012        2013        2014        2015         2016
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

.. container:: table-header

   Here's some common scenarios for payouts. Remember, the next-day cut off is
   at **3:00 PM Pacific (PT)**.

.. list-table::
   :widths: 20 35 20
   :header-rows: 1
   :class: table table-hover

   * - Type of scenario
     - Example submission date
     - Available when? [*]_
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

.. _sample page: https://gist.github.com/2662770
.. _balanced.js: https://js.balancedpayments.com/v1/balanced.js
.. _testing documentation: /docs/testing#simulating-card-failures
.. _jQuery: http://www.jquery.com
.. _dashboard: https://dashboard.balancedpayments.com/
.. _issues: https://github.com/balanced/balanced-api/issues
.. _bank holidays: http://www.federalreserve.gov/aboutthefed/k8.htm
.. _FedACH directory: https://www.fededirectory.frb.org
.. _github issue #151: https://github.com/balanced/balanced-api/issues/151
.. _github issue #70: https://github.com/balanced/balanced-api/issues/70
.. _github issue #132: https://github.com/balanced/balanced-api/issues/132
