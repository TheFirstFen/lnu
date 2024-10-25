import java.util.ArrayList;
import java.util.Collections;
import java.util.List;


public class CardDeckApp {
    public static void main(String[] args) {
        Deck deck = new Deck();
        System.out.println("All cards in order \n" + deck.getAllCards() + "\n");
        deck.shuffle();
        System.out.println("The cards are shuffled \n" + deck.getAllCards() + "\n");

        System.out.println("\nFirst card in the deck: " + deck.getFirstCard());
        
        System.out.println("Last card in the deck: " + deck.getLastCard());
        


        System.out.println("Removing and showing one card from the deck: " + deck.dealOneCard() + "\n");

        List<Card> pokerHand = deck.dealPokerHand(5);
        System.out.println("Dealing a 5 card poker hand:");
        for (Card card : pokerHand) {
            System.out.println(card);
        }

        int sumOfTwoCards = deck.dealAndSumTwoCards();
        System.out.println("\nDealing 2 cards and summing their values: " + sumOfTwoCards);

        System.out.println("Remaining cards in the deck: " + deck.getRemainingCardsCount() + "\n");
    }
}


class Card {
    private final String suit;
    private final String rank;
    private final int value;

    public Card(String suit, String rank, int value) {
        this.suit = suit;
        this.rank = rank;
        this.value = value;
    }

    public String getSuit() {
        return suit;
    }

    public String getRank() {
        return rank;
    }

    public int getValue() {
        return value;
    }

    @Override
    public String toString() {
        return rank + " of " + suit;
    }
}

class Deck {
    private final List<Card> cards;

    public Deck() {
        cards = new ArrayList<>();
        initializeDeck();
    }

    private void initializeDeck() {
        String[] suits = {"Hearts", "Diamonds", "Clubs", "Spades"};
        String[] ranks = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"};

        for (String suit : suits) {
            for (int i = 0; i < ranks.length; i++) {
                int value = i + 2;
                if (i >= 10) {
                    value = 10;
                }
                if (i == 12) {
                    value = 1;
                }

                cards.add(new Card(suit, ranks[i], value));
            }
        }
    }


    public void shuffle() {
        Collections.shuffle(cards);
    }

    public Card getFirstCard() {
        return cards.get(0);
    }

    public Card getLastCard() {
        return cards.get(cards.size() - 1);
    }

    public List<Card> getAllCards() {
        return cards;
    }

    public Card dealOneCard() {
        if (cards.isEmpty()) {
            System.out.println("The deck is empty.");
            return null;
        }
        return cards.remove(0);
    }

    public List<Card> dealPokerHand(int numCards) {
        List<Card> hand = new ArrayList<>();
        for (int i = 0; i < numCards; i++) {
            Card card = dealOneCard();
            if (card != null) {
                hand.add(card);
            }
        }
        return hand;
    }

    public int dealAndSumTwoCards() {
        List<Card> hand = dealPokerHand(2);
        int sum = 0;
        for (Card card : hand) {
            sum += card.getValue();
        }
        return sum;
    }

    public int getRemainingCardsCount() {
        return cards.size();
    }
}