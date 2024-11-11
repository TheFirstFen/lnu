package com.onlinefarmacy;

public class InitializeReceipts {
    

    public static void setReceipts() {
        ReceiptHandling.createReceipt(0, 3);
        ReceiptHandling.createReceipt(1, 1);
        ReceiptHandling.createReceipt(2, 2);
        ReceiptHandling.createReceipt(3, 7);
        ReceiptHandling.createReceipt(4, 4);
    }
}
