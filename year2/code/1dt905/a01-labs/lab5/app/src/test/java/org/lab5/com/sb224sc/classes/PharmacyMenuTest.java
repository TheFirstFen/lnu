package org.lab5.com.sb224sc.classes;

import static org.junit.jupiter.api.Assertions.assertTrue;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.InputStream;
import java.io.PrintStream;

import org.junit.jupiter.api.Test;

class PharmacyMenuTest {
    @Test
    void testMenuWithValidInput() {
        Pharmacy pharmacy = new Pharmacy("Test Pharmacy", "./path");
        pharmacy.addPrescription(new Prescriptions(1, "2023-09-28 10:00:00", "Medicine A", 5, 10.0));
        pharmacy.addPrescription(new Prescriptions(2, "2023-09-28 11:00:00", "Medicine B", 3, 15.0));

        String simulatedUserInput = "1\n8\n";
        InputStream inputStream = new ByteArrayInputStream(simulatedUserInput.getBytes());
        System.setIn(inputStream);
        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outputStream));

        PharmacyMenu pharmacyMenu = new PharmacyMenu(pharmacy);
        pharmacyMenu.menu();

        String consoleOutput = outputStream.toString();

        assertTrue(consoleOutput.contains("Welcome to Test Pharmacy"));
        assertTrue(consoleOutput.contains("1. View all prescriptions"));
        assertTrue(consoleOutput.contains("8. Quit"));
        assertTrue(consoleOutput.contains("Thanks for visiting Test Pharmacy"));
    }

    @Test
    void testMenuWithInvalidInput() {
        Pharmacy pharmacy = new Pharmacy("Test Pharmacy", "./path");

        String simulatedUserInput = "invalid\n1\n8\n";
        InputStream inputStream = new ByteArrayInputStream(simulatedUserInput.getBytes());
        System.setIn(inputStream);
        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outputStream));

        PharmacyMenu pharmacyMenu = new PharmacyMenu(pharmacy);
        pharmacyMenu.menu();

        String consoleOutput = outputStream.toString();

        assertTrue(consoleOutput.contains("Welcome to Test Pharmacy"));
        assertTrue(consoleOutput.contains("Invalid input"));
        assertTrue(consoleOutput.contains("Thanks for visiting Test Pharmacy"));
    }

    @Test
    void testMenuConstructorWithValidInput() {
        Pharmacy pharmacy = new Pharmacy("Test Pharmacy", "./path");
        pharmacy.addPrescription(new Prescriptions(1, "2023-09-28 10:00:00", "Medicine A", 5, 10.0));
        pharmacy.addPrescription(new Prescriptions(2, "2023-09-28 11:00:00", "Medicine B", 3, 15.0));

        String simulatedUserInput = "2\n-1\n1\n8\n";
        InputStream inputStream = new ByteArrayInputStream(simulatedUserInput.getBytes());
        System.setIn(inputStream);
        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outputStream));

        PharmacyMenu pharmacyMenu = new PharmacyMenu(pharmacy.pharmacyName, "./path", "./json", "./csv");
        pharmacyMenu.menu();

        String consoleOutput = outputStream.toString();

        assertTrue(consoleOutput.contains("Welcome to Test Pharmacy"));
        assertTrue(consoleOutput.contains("prescription ID"));
        assertTrue(consoleOutput.contains("8. Quit"));
        assertTrue(consoleOutput.contains("Thanks for visiting Test Pharmacy"));
    }

    @Test
    void testUpdateRemovePrescription() {
        Pharmacy pharmacy = new Pharmacy("Test Pharmacy", "./path");

        String simulatedUserInput = "3\ntest\n1\n10.99\n4\n0\ntest1\n7\n8.99\n5\n0\n8\n";
        InputStream inputStream = new ByteArrayInputStream(simulatedUserInput.getBytes());
        System.setIn(inputStream);
        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outputStream));

        PharmacyMenu pharmacyMenu = new PharmacyMenu(pharmacy);
        pharmacyMenu.menu();

        String consoleOutput = outputStream.toString();

        assertTrue(consoleOutput.contains("Welcome to Test Pharmacy"));
        assertTrue(consoleOutput.contains("updated successfully"));
        assertTrue(consoleOutput.contains("removed successfully"));
        assertTrue(consoleOutput.contains("8. Quit"));
        assertTrue(consoleOutput.contains("Thanks for visiting Test Pharmacy"));
    }

    @Test
    void testExport() {
        Pharmacy pharmacy = new Pharmacy("Test Pharmacy", "./data/test/");

        String simulatedUserInput = "3\ntest\n1\n10.99\n6\n7\n8\n";
        InputStream inputStream = new ByteArrayInputStream(simulatedUserInput.getBytes());
        System.setIn(inputStream);
        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outputStream));

        PharmacyMenu pharmacyMenu = new PharmacyMenu(pharmacy);
        pharmacyMenu.menu();

        String consoleOutput = outputStream.toString();

        assertTrue(consoleOutput.contains("Welcome to Test Pharmacy"));
        assertTrue(consoleOutput.contains("Enter quantity"));
        assertTrue(consoleOutput.contains("JSON successfully"));
        assertTrue(consoleOutput.contains("CSV successfully"));
        assertTrue(consoleOutput.contains("8. Quit"));
        assertTrue(consoleOutput.contains("Thanks for visiting Test Pharmacy"));
    }
}
