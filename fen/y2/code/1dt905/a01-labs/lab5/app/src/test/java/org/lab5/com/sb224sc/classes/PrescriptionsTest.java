package org.lab5.com.sb224sc.classes;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class PrescriptionsTest {
    private Prescriptions prescription;

    @BeforeEach
    void setUp() {
        prescription = new Prescriptions(1, "2023-09-28 10:00:00", "MedicineA", 5, 10.0);
        prescription.setTotalCost();
    }

    @Test
    void testGetters() {
        assertEquals(1, prescription.getId());
        assertEquals("2023-09-28 10:00:00", prescription.getDateTime());
        assertEquals("MedicineA", prescription.getDrugName());
        assertEquals(5, prescription.getQuantity());
        assertEquals(10.0, prescription.getPricePerPackage(), 0.001);
        assertEquals(50.0, prescription.getTotalCost(), 0.001);
    }

    @Test
    void testSetters() {
        prescription.setId(2);
        prescription.setDateTime("2023-09-29 14:30:00");
        prescription.setDrugName("MedicineB");
        prescription.setQuantity(3);
        prescription.setPricePerPackage(8.5);
        prescription.setTotalCost();

        assertEquals(2, prescription.getId());
        assertEquals("2023-09-29 14:30:00", prescription.getDateTime());
        assertEquals("MedicineB", prescription.getDrugName());
        assertEquals(3, prescription.getQuantity());
        assertEquals(8.5, prescription.getPricePerPackage(), 0.001);
        assertEquals(25.5, prescription.getTotalCost(), 0.001);
    }

    @Test
    void testSetTotalCost() {
        prescription.setQuantity(0);
        prescription.setTotalCost();
        assertEquals(0.0, prescription.getTotalCost(), 0.001);

        prescription.setQuantity(5);
        prescription.setPricePerPackage(0.0);
        prescription.setTotalCost();
        assertEquals(0.0, prescription.getTotalCost(), 0.001);
    }

    @Test
    void testSetDateTime() {
        prescription.setDateTime();
        assertNotNull(prescription.getDateTime());
    }

    @Test
    void testToString() {
        assertNotNull(prescription.toString());
    }
}
