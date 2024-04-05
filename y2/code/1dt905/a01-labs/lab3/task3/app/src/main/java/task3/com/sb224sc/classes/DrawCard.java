package task3.com.sb224sc.classes;

public class DrawCard {
    private Deck deck;

    public DrawCard(Deck deck) {
        this.deck = deck;
    }

    /**
     * Draws a card from the deck.
     *
     * @return The drawn card. Returns null if there are no more cards in the deck.
     */
    public Card drawCard() {
        Card card = deck.drawCard();
        if (card != null) {
            System.out.println("\nDrew card: " + card);
        } else {
            System.out.println("No more cards in the deck.");
        }
        return card;
    }

    /**
     * Retrieves the top card from the deck without modifying the deck.
     *
     * @return The top card of the deck.
     */
    public Card cheat() {
        Card card = deck.peekAtTopCard();
        return card;
    }
}
