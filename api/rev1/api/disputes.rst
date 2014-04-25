Disputes
=========

A ``Dispute`` resource represents a customer-disputed charge made on their
credit card, also known as a chargeback.

Disputes have a ``status`` attribute representing the current status of the
dispute and may be one of:

.. cssclass:: dl-horizontal dl-params dl-param-values dd-noindent dd-marginbottom

  ``pending``
      The initial status of the dispute. The dispute is pending a challenge
      with documentation of transaction fulfillment.
  ``won``
    The card processor has ruled in favor of the marketplace that the transaction
    was legitimate.
  ``lost``
    The card processor has ruled in favor of the customer that the transaction
    was not fulfilled or otherwise not legitimate.


Fetch a Dispute
-----------------

.. _disputes.show:

Fetches the details of an event that was previously created.

.. container:: code-white

  .. dcode:: scenario dispute_show


List All Disputes
------------------

.. cssclass:: dl-horizontal dl-params

  ``limit``
      *optional* integer. Defaults to ``10``.

  ``offset``
      *optional* integer. Defaults to ``0``.

.. container:: code-white

  .. dcode:: scenario dispute_list