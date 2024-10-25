package com.sb224sc.game;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Deck {
    private List<Card> deckOfCards;

    public Deck() {
        generateDeck();
    }

    private void generateDeck() {
        deckOfCards = new ArrayList<>();
        String[] suits = { "Spades", "Hearts", "Clubs", "Diamonds" };
        String[] ranks = { "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace" };

        for (String suit : suits) {
            for (int i = 0; i < ranks.length; i++) {
                int value = i + 2;

                deckOfCards.add(new Card(suit, ranks[i], value));
            }
        }
    }

    public void shuffle() {
        Collections.shuffle(deckOfCards);
    }

    public void printTopAndBottomCard() {
        if (!deckOfCards.isEmpty()) {
            System.out.println("\nTop Card: " + deckOfCards.get(0));
            System.out.println("Bottom Card: " + deckOfCards.get(deckOfCards.size() - 1));
        } else {
            System.out.println("\nDeck is empty.");
        }
    }

    public Card drawCard() {
        if (!deckOfCards.isEmpty()) {
            return deckOfCards.remove(0);
        } else {
            System.out.println("\nDeck is empty.");
            return null;
        }
    }

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

    public int sumOfTwoCards() {
        List<Card> hand = dealPokerHand(2);
        int sum = 0;

        for (Card card : hand) {
            sum += card.getValue();
        }

        return sum;
    }
}
