package com.onlinefarmacy;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;

import org.junit.jupiter.api.Test;

public class TestMain {
    
    @Test
    public void testMain() {
        Main.exitprogram = true;
        Main.main(new String[0]);
        assertNotNull(ReceiptStorage.getStoredReceipts());
        assertEquals("Alvedon", ReceiptHandling.getDrugNameByIndex(0));
        assertEquals(20.0, ReceiptHandling.getDrugPriceByIndex(0));
    }
}
