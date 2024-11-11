package com.onlinefarmacy;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.List;

import org.junit.jupiter.api.Test;

public class TestInitializeReceipts {
    @Test
    public void InitializeTest() {
        InitializeDrugs.setDrugs();
        InitializeReceipts.setReceipts();
        List<Receipt> receipts = ReceiptStorage.getStoredReceipts();
        Receipt indexZeroRec = receipts.get(0);
        String name = indexZeroRec.getDrugName();
        Integer amount = indexZeroRec.getAmount();
        assertEquals("Alvedon", name);
        assertEquals(3, amount);
    }
}
