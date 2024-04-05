package org.lab5.com.sb224sc.classes;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.ArrayList;
import java.util.List;

import org.junit.jupiter.api.Test;

class LoadStorageTest {
    @Test
    void testLoadPrescriptionsFromJSON() {
        String testDirPath = "./data/import/";

        List<Prescriptions> loadedPrescriptions = new ArrayList<>();

        LoadStorage.loadPrescriptionsFromJSON(loadedPrescriptions, testDirPath);

        assertFalse(loadedPrescriptions.isEmpty());

        for (Prescriptions prescription : loadedPrescriptions) {
            prescription.setTotalCost();

            Object id = prescription.getId();
            Object quantity = prescription.getQuantity();
            Object pricePerPackage = prescription.getPricePerPackage();
            Object totalCost = prescription.getTotalCost();
            assertTrue(id instanceof Integer);
            assertNotNull(prescription.getDateTime());
            assertNotNull(prescription.getDrugName());
            assertTrue(quantity instanceof Integer);
            assertTrue(pricePerPackage instanceof Double);
            assertTrue(totalCost instanceof Double);
        }
    }
}
