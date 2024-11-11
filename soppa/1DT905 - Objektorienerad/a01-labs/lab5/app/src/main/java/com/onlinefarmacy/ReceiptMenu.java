package com.onlinefarmacy;

import java.util.Scanner;

public class ReceiptMenu {
    public static void showChoices() {
        System.out.println("Choose which recipe to view!\n");
        Integer i = 1;
        for (Receipt receipt : ReceiptStorage.getStoredReceipts()) {
            System.out.println(i + ": " + receipt.getDateTime() + ", " + 
                               receipt.getUniqueId() + ", " + receipt.getDrugName());
            i ++;
        }
    }

    public static void showReceipt(String choice, Scanner scanner) {
        if (!choice.equalsIgnoreCase("q")) {
            try {
                Integer intChoice = Integer.parseInt(choice);
                if (intChoice <= ReceiptStorage.getStoredReceipts().size() && intChoice > 0) {
                    Receipt receiptToShow = ReceiptStorage.getStoredReceipts().get(intChoice - 1);
                    System.out.println(receiptToShow.toJson());
                } else {
                    throw new NumberFormatException();
                }
            } catch (NumberFormatException e) {
                System.out.print("Incorrect input, try again: ");
                String newChoice = scanner.nextLine();
                showReceipt(newChoice, scanner);
            }            
        }
    }
    public static void removeReceipt(String removeChoice, Scanner scanner) {
        System.out.println("Are you sure you want to delete this one(y/n)? ");
        String yesOrNo = scanner.nextLine();
        incorrectInputRemove(yesOrNo, scanner, removeChoice);
    }
    public static void incorrectInputRemove(String yesOrNo, Scanner scanner, String removeChoice) {
        if (yesOrNo.equalsIgnoreCase("y")) {
            Integer intRemoveChoice = Integer.parseInt(removeChoice);
            ReceiptStorage.removeReceipt(intRemoveChoice - 1);
            System.out.println("Receipt was removed!");
        } else if (!yesOrNo.equalsIgnoreCase("n")) {
            System.out.println("Incorrect input, try again: ");
            String newYesOrNo = scanner.nextLine();
            incorrectInputRemove(newYesOrNo, scanner, removeChoice);
        } 
    }
    public static void updateReceipt(String updateChoice, Scanner scanner) {
        System.out.println("What do you want to change?\n" +
                           "1. Drug\n" + 
                           "2. Quantity\n");
        System.out.print("Your choice: ");
        String quantOrDrug = scanner.nextLine();
        incorrectInputUpdate(quantOrDrug, scanner, updateChoice);
    }
    public static void incorrectInputUpdate(String quantOrDrug, Scanner scanner, String updateChoice) {
        if (quantOrDrug.equals("1")) {

            Integer intUpdateChoice = Integer.parseInt(updateChoice);
            Integer drugIndex = getDrug(scanner);
            String newDrug = ReceiptHandling.getDrugNameByIndex(0);
            ReceiptStorage.updateDrug(intUpdateChoice - 1, newDrug, drugIndex);
            System.out.println("Receipt was updated!");
        } else if (quantOrDrug.equals("2")) {
            Integer intUpdateChoice = Integer.parseInt(updateChoice);
            Integer newAmount = getAmount(scanner);
            ReceiptStorage.updateQuantity(intUpdateChoice - 1, newAmount);
            System.out.println("Receipt was updated!");
        } else if (!quantOrDrug.equalsIgnoreCase("q")) {
            System.out.println("Incorrect input, try again: ");
            String newYesOrNo = scanner.nextLine();
            incorrectInputUpdate(newYesOrNo, scanner, updateChoice);
        }
    }
    public static Integer getAmount(Scanner scanner) {
        Integer intQuantity = 0;
        while (true) {
            System.out.print("Choose a new quantity: ");
            String newQuantity = scanner.nextLine();
            try {
                intQuantity = Integer.parseInt(newQuantity);
                if (intQuantity <= 0 || intQuantity > 1000) {
                    throw new NumberFormatException();
                } else {
                    break;
                }
            } catch (NumberFormatException e) {
                System.out.println("Incorrect input try again!");
            }
        }
        return intQuantity;
    }

    public static Integer getDrug(Scanner scanner) {
        System.out.println("Choose which drug to change to:\n");
        System.out.print("1. Alvedon\n" +
                           "2. Ipren\n" +
                           "3. Desloratadine\n" +
                           "4. Brikanyl\n" + 
                           "5. Morifin\n");
        System.out.print("Your choice: ");
        String choice = scanner.nextLine();
        return check_input_choice_drug(choice, scanner);

    }
    public static Integer check_input_choice_drug(String choice, Scanner scanner) {
        switch (choice)  {
            case "1":
                return 0;
            case "2":
                return 1;
            case "3":
                return 2;
            case "4":
                return 3;
            case "5":
                return 4;
            default:
                System.out.print("Incorrect input: ");
                String newChoice = scanner.nextLine();
                return check_input_choice_drug(newChoice, scanner);
        }
    }
}
