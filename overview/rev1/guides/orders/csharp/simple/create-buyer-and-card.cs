Customer buyer = Customer.new();
customer.name = "Henry Ford";
customer.Save();

Card card = Card.new();
card.number = 5105105105105100;
card.cvv = 123;
card.Save();

card.AssociateToCustomer(buyer);