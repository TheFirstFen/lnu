package org.lab5.com.sb224sc.classes;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class PharmacyConfigTest {
    private PharmacyConfig pharmacyConfig;

    @BeforeEach
    void setUp() {
        // Create a new PharmacyConfig instance before each test
        pharmacyConfig = new PharmacyConfig("TestPharmacy", "/import", "/exportJSON", "/exportCSV");
    }

    @Test
    void testConstructorAndGetters() {
        // Test the constructor and getter methods
        assertEquals("TestPharmacy", pharmacyConfig.getPharmacyName());
        assertEquals("/import", pharmacyConfig.getImportPath());
        assertEquals("/exportJSON", pharmacyConfig.getExportJSONPath());
        assertEquals("/exportCSV", pharmacyConfig.getExportCSVPath());
    }

    @Test
    void testSetters() {
        // Test the setter methods
        pharmacyConfig.setPharmacyName("NewPharmacy");
        pharmacyConfig.setImportPath("/newImport");
        pharmacyConfig.setExportJSONPath("/newExportJSON");
        pharmacyConfig.setExportCSVPath("/newExportCSV");

        assertEquals("NewPharmacy", pharmacyConfig.getPharmacyName());
        assertEquals("/newImport", pharmacyConfig.getImportPath());
        assertEquals("/newExportJSON", pharmacyConfig.getExportJSONPath());
        assertEquals("/newExportCSV", pharmacyConfig.getExportCSVPath());
    }
}
