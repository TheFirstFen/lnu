package org.lab5.com.sb224sc.classes;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Scanner;

@SuppressWarnings("java:S106")
public class EditPrescriptions {
    private EditPrescriptions() {
        throw new IllegalStateException("Utility class.");
    }

    /**
     * Adds a prescription to the pharmacy.
     *
     * @param sc       a Scanner object used to read user input
     * @param pharmacy a Pharmacy object representing the pharmacy
     */
    public static void addPrescription(Scanner sc, Pharmacy pharmacy) {
        Prescriptions prescriptionToAdd = null;

        System.out.println("Enter drug name: ");
        String drugName = sc.nextLine();
        System.out.println("Enter quantity: ");
        int quantity = sc.nextInt();
        System.out.println("Enter price per package: ");
        double pricePerPackage = sc.nextDouble();
        sc.nextLine();

        int nextPrescriptionId = pharmacy.getNextPrescriptionId();

        DateTimeFormatter timeFormat = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");

        prescriptionToAdd = new Prescriptions(nextPrescriptionId,
                LocalDateTime.now().format(timeFormat), drugName, quantity,
                pricePerPackage);

        pharmacy.addPrescription(prescriptionToAdd);

        System.out.println("Prescription added successfully.\n");
    }

    /**
     * Updates a prescription in the pharmacy.
     *
     * @param sc       the Scanner object to read user input
     * @param pharmacy the Pharmacy object representing the pharmacy
     */
    public static void updatePrescription(Scanner sc, Pharmacy pharmacy) {
        Prescriptions prescriptionToUpdate = null;

        System.out.println("Enter the unique id of the prescription to update: ");
        int idToUpdate = sc.nextInt();
        sc.nextLine();

        for (Prescriptions prescription : pharmacy.prescriptions) {
            if (prescription.getId() == idToUpdate) {
                prescriptionToUpdate = prescription;
                break;
            }
        }

        if (prescriptionToUpdate != null) {
            System.out.println("Enter the new name of the drug: ");
            String drugName = sc.nextLine();
            System.out.println("Enter the new number of packages: ");
            int quantity = sc.nextInt();
            sc.nextLine();
            System.out.println("Enter the new price per package: ");
            double pricePerPackage = sc.nextDouble();
            sc.nextLine();

            prescriptionToUpdate.setDateTime();
            prescriptionToUpdate.setDrugName(drugName);
            prescriptionToUpdate.setQuantity(quantity);
            prescriptionToUpdate.setPricePerPackage(pricePerPackage);
            prescriptionToUpdate.setTotalCost();

            System.out.println("Prescription updated successfully!\n");
        }
    }

    /**
     * Removes a prescription from the pharmacy based on its unique id.
     *
     * @param sc       the Scanner object used to read user input
     * @param pharmacy the Pharmacy object containing the list of prescriptions
     */
    public static void removePrescription(Scanner sc, Pharmacy pharmacy) {
        System.out.println("Enter the unique id of the prescription to remove: ");
        int idToRemove = sc.nextInt();
        sc.nextLine();

        Prescriptions prescriptionToRemove = null;
        for (Prescriptions prescription : pharmacy.prescriptions) {
            if (prescription.getId() == idToRemove) {
                prescriptionToRemove = prescription;
                break;
            }
        }

        if (prescriptionToRemove != null) {
            pharmacy.prescriptions.remove(prescriptionToRemove);
            System.out.println("Prescription removed successfully!\n");
        }
    }
}
