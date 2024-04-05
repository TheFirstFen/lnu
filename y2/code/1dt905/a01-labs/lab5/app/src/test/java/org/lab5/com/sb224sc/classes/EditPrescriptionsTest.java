package org.lab5.com.sb224sc.classes;

import static org.junit.jupiter.api.Assertions.*;

import java.util.Scanner;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class EditPrescriptionsTest {
    private Pharmacy pharmacy;

    @BeforeEach
    void setUp() {
        pharmacy = new Pharmacy("Test Pharmacy", "./config/");
    }

    @Test
    void testAddPrescription() {
        EditPrescriptions.addPrescription(new Scanner("Test Drug\n10\n5.0\n"), pharmacy);

        assertEquals(1, pharmacy.getPrescriptionsList().size());
        assertNotNull(pharmacy.getPrescriptionsList().get(0));
    }

    @Test
    void testUpdatePrescription() {
        Prescriptions existingPrescription = new Prescriptions(1, "2023-09-28 10:00:00", "Existing Drug", 5, 8.0);
        pharmacy.addPrescription(existingPrescription);

        Scanner sc = new Scanner("1\nNew Drug\n10\n7.5\n");

        EditPrescriptions.updatePrescription(sc, pharmacy);

        assertEquals("New Drug", existingPrescription.getDrugName());
        assertEquals(10, existingPrescription.getQuantity());
        assertEquals(7.5, existingPrescription.getPricePerPackage(), 0.001); // Use delta for double comparison
    }

    @Test
    void testUpdatePrescriptionWithEmptyList() {
        Scanner sc = new Scanner("1\n");

        EditPrescriptions.updatePrescription(sc, pharmacy);

        assertTrue(pharmacy.prescriptions.isEmpty());
    }

    @Test
    void testUpdatePrescriptionWithToUpdateNull() {
        Prescriptions existingPrescription = new Prescriptions(1, "2023-09-28 10:00:00", "Existing Drug", 5, 8.0);
        pharmacy.addPrescription(existingPrescription);

        Scanner sc = new Scanner("3\n");

        EditPrescriptions.updatePrescription(sc, pharmacy);

        assertNotNull(pharmacy.prescriptions.get(0));
    }

    @Test
    void testRemovePrescription() {
        Prescriptions prescriptionToRemove = new Prescriptions(1, "2023-09-28 10:00:00", "Remove Drug", 5, 8.0);
        pharmacy.addPrescription(prescriptionToRemove);

        Scanner sc = new Scanner("1\n");

        EditPrescriptions.removePrescription(sc, pharmacy);

        assertEquals(0, pharmacy.getPrescriptionsList().size());
    }

    @Test
    void testRemovePrescriptionWithEmptyList() {
        Scanner sc = new Scanner("1\n");

        EditPrescriptions.removePrescription(sc, pharmacy);

        assertTrue(pharmacy.prescriptions.isEmpty());
    }

    @Test
    void testRemovePrescriptionWithToRemoveNull() {
        Prescriptions existingPrescription = new Prescriptions(1, "2023-09-28 10:00:00", "Existing Drug", 5, 8.0);
        pharmacy.addPrescription(existingPrescription);

        Scanner sc = new Scanner("3\n");

        EditPrescriptions.removePrescription(sc, pharmacy);

        assertNotNull(pharmacy.prescriptions.get(0));
    }
}
