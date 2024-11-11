package com.onlinefarmacy;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotEquals;

import java.io.File;

import org.junit.jupiter.api.Test;

public class TestReceiptStorage {


    @Test
    public void testUpdateDrug() {
        InitializeDrugs.setDrugs();
        InitializeReceipts.setReceipts();
        ReceiptStorage.updateDrug(0, "Morifin", 4);
        ReceiptStorage.updateQuantity(0, 250);
        Receipt updatedReceipt = ReceiptStorage.getStoredReceipts().get(0);
        assertEquals("Morifin", updatedReceipt.getDrugName());
        assertEquals(250, updatedReceipt.getAmount());
    }
    @Test
    public void testRemoveDrug() {
        InitializeDrugs.setDrugs();
        InitializeReceipts.setReceipts();
        Receipt oldFirstIndexReceipt = ReceiptStorage.getStoredReceipts().get(0);
        ReceiptStorage.removeReceipt(0);
        Receipt updatedReceipt = ReceiptStorage.getStoredReceipts().get(0);
        assertNotEquals(oldFirstIndexReceipt, updatedReceipt);
    }
    @Test
    public void testJsonExport() {
        ReceiptStorage.getStoredReceipts().clear();
        Receipt testReceipt1 = new Receipt();
        testReceipt1.setDateTime();
        testReceipt1.setDrugName("Test Drug");
        ReceiptStorage.storeReceipt(testReceipt1);

        String recDirectory = "ExportsTest";
        ReceiptStorage.exportAllAsJson(recDirectory);

        String expectedPath = "JsonExports" + "/" + testReceipt1.getDrugName() + " - " + testReceipt1.getDateTime();
        assertEquals(expectedPath, ReceiptStorage.getStoredReceipts().get(0).getJsonFilePath());
        cleanFiles(recDirectory, testReceipt1, "Json");
    }
    @Test
    public void testCSVExport() {
        ReceiptStorage.getStoredReceipts().clear();
        Receipt testReceipt1 = new Receipt();
        testReceipt1.setDateTime();
        testReceipt1.setDrugName("Test Drug");
        ReceiptStorage.storeReceipt(testReceipt1);

        String recDirectory = "ExportsTest";
        ReceiptStorage.exportAllAsCSV(recDirectory);

        String expectedPath = "CSVExports" + "/" + testReceipt1.getDrugName() + " - " + testReceipt1.getDateTime();
        assertEquals(expectedPath, ReceiptStorage.getStoredReceipts().get(0).getCSVFilePath());
        cleanFiles(recDirectory, testReceipt1, "CSV");
    }
    // Method that removes the created test files
    private void cleanFiles(String recDirectory, Receipt testReceipt, String format) {
    String filePath = recDirectory + "/" + format + "Exports/" + testReceipt.getDrugName() + " - " + testReceipt.getDateTime() + "." + format.toLowerCase();
    
    File file = new File(filePath);
    if (file.exists() && file.isFile()) {
        if (file.delete()) {
            System.out.println(format + " file deleted successfully.");
        } else {
            System.out.println("Failed to delete CSV file.");
        }
    }
    File directory = new File(recDirectory + "/" + format + "Exports/");
    if (directory.exists() && directory.isDirectory()) {
        if (directory.delete()) {
            System.out.println(format + " directory deleted successfully.");
        } else {
            System.out.println("Failed to delete " + format + " directory.");
        }
    }
}
}


