package com.onlinefarmacy;

import java.util.Scanner;

public class CreateReceiptMenu {
    public static void createReceiptMenu(Scanner scanner) {
        System.out.println("Create a new receipt menu");
        System.out.println("Choose which drug:\n");
        System.out.print("1. Alvedon\n" +
                           "2. Ipren\n" +
                           "3. Desloratadine\n" +
                           "4. Brikanyl\n" + 
                           "5. Morifin\n");
        System.out.print("Your choice: ");
        String choice = scanner.nextLine();
        if (!choice.equalsIgnoreCase("q")) {
            check_input_choice(choice, scanner);
        }
    }
    public static void check_input_choice(String choice, Scanner scanner) {
        switch (choice)  {
            case "1":
                addQuantity(0, scanner);
                break;
            case "2":
                addQuantity(1, scanner);
                break;
            case "3":
                addQuantity(2, scanner);
                break;
            case "4":
                addQuantity(3, scanner);
                break;
            case "5":
                addQuantity(4, scanner);
                break;
            case "q":
                break;
            default:
                System.out.print("Incorrect input: ");
                String newChoice = scanner.nextLine();
                check_input_choice(newChoice, scanner);
        }
    }
    public static void addQuantity(Integer drugIndex, Scanner scanner) {
        System.out.println("Creating a receipt for " + ReceiptHandling.getDrugNameByIndex(drugIndex));
        System.out.print("Choose amount(min 1, max 1000): ");
        String amount = scanner.nextLine();
        try {
            Integer amountInt = Integer.parseInt(amount);
            if (amountInt <= 0 || amountInt > 1000) {
                throw new NumberFormatException();
            } else {
                ReceiptHandling.createReceipt(drugIndex, amountInt);
                System.out.println("Created a recipe for " + amountInt + " " + ReceiptHandling.getDrugNameByIndex(drugIndex));
            }
        } catch (NumberFormatException e) {
            System.out.println("Incorrect input, try again!");
            addQuantity(drugIndex, scanner);
        }
    }
}