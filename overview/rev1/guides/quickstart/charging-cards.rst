Charging Funding Instruments
==================================


Adding a Card
----------------

.. note::
  :header_class: alert alert-tab-red
  :body_class: alert alert-red
  
  This method is not recommended for production environments. Please use
  balanced.js to create cards.


Let's create a ``Card``.

.. code-block:: ruby

  card = Balanced::Card.new(
    :name => 'John Doe',
    :expiration_month => '12',
    :number => '5105105105105100',
    :expiration_year => '2020',
    :security_code => '123'
  ).save


Charging a Card
----------------

Now that we have a ``Card``, we can charge it. This will issue a debit which
will deduct funds from the target card.

.. code-block:: ruby

  card.debit(
    :amount => 5000,
    :appears_on_statement_as => 'Statement text',
    :description => 'Some descriptive text for the debit in the dashboard'
  )


Charging a Bank Account
------------------------

Now that we have a ``Card``, we can charge it. This will issue a debit which
will deduct funds from the target card.

.. code-block:: ruby

  card.debit(
    :amount => 5000,
    :appears_on_statement_as => 'Statement text',
    :description => 'Some descriptive text for the debit in the dashboard'
  )