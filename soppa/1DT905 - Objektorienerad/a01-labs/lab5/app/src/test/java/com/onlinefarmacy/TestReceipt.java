package com.onlinefarmacy;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class TestReceipt {

    @Test
    public void testSetDateTime() {
        Receipt receipt = new Receipt();
        receipt.setDateTime();
        assertNotNull(receipt.getDateTime());
    }

    @Test
    public void testSetUniqueId() {
        Receipt receipt = new Receipt();
        receipt.setUniqueId(12345);
        assertEquals(12345, receipt.getUniqueId());
    }

    @Test
    public void testSetDrugName() {
        Receipt receipt = new Receipt();
        receipt.setDrugName("Test Drug");
        assertEquals("Test Drug", receipt.getDrugName());
    }

    @Test
    public void testSetAPrice() {
        Receipt receipt = new Receipt();
        receipt.setAPrice(25.0);
        assertEquals(25.0, receipt.getaAPrice(), 0.001);
    }

    @Test
    public void testSetAmount() {
        Receipt receipt = new Receipt();
        receipt.setAPrice(20.0);
        receipt.setAmount(5);
        assertEquals(5, receipt.getAmount());
    }

    @Test
    public void testSetTotSum() {
        Receipt receipt = new Receipt();
        receipt.setAPrice(25.0);
        receipt.setAmount(5);
        receipt.setTotSum();
        assertEquals(125.0, receipt.getTotSum(), 0.001);
    }

    @Test
    public void testToJson() {
        Receipt receipt = new Receipt();
        receipt.setDateTime();
        receipt.setUniqueId(12345);
        receipt.setDrugName("Test Drug");
        receipt.setAPrice(25.0);
        receipt.setAmount(5);
        String json = receipt.toJson();
        assertTrue(json.contains("12345"));
        assertTrue(json.contains("Test Drug"));
        assertTrue(json.contains("125.0"));
    }

    @Test
    public void testGetJsonFilePath() {
        Receipt receipt = new Receipt();
        receipt.setDateTime();
        receipt.setDrugName("Test Drug");
        String expectedPath = "JsonExports/Test Drug - " + receipt.getDateTime();
        assertEquals(expectedPath, receipt.getJsonFilePath());
    }

    @Test
    public void testGetCSVFilePath() {
        Receipt receipt = new Receipt();
        receipt.setDateTime();
        receipt.setDrugName("Test Drug");
        String expectedPath = "CSVExports/Test Drug - " + receipt.getDateTime();
        assertEquals(expectedPath, receipt.getCSVFilePath());
    }
}