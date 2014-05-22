// cardHref is the stored href for the card
CardHold cardHold = new CardHold(cardHref);

try {
    cardHold.unstore();
}
catch (HTTPError e) {}
catch (NotCreated notCreated) {}