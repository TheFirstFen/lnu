package com.blackjack;

import java.util.Scanner;

public class Menu {
    public static void startMenu(Scanner scanner, playerTurn player, bankirTurn bankir) {
        System.out.println("\n1) Hit (get another card)\n" +
                           "2) Stand (stop with this value)\n" +
                           "3) See the next card(cheating)\n" +
                           "q) Quit");
        System.out.print("Your choice: ");
        String choice = scanner.nextLine();
        if (choice.equalsIgnoreCase("q")) {
            Main.exitprogram = true;
        } else {
            check_input_choice(choice, scanner, player, bankir);
        }
    }

    public static void check_input_choice(String choice, Scanner scanner, playerTurn player, bankirTurn bankir) {
        switch (choice) {
            case "1":
                ((playerTurn) player).addFirstCardToHand();
                ((playerTurn) player).checkIfBust(player, bankir);
                break;
            case "2":
                ((bankirTurn) bankir).bankirLoop(player, bankir);
                break;
            case "3":
                Card card = Deck.showNextCard();
                System.out.println("***\nHere is the next card: " + ((Card) card).getCard() + "\n***");
                break;
            case "q":
                Main.exitprogram = true;
                break;
            default:
                System.out.print("Incorrect input, try again: ");
                String newChoice = scanner.nextLine();
                check_input_choice(newChoice, scanner, player, bankir);
                break;
        }
    }
}
