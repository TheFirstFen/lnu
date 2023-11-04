package org.lab5.com.sb224sc.classes;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class PharmacyTest {
    private Pharmacy pharmacy;

    @BeforeEach
    void setUp() {
        pharmacy = new Pharmacy("TestPharmacy", "./testPath/");
    }

    @Test
    void testConstructorWithInput() {
        assertEquals("TestPharmacy", pharmacy.pharmacyName);
        assertTrue(pharmacy.prescriptions.isEmpty());
    }

    @Test
    void testConstructorWithInvalidInput() {
        pharmacy = new Pharmacy(null, null);
        assertNull(pharmacy.pharmacyName);
        assertTrue(pharmacy.prescriptions.isEmpty());
    }

    @Test
    void testConstructorWithoutInput() {
        pharmacy = new Pharmacy();
        assertNull(pharmacy.pharmacyName);
        assertTrue(pharmacy.prescriptions.isEmpty());
    }

    @Test
    void testAddPrescription() {
        Prescriptions prescription = new Prescriptions(1, "2023-09-28 10:00:00", "Medicine", 5, 10.0);

        pharmacy.addPrescription(prescription);

        assertEquals(1, pharmacy.prescriptions.size());
        assertTrue(pharmacy.prescriptions.contains(prescription));
    }

    @Test
    void testGetNextPrescriptionId() {
        assertEquals(0, pharmacy.getNextPrescriptionId());

        pharmacy.addPrescription(new Prescriptions(1, "2023-09-28 10:00:00", "Medicine", 5, 10.0));

        assertEquals(2, pharmacy.getNextPrescriptionId());
    }

    @Test
    void testGetPrescriptionsList() {
        pharmacy.addPrescription(new Prescriptions(1, "2023-09-28 10:00:00", "Medicine", 5, 10.0));
        assertEquals(1, pharmacy.getPrescriptionsList().size());
    }
}
