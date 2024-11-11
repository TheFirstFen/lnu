package com.onlinefarmacy;

import java.util.Scanner;

public class Menu {
    public static void menu(Scanner scanner, String recDirectory) {
        System.out.println("\n1) View all receipts\n" +
                           "2) View one receipt\n" +
                           "3) Add a new receipt\n" +
                           "4) Change an existing receipt\n" +
                           "5) Remove an existing receipt\n" +
                           "6) Export all recipes as JSON\n" +
                           "7) Export all recipes as CSV\n" +
                           "q) Quit"); 
        System.out.print("Your choice: ");
        String choice = scanner.nextLine();
        if (choice.equalsIgnoreCase("q")) {
            Main.exitprogram = true;
            System.out.println("Exiting the program...");
        } else {
            check_input_choice(choice, scanner, recDirectory);
        }
    }
    public static void check_input_choice(String choice, Scanner scanner, String recDirectory) {
        switch (choice)  {
            case "1":
                ReceiptStorage.printReceipts();
                break;
            case "2":
                ReceiptMenu.showChoices();
                System.out.print("Choice: ");
                String receiptChoice = scanner.nextLine();
                ReceiptMenu.showReceipt(receiptChoice, scanner);
                break;
            case "3":
                CreateReceiptMenu.createReceiptMenu(scanner);
                break;
            case "4":
                ReceiptMenu.showChoices();
                System.out.print("Which one do you want to update? ");
                String updateChoice = scanner.nextLine();
                ReceiptMenu.showReceipt(updateChoice, scanner);
                ReceiptMenu.updateReceipt(updateChoice, scanner);
                break;
            case "5":
                ReceiptMenu.showChoices();
                System.out.print("Which one do you want to delete? ");
                String removeChoice = scanner.nextLine();
                ReceiptMenu.showReceipt(removeChoice, scanner);
                ReceiptMenu.removeReceipt(removeChoice, scanner);
                break;
            case "6":
                ReceiptStorage.exportAllAsJson(recDirectory);
                break;
            case "7":
                ReceiptStorage.exportAllAsCSV(recDirectory);
                break;
            case "q":
                Main.exitprogram = true;
                System.out.println("Exiting the program...");
                break;
            default:
                System.out.print("Incorrect input: ");
                String newChoice = scanner.nextLine();
                check_input_choice(newChoice, scanner, recDirectory);
        }
    }
}
