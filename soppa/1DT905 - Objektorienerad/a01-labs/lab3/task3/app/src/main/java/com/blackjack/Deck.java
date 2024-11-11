package com.blackjack;


import java.util.ArrayList;
import java.util.Collections;
import java.util.List;



public class Deck {
    private static String[] ranks = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"};
    private static String[] suits = {"Hearts", "Diamonds", "Clubs", "Spades"};
    public static List<Card> deck = new ArrayList<>();

    public static void createDeck() {

        for (String suit : suits) {
            for (String rank : ranks) {
                Card card = new Card();
                card.addRank(rank);
                card.addSuit(suit);
                deck.add(card);
            }
        }
    }
    public static void shuffleDeck() {
        Collections.shuffle(deck);
    }


    public static Card getNewCard() {
        Card tempCard = deck.get(0);
        deck.remove(0);
        return tempCard;
    }

    public static Card showNextCard() {
        Card tempCard = deck.get(0);
        return tempCard;
    }


    public static List<Card> twoCardDeal() {
        List<Card> firstDealCards = new ArrayList<>();
        for (int i = 0; i < 3; i++) {
            firstDealCards.add(deck.get(0));
            deck.remove(0);
        }
        return firstDealCards;
    }
}

