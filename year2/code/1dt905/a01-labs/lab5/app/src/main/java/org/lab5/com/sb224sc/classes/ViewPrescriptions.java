package org.lab5.com.sb224sc.classes;

import java.util.List;

@SuppressWarnings("java:S106")
public class ViewPrescriptions {
    private ViewPrescriptions() {
        throw new IllegalStateException("Utility class.");
    }

    /**
     * Prints all the prescriptions in the given list.
     *
     * @param prescriptions the list of prescriptions to be printed
     */
    public static void viewAllPrescriptions(List<Prescriptions> prescriptions) {
        System.out.println("All Prescriptions:\n");

        for (Prescriptions prescription : prescriptions) {
            printPrescription(prescription);
        }
    }

    /**
     * View a prescription by ID.
     *
     * @param prescriptions a list of prescriptions
     * @param id            the ID of the prescription to view
     */
    public static void viewAPrescription(List<Prescriptions> prescriptions, int id) {
        boolean found = false;

        for (Prescriptions prescription : prescriptions) {
            if (prescription.getId() == id) {
                printPrescription(prescription);
                found = true;
                break;
            }
        }

        if (!found) {
            System.out.println("Prescription with ID " + id + " not found.");
        }
    }

    /**
     * Prints the given prescription and adds a new line.
     *
     * @param prescription the prescription to be printed
     */
    private static void printPrescription(Prescriptions prescription) {
        System.out.println(prescription.toString() + "\n");
    }
}
