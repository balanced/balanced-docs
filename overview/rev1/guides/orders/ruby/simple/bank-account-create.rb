bank_account = Balanced::BankAccount.create(
  :name => 'William Henry Cavendish III',
  :routing_number => '321174851',
  :account_number => '0987654321',
  :type => 'checking'
)

bank_account.associate_to_customer(customer)