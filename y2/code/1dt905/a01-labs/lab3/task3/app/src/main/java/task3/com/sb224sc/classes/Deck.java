package task3.com.sb224sc.classes;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Deck {
    private List<Card> deckOfCards;

    public Deck() {
        generateDeck();
    }

    /**
     * Returns the remaining amount of cards in the deck.
     *
     * @return the remaining amount of cards in the deck.
     */
    public int getRemainingAmountOfCards() {
        return deckOfCards.size();
    }

    /**
     * Generates a deck of cards.
     *
     */
    private void generateDeck() {
        deckOfCards = new ArrayList<>();
        String[] suits = { "Spades", "Hearts", "Clubs", "Diamonds" };
        String[] ranks = { "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace" };

        for (String suit : suits) {
            for (int i = 0; i < ranks.length; i++) {
                int value = i + 2;
                if (ranks[i].equals("Ace")) {
                    value = 11;
                }

                deckOfCards.add(new Card(suit, ranks[i], value));
            }
        }
    }

    /**
     * Shuffles the deck of cards.
     *
     */
    public void shuffle() {
        Collections.shuffle(deckOfCards);
    }

    /**
     * Prints the top and bottom card of the deck.
     *
     */
    public void printTopAndBottomCard() {
        if (!deckOfCards.isEmpty()) {
            System.out.println("\nTop Card: " + deckOfCards.get(0));
            System.out.println("Bottom Card: " + deckOfCards.get(deckOfCards.size() - 1));
        } else {
            System.out.println("\nDeck is empty.");
        }
    }

    /**
     * Retrieves a card from the deck.
     *
     * @return The card drawn from the deck, or null if the deck is empty.
     */
    public Card drawCard() {
        if (!deckOfCards.isEmpty()) {
            Card card = deckOfCards.remove(0);
            return card;
        } else {
            System.out.println("\nDeck is empty.");
            return null;
        }
    }

    /**
     * Generates a poker hand by dealing a specified amount of cards.
     *
     * @param amountCards the number of cards to be dealt.
     * @return the list of cards representing the poker hand.
     */
    public List<Card> dealPokerHand(int amountCards) {
        List<Card> hand = new ArrayList<>();

        for (int i = 0; i < amountCards; i++) {
            Card card = drawCard();
            if (card != null) {
                hand.add(card);
            }
        }

        return hand;
    }

    /**
     * Calculates the sum of the values of two cards.
     *
     * @return the sum of the values of the two cards.
     */
    public int sumOfTwoCards() {
        List<Card> hand = dealPokerHand(2);
        int sum = 0;

        for (Card card : hand) {
            sum += card.getValue();
        }

        return sum;
    }

    /**
     * Returns the top card from the deck without removing it.
     *
     * @return the top card from the deck, or null if the deck is empty.
     */
    public Card peekAtTopCard() {
        if (!deckOfCards.isEmpty()) {
            return deckOfCards.get(0);
        } else {
            System.out.println("\nDeck is empty.");
            return null;
        }
    }
}
