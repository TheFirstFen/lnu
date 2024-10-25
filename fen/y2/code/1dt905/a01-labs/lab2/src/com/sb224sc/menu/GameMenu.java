package com.sb224sc.menu;

import com.sb224sc.game.*;

import java.util.Scanner;

public class GameMenu {
    public void gameLoop() {
        Deck deck = null;
        Scanner sc = new Scanner(System.in);

        while (true) {
            System.out.println("\n1) Create the deck with all cards \"in order\"");
            System.out.println("2) Shuffle the deck");
            System.out.println("3) Print the first and last card in the deck (without removing them)");
            System.out.println("4) Remove and show one card from the deck");
            System.out.println("5) Deal a 5 card poker hand (remove and show 5 cards from the deck)");
            System.out.println("6) Deal 2 cards and sum the values of the cards (ace is 1 or 14)");
            System.out.println("\nqQ) Exit.");

            System.out.print("\nYour choice: ");

            if (sc.hasNextLine()) {
                String input = sc.nextLine();

                try {
                    if (input.equalsIgnoreCase("q")) {
                        System.out.println("Exiting...");
                        sc.close();
                        System.exit(0);
                    } else if (Integer.parseInt(input) == 1) {
                        deck = new Deck();
                    } else if (deck != null) {
                        if (Integer.parseInt(input) == 2) {
                            deck.shuffle();
                        } else if (Integer.parseInt(input) == 3) {
                            deck.printTopAndBottomCard();
                        } else if (Integer.parseInt(input) == 4) {
                            System.out.println(deck.drawCard());
                        } else if (Integer.parseInt(input) == 5) {
                            System.out.println(deck.dealPokerHand(5));
                        } else if (Integer.parseInt(input) == 6) {
                            System.out.println(deck.sumOfTwoCards());
                        } else {
                            System.out.println("Please input an appropriate value.");
                        }
                    } else {
                        System.out.println("Deck is empty. Please create the deck.");
                    }
                } catch (Exception e) {
                    System.out.println(e);
                }
            } else {
                break;
            }
            
        }
    }
}