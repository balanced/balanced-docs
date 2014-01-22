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

Credits have a ``status`` attribute representing the current status of the credit
throughout the payout process. There are three possible ``status`` values:

.. cssclass:: dd-noindent dd-marginbottom

  ``pending``
    As soon as the credit is created through the API, the status shows
    as ``pending``. This indicates that Balanced received the information for the
    credit and will begin processing. The ACH network itself processes transactions
    in a batch format. Batch submissions are processed at 3pm PST on business days.
    If the credit is created after 3pm PST, it will not be submitted for processing
    until **3pm PST** the next business day.
  ``succeeded``
    One business day after the batch submission, the status will change to
    ``succeeded``. That is the *expected* status of the credit. If the account
    number and routing number were entered correctly, the money should in fact
    be available to the seller. However, there is no immediate confirmation
    regarding the transaction showing up in the seller's account successfully.
  ``failed``
    The seller's bank has up to three business days from when the money *should*
    be available to indicate a rejection along with the rejection reason.
    Unfortunately, not all banks comply with ACH network policies and may respond
    after three business days with a rejection. As soon as Balanced receives the
    rejection, the status is updated to ``failed``.


Payout Methods
--------------

Currently Balanced only supports payouts to bank accounts via ACH but we will
add more. All of this is publicly tracked via Github issues. For example:

* `Payouts via Check <https://github.com/balanced/balanced-api/issues/69>`_
* `Pushing to Cards <https://github.com/balanced/balanced-api/issues/32>`_

Feel free to chime in on an existing issue or create a new one if you'd like
to see another payment method supported.


Pre-funding Escrow
------------------------

Any payout issued requires maintaining sufficient money in your Balanced escrow.

If you do not have a sufficient balance, Balanced will return a ``409`` http
status code, stating that you do not have sufficient funds to cover your
desired ACH operation. You will have to add funds to your marketplace escrow
from a credit card or bank account attached to your marketplace. This may be
done via the API or via the Balanced `dashboard`_. To do this via the API:


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
