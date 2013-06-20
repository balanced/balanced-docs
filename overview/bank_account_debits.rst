.. _bank_account_debits:

Debiting Bank Accounts
======================

.. note::
   :class: alert alert-info

   You'll only need to verify a bank account if you're planning to later debit
   that account, which is a functionality only available through our ACH
   Debits private beta. Email support@balancedpayments.com to request access.

Balanced allows you to debit bank accounts via ACH. In order to do this you
must first verify the bank account to ensure that you are authorized to debit
it.

This process of verification is done using micro-deposits. These are test
credits to the specified bank account for random amounts which must be passed
back to Balanced to verify that they were successfully received.

The process of verifying a bank account takes 1-2 business days since Balanced
must send the money to the bank account being verified and it must also show up
on the bank account's statement in order for you to view the amounts sent.

We have complete examples for both the Python and Ruby client libraries:

- `Complete example using Python`_
- `Complete example using Ruby`_

Tutorial
--------

At a high level, we're going to implement the process for verifying and
debiting a bank account. Before you begin, we recommend that you look at how
to `collect bank account information tutorial`_.

Here's how we're going to accomplish this:

- `Create a bank account verification`_
- `Confirm the bank account verification`_
- `Debit the bank account`_

.. note::
   :class: alert alert-info

   To learn how to collect bank account information check out the
   `collect bank account information tutorial`_


Create a bank account verification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Creating a bank account verification is done via the `verify` operation on any
bank account via the client libraries or directly via the HTTP API.

The side effect of creating this resource is to generate two small
(under $1 USD) deposits to the bank account in question. These should appear in
the bank account within 2 business days and need to be reported back as
discussed in the `Confirm the bank account verification`_ section.

- `Create a verification using Python`_
- `Create a verification using Ruby`_
- `Create a verification using PHP`_
- `Create a verification using REST API`_
- `Create a verification using Java`_


Confirm the bank account verification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once you have the two deposit amounts you must update the verification object.
You have 3 attempts to get this right, after the 3rd unsuccessful attempt you
must create a new verification and begin the process over again. If you
successfully confirm the amounts on the verification the bank account is
automatically made available for debiting.

- `Confirm a bank account verification using Python`_
- `Confirm a bank account verification using Ruby`_
- `Confirm a bank account verification using PHP`_
- `Confirm a bank account verification using REST API`_
- `Confirm a bank account verification using Java`_


Debit the bank account
~~~~~~~~~~~~~~~~~~~~~~

Debiting a bank account is exactly the same as charging a card. We have
examples for the various client libraries, if you're directly interacting with
the REST API then simply POST to the `debits_uri` for your marketplace and pass
through the URI of your bank account as the `source_uri` attribute.

- `Debit bank account using Python`_
- `Debit bank account using Ruby`_
- `Debit bank account using PHP`_
- `Debit bank account using REST API`_
- `Debit bank account using Java`_



.. _collect bank account information tutorial: https://docs.balancedpayments.com/overview?language=bash#id2

.. _Create a verification using Python: https://docs.balancedpayments.com/api?language=python#verifying-a-bank-account
.. _Create a verification using Ruby: https://docs.balancedpayments.com/api?language=ruby#verifying-a-bank-account
.. _Create a verification using PHP: https://docs.balancedpayments.com/api?language=php#verifying-a-bank-account
.. _Create a verification using Java: https://docs.balancedpayments.com/api?language=java#verifying-a-bank-account
.. _Create a verification using REST API: https://docs.balancedpayments.com/api?language=bash#verifying-a-bank-account

.. _Debit bank account using Python: https://docs.balancedpayments.com/api?language=python#create-a-new-debit
.. _Debit bank account using Ruby: https://docs.balancedpayments.com/api?language=ruby#create-a-new-debit
.. _Debit bank account using PHP: https://docs.balancedpayments.com/api?language=php#create-a-new-debit
.. _Debit bank account using Java: https://docs.balancedpayments.com/api?language=java#create-a-new-debit
.. _Debit bank account using REST API: https://docs.balancedpayments.com/api?language=bash#create-a-new-debit

.. _Confirm a bank account verification using Python: https://docs.balancedpayments.com/api?language=python#confirm-a-bank-account-verification
.. _Confirm a bank account verification using Ruby: https://docs.balancedpayments.com/api?language=ruby#confirm-a-bank-account-verification
.. _Confirm a bank account verification using PHP: https://docs.balancedpayments.com/api?language=php#confirm-a-bank-account-verification
.. _Confirm a bank account verification using Java: https://docs.balancedpayments.com/api?language=java#confirm-a-bank-account-verification
.. _Confirm a bank account verification using REST API: https://docs.balancedpayments.com/api?language=bash#confirm-a-bank-account-verification

.. _Complete example using Python: https://github.com/balanced/balanced-python/blob/master/examples/bank_account_debits.py
.. _Complete example using Ruby: https://github.com/balanced/balanced-ruby/blob/master/examples/bank_account_debits.rb
