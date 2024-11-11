package com.onlinefarmacy;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class TestReceiptHandling {

    @Test
    public void DrugNamesListTest() {
        InitializeDrugs.setDrugs();
        String zeroIndex = ReceiptHandling.getDrugNameByIndex(0);
        assertEquals("Alvedon", zeroIndex);
    }
    @Test
    public void DrugPriceListTest() {
        InitializeDrugs.setDrugs();
        Double zeroIndexPrice = ReceiptHandling.getDrugPriceByIndex(0);
        assertEquals(20.0, zeroIndexPrice);
    }
}

