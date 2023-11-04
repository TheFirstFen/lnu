package task3.com.sb224sc.classes;

public class Card {
    private String suit;
    private String rank;
    private int value;

    public Card(String suit, String rank, int value) {
        this.suit = suit;
        this.rank = rank;
        this.value = (rank.equals("Jack") || rank.equals("Queen") || rank.equals("King")) ? 10 : value;
    }

    /**
     * Retrieves the suit of the card.
     *
     * @return the suit of the card.
     */
    public String getSuit() {
        return suit;
    }

    /**
     * Retrieves the rank of the card.
     *
     * @return the rank of the card.
     */
    public String getRank() {
        return rank;
    }

    /**
     * Returns the value of the card based on the rank.
     *
     * @return the value of the card.
     */
    public int getValue() {
        if (rank.equals("Ace")) {
            return 11;
        } else if (rank.equals("King") || rank.equals("Queen") || rank.equals("Jack")) {
            return 10;
        } else {
            return value;
        }
    }

    /**
     * Calculates the value of a card in a card game.
     *
     * @param isAceHigh  a boolean indicating if an ace is considered high.
     * @param totalValue the current total value of the cards.
     * @return the value of the card.
     */
    public int getValue(boolean isAceHigh, int totalValue) {
        if (isAceHigh && rank.equals("Ace") && totalValue + 11 <= 21) {
            return 11;
        } else {
            return 1;
        }
    }

    /**
     * Returns a string representation of the rank and suit of the card.
     *
     * @return a string representation of the rank and suit of the card.
     */
    @Override
    public String toString() {
        return rank + " of " + suit;
    }
}
