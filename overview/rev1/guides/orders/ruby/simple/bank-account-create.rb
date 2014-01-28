bank_account = Balanced::BankAccount.create(
  :name => 'Henry Ford',
  :routing_number => '321174851',
  :account_number => '0987654321',
  :type => 'checking'
)

bank_account.associate_to_customer(customer)