package task3;

import java.util.List;
import java.util.Scanner;

import task3.com.task3.helpers.Deck;

public class Main {
    private static Boolean Deckcreated = false;
    private static Boolean exitprogram = false;
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("\n1) Create the deck with all the cards 'in order'\n" +
                               "2) Shuffle the deck\n" +
                               "3) Print the first and last card in the deck (without removing them)\n" +
                               "4) Remove and show one card of the deck\n" +
                               "5) Deal a 5 card poker hand (remove and show 5 cards from the deck)\n" +
                               "6) Deal 2 cards and sum the values of the cards (ace is 1 or 14)\n" +
                               "q) Quit");
            System.out.print("Your choice: ");
            String choice = scanner.nextLine();
            if (choice.equalsIgnoreCase("q")) {
                System.out.println("Exiting the program...");
                break;
            } else {
                // Check if deck is created
                if (choice.equals("1" )) {
                    check_input_choice(choice, scanner);
                } else if (Deckcreated) {
                    check_input_choice(choice, scanner);
                } else {
                    check_input_choice("NoDeckCreated", scanner);
                }

            }
            if (exitprogram) {
                System.out.println("Exiting the program...");
                break;
            }
        }
        scanner.close();
    }
    public static void check_input_choice(String choice, Scanner scanner) {
        if (choice.equals("1") && Deckcreated.equals(false)) {
            Deck.createDeck();
            Deckcreated = true;
            System.out.println("-----------------------------------------------");
            System.out.println("Ordered deck created!");
            System.out.println("-----------------------------------------------");
        } else if (choice.equals("2")) {
            System.out.println("-----------------------------------------------");
            System.out.println("Deck shuffled!");
            System.out.println("-----------------------------------------------");
            Deck.shuffleDeck();
        } else if (choice.equalsIgnoreCase("3")) {
            System.out.println("-----------------------------------------------");
            System.out.println("First card: " + Deck.getFirst());
            System.out.println("Last card: " + Deck.getLast());
            System.out.println("-----------------------------------------------");
        } else if (choice.equalsIgnoreCase("4")) {
            System.out.println(Deck.removeAndShow() + " was removed!");
        } else if (choice.equalsIgnoreCase("5")) {
            System.out.println("-----------------------------------------------");
            System.out.println("Your poker hand:");
            for (String card : Deck.givePokerHand()) {
                System.out.println(card);
            };
            System.out.println("-----------------------------------------------");
        } else if (choice.equalsIgnoreCase("6")) {
            List<Integer> handValue = Deck.twoCardDeal();
            if (handValue.size() == 1) {
                System.out.println("Value of your hand is " + handValue.get(0));
            } else if (handValue.size() == 2) {
                System.out.println("Value of your hand is " + handValue.get(0));
                System.out.println("or " + handValue.get(1));
            } else {
                System.out.println("Value of your hand is " + handValue.get(0));
                System.out.println(", " + handValue.get(1));
                System.out.println("or " + handValue.get(2));
            }
        } else if (choice.equalsIgnoreCase("NoDeckCreated")) {
            System.out.println("-----------------------------------------------");
            System.out.println("No deck has been created, do that first: ");
            
        } else if (choice.equalsIgnoreCase("q")) {
            exitprogram = true;
        } else {
            System.out.println("-----------------------------------------------");
            System.out.println("Incorrect input, try again: ");
            String Newchoice = scanner.nextLine();
            check_input_choice(Newchoice, scanner);
        }
    }
}
