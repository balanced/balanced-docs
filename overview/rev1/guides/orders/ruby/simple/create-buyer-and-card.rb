buyer = Balanced::Customer.new(
  :name => 'John Buyer'
).save

card = Balanced::Card.create(
  :number => '5105105105105100',
  :expiration_month => '12',
  :expiration_year => '2020',
  :cvv => '123'
)

card.associate_to_customer(buyer)