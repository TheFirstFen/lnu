package org.lab5.com.sb224sc.classes;

import static org.junit.jupiter.api.Assertions.assertTrue;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.util.ArrayList;
import java.util.List;

import org.junit.jupiter.api.Test;

class ViewPrescriptionsTest {
    @Test
    void testViewAllPrescriptions() {
        List<Prescriptions> prescriptions = new ArrayList<>();
        prescriptions.add(new Prescriptions(1, "2023-09-28 10:00:00", "Drug A", 5, 10.0));
        prescriptions.add(new Prescriptions(2, "2023-09-29 14:30:00", "Drug B", 3, 15.0));

        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outputStream));

        ViewPrescriptions.viewAllPrescriptions(prescriptions);

        System.setOut(System.out);

        assertTrue(outputStream.toString().contains("All Prescriptions:"));
    }

    @Test
    void testViewAPrescription() {
        List<Prescriptions> prescriptions = new ArrayList<>();
        prescriptions.add(new Prescriptions(1, "2023-09-28 10:00:00", "Drug A", 5, 10.0));
        prescriptions.add(new Prescriptions(2, "2023-09-29 14:30:00", "Drug B", 3, 15.0));

        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outputStream));

        ViewPrescriptions.viewAPrescription(prescriptions, 2);

        System.setOut(System.out);

        assertTrue(outputStream.toString().contains("Prescription ID: 2"));
    }

    @Test
    void testViewAPrescriptionWithInvalidID() {
        List<Prescriptions> prescriptions = new ArrayList<>();
        prescriptions.add(new Prescriptions(1, "2023-09-28 10:00:00", "Drug A", 5, 10.0));

        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outputStream));

        ViewPrescriptions.viewAPrescription(prescriptions, 3);

        System.setOut(System.out);

        assertTrue(outputStream.toString().contains("ID 3 not found"));
    }
}
