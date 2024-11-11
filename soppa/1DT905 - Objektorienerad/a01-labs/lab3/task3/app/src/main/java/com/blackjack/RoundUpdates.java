package com.blackjack;

import java.util.List;

public class RoundUpdates {
    private static Integer currentRound = 0;

    public static void updateGame(playerTurn player, bankirTurn bankir) {
    if (currentRound == 0) {
        Deck.createDeck();
        Deck.shuffleDeck();
        ((playerTurn) player).newHand();
        ((bankirTurn) bankir).newHand();
        System.out.println("Welcome to a game of Black Jack\n" +
        "My name is Kalle and i will be your bankir for today.\n");
        List<Card> firstDealCards = Deck.twoCardDeal();
        ((playerTurn) player).addCardToHand(firstDealCards.get(0));
        ((playerTurn) player).addCardToHand(firstDealCards.get(2));
        ((bankirTurn) bankir).addCardToHand(firstDealCards.get(1));
        System.out.println("The bankirs cards are:");
        printCards(((bankirTurn) bankir).getCards());
        System.out.println("The value of the bankirs cards are:");
        printValues(((bankirTurn) bankir).getValues());
        System.out.println("\nYour cards are:");
        printCards(((playerTurn) player).getCards());
        System.out.println("The value of your cards are:");
        printValues(((playerTurn) player).getValues());
        currentRound += 1;
    } else {
        System.out.println("The bankirs cards are:");
        printCards(((bankirTurn) bankir).getCards());
        System.out.println("The value of the bankirs cards are:");
        printValues(((bankirTurn) bankir).getValues());
        System.out.println("\nYour cards are:");
        printCards(((playerTurn) player).getCards());
        System.out.println("The value of your cards are:");
        printValues(((playerTurn) player).getValues());
        currentRound += 1;
        }
    
    }

    private static void printCards(List<Card> cards) {
        for (Card card : cards){
            System.out.println(((Card) card).getCard());
        }
    }
    private static void printValues(List<Integer> values) {
        for (Integer value : values){
            if (value <= 21) {
                System.out.print(value + " ");
            } else {
                System.out.print("'" + value + "' ");
            }
        }
        System.out.println("");
    }

    public static Integer getRound() {
        return currentRound;
    }
}
