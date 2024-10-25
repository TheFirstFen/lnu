package lab5;

import java.io.*;
import java.util.*;

import com.google.gson.Gson;

import lab5.com.drugs.Pharmacy;
import lab5.com.drugs.PharmacyConfig;
import lab5.com.drugs.Receipt;
 

public class Menu {
    public void menuLoop() {
        try {
            Gson gson = new Gson();
            //String configPath = ".." + File.separator + "app" + File.separator + "config" + File.separator + "config.json";
            BufferedReader reader = new BufferedReader(new FileReader("..\\app\\config\\config.json"));
            PharmacyConfig config = gson.fromJson(reader, PharmacyConfig.class);
            reader.close();

            Pharmacy pharmacy = new Pharmacy(config.getName(), config.getReceiptDirectory());

            pharmacy.loadReceiptsFromJSON("..\\app\\receipts\\receipts.json");

            Scanner scanner = new Scanner(System.in);
            while(true) {

                System.out.println("Welcome to eu222dq's Online Farmacy - menu");

                System.out.println("1. View all receipts");
                System.out.println("2. view a receipt");
                System.out.println("3. Add a new receipt");
                System.out.println("4. Uppdate/ change a receipt");
                System.out.println("5. Remove a receipt");
                System.out.println("6. Export all receipts as JSON");
                System.out.println("7. Export all receipts as CSV");
                System.out.println("8. Quit");

                System.out.print("Enter you choice: ");
                int choice = scanner.nextInt();
                scanner.nextLine();

                switch (choice) {
                case 1:
                    displayAllReceipts(pharmacy);
                    break;
                case 2:
                    viewReceipt(pharmacy, scanner);
                    break;
                case 3:
                    addReceipt(pharmacy, scanner);
                    break;
                case 4:
                    updateReceipt(pharmacy, scanner);
                    break;
                case 5:
                    removeReceipt(pharmacy, scanner);
                    break;
                case 6:
                    pharmacy.exportAllReceiptsAsJSON();
                    break;
                case 7:
                    pharmacy.exportAllReceiptsAsCVS();
                    break;
                case 8:
                    System.out.println(" Thank you for using Online Farmacy. Goodbye!");
                    System.out.println("Would you like to save the receipts to the next time? (y/n) (Defualt yes)");
                    String yesNo = scanner.nextLine();
                    
                    if (yesNo.equals("n")) {
                        scanner.close();
                        System.exit(0);
                    }
                    else{
                        pharmacy.exportAllReceiptsAsJSON();
                        pharmacy.exportAllReceiptsAsCVS();
                        scanner.close();
                        System.exit(0);
                    }

                default:
                    System.out.println("Wrong input, Try again");
                }
            }
        }catch (IOException e) {
            System.out.println("Error loading configuration: " + e.getMessage());
        }
    }
    private static void displayAllReceipts(Pharmacy pharmacy) {
        List<Receipt> receipts = pharmacy.getAllReceipts();
        if (receipts.isEmpty()) {
            System.out.println("No receipts found.");
        }
        else {
            System.out.println("All Receipts:");
            System.out.println("ID\tDate\t\t\t\tDrug Name\tPackages\tPrice Per Package\tTotal Cost");
            for (Receipt receipt : receipts) {
                System.out.printf("%d\t%s\t%s\t\t%d\t\t%.2f\t\t\t%.2f%n",
                        receipt.getId(),
                        receipt.getDate(),
                        receipt.getDrugName(),
                        receipt.getNumPackages(),
                        receipt.getPricePerPackage(),
                        receipt.getTotalCost());
            }
        }
    }

    private static void viewReceipt(Pharmacy pharmacy, Scanner scanner) {
        System.out.print("Enter the ID of the receipt you want to view: ");
        int receiptId = scanner.nextInt();
        scanner.nextLine();

        Receipt receipt = pharmacy.getReceipt(receiptId);

        if (receipt == null) {
            System.out.println("Receipt with ID " + receiptId + " not found.");
        }
        else {
            System.out.println("");
            System.out.println("Receipt Details:");
            System.out.println("ID: " + receipt.getId());
            System.out.println("Date and Time: " + receipt.getDate());
            System.out.println("Drug Name: " + receipt.getDrugName());
            System.out.println("Number of Packages: " + receipt.getNumPackages());
            System.out.println("Price Per Package: " + receipt.getPricePerPackage());
            System.out.println("Total Cost: " + receipt.getTotalCost());
            System.out.println("");
        }

    }

    private static void addReceipt(Pharmacy pharmacy, Scanner scanner){
        System.out.println("Enter Receipt Details:");

        Date currentDate = new Date();

        System.out.print("Drug Name: ");
        String drugName = scanner.nextLine();

        System.out.print("Number of Packages: ");
        int numPackages = scanner.nextInt();
        scanner.nextLine();

        System.out.print("Price Per Package: ");
        double pricePerPackage = scanner.nextDouble();
        scanner.nextLine();

        Receipt newReceipt = new Receipt(0, currentDate, drugName, numPackages, pricePerPackage);

        pharmacy.addReceipt(newReceipt);
        System.out.println("Receipt added successfully.");
    }

    private static void updateReceipt(Pharmacy pharmacy, Scanner scanner) {
        System.out.print("Enter the ID of the receipt you want to update: ");
        int receiptId = scanner.nextInt();
        scanner.nextLine();

        Receipt existingReceipt = pharmacy.getReceipt(receiptId);
        if (existingReceipt == null) {
            System.out.println("Receipt with ID " + receiptId + " not found.");
        } else {
            System.out.println("Updating Receipt with ID " + receiptId);

            System.out.print("New Drug Name: ");
            String newDrugName = scanner.nextLine();

            Date newDate = new Date();

            System.out.print("New Number of Packages: ");
            int newNumPackages = scanner.nextInt();
            scanner.nextLine();

            System.out.print("New Price Per Package: ");
            double newPricePerPackage = scanner.nextDouble();
            scanner.nextLine();

            existingReceipt.setDate(newDate);
            existingReceipt.setDrugName(newDrugName);
            existingReceipt.setNumPackages(newNumPackages);
            existingReceipt.setPricePerPackage(newPricePerPackage);

            pharmacy.uppdateReceipt(existingReceipt);
            System.out.println("Receipt with ID " + receiptId + " updated successfully.");
        }
    }

    private static void removeReceipt(Pharmacy pharmacy, Scanner scanner) {
        System.out.print("Enter the ID of the receipt you want to remove: ");
        int receiptId = scanner.nextInt();
        scanner.nextLine();

        pharmacy.removeReceipt(receiptId);
        System.out.println("Receipt with ID " + receiptId + " removed successfully");
    }
}
