Disputes
=========

A ``Dispute`` resource represents a chargeback.

.. note::
   :header_class: alert alert-tab
   :body_class: alert alert-green

   -


Fetch a Dispute
-----------------

.. _disputes.show:

Fetches the details of an event that was previously created.

.. container:: code-white

    .. dcode:: scenario dispute_show


List all Disputes
------------------

.. cssclass:: dl-horizontal dl-params

  ``limit``
      *optional* integer. Defaults to ``10``.

  ``offset``
      *optional* integer. Defaults to ``0``.

.. container:: code-white

  .. dcode:: scenario dispute_list