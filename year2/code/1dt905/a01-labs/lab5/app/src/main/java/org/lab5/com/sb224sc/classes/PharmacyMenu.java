package org.lab5.com.sb224sc.classes;

import java.util.Scanner;

@SuppressWarnings("java:S106")
public class PharmacyMenu {
    private boolean quit = false;
    protected Pharmacy pharmacy;
    private String jsonPath;
    private String csvPath;

    public PharmacyMenu(String pharmacyName, String loadPath, String jsonPath, String csvPath) {
        this.pharmacy = new Pharmacy(pharmacyName, loadPath);
        this.jsonPath = jsonPath;
        this.csvPath = csvPath;
    }

    public PharmacyMenu(Pharmacy pharmacy) {
        this.pharmacy = pharmacy;
    }

    /**
     * Executes the menu loop of the program.
     */
    public void menu() {
        Scanner sc = new Scanner(System.in);

        while (!quit) {
            try {
                menuLoop(sc);
            } catch (Exception e) {
                System.out.println(e.toString());
            }
        }

        sc.close();
    }

    /**
     * A description of the entire Java function.
     *
     * @param sc the Scanner object used for user input
     */
    private void menuLoop(Scanner sc) {
        System.out.println("Welcome to " + pharmacy.pharmacyName + ":\n");
        menuOptions();
        String choice = sc.nextLine();
        if (handleInput(choice, sc).equals("8")) {
            quit = true;
            System.out.println("Thanks for visiting " + pharmacy.pharmacyName);
        }
    }

    /**
     * Prints the menu options for the prescription management system.
     *
     * @param None This function does not take any parameters.
     */
    private void menuOptions() {
        System.out.println("1. View all prescriptions");
        System.out.println("2. View a prescription");
        System.out.println("3. Add a new prescription");
        System.out.println("4. Update/change a prescription");
        System.out.println("5. Remove a prescription");
        System.out.println("6. Export all prescriptions as JSON");
        System.out.println("7. Export all prescriptions as CSV");
        System.out.println("8. Quit");
    }

    /**
     * Handles the input choice and performs the corresponding action.
     *
     * @param choice the user's input choice
     * @param sc     the Scanner object for user input
     * @return the user's input choice
     */
    public String handleInput(String choice, Scanner sc) {
        switch (choice) {
            case "1":
                ViewPrescriptions.viewAllPrescriptions(pharmacy.prescriptions);
                break;
            case "2":
                int idToFind = -1;
                do {
                    System.out.println("Enter prescription ID you are looking for: ");
                    idToFind = sc.nextInt();
                    sc.nextLine();
                } while (idToFind == -1);
                ViewPrescriptions.viewAPrescription(pharmacy.prescriptions, idToFind);
                break;
            case "3":
                EditPrescriptions.addPrescription(sc, pharmacy);
                break;
            case "4":
                EditPrescriptions.updatePrescription(sc, pharmacy);
                break;
            case "5":
                EditPrescriptions.removePrescription(sc, pharmacy);
                break;
            case "6":
                ExportPrescriptions.exportPrescriptionsAsJSON(pharmacy.prescriptions, jsonPath);
                break;
            case "7":
                ExportPrescriptions.exportPrescriptionsAsCSV(pharmacy.prescriptions, csvPath);
                break;
            case "8":
                System.out.println("Exiting application...");
                break;
            default:
                System.out.println("Invalid input");
                break;
        }
        return choice;
    }
}
