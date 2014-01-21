Working with Credits
=====================


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

.. .. dcode:: scenario credit-show
  :section-include: response

There are three possible values for the ``status`` field on a credit:

``pending``
  As soon as the credit is created through the API, the status shows
  as ``pending``. This indicates that Balanced received the information for the
  credit and will begin processing. The ACH network itself processes transactions
  in a batch format. Batch submissions are processed at 3pm PST on business days.
  If the credit is created after 3pm PST, it will not be submitted for processing
  until **3pm PST** the next business day.

``succeeded``
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




.. _sample page: https://gist.github.com/2662770
.. _balanced.js: https://js.balancedpayments.com/v1/balanced.js
.. _testing documentation: /docs/testing#simulating-card-failures
.. _jQuery: http://www.jquery.com
.. _dashboard: https://dashboard.balancedpayments.com/
.. _issues: https://github.com/balanced/balanced-api/issues
.. _github issue #151: https://github.com/balanced/balanced-api/issues/151
.. _github issue #70: https://github.com/balanced/balanced-api/issues/70
.. _github issue #132: https://github.com/balanced/balanced-api/issues/132
