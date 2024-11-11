package com.onlinefarmacy;

import java.util.ArrayList;
import java.util.List;

public class ReceiptStorage {
    private static List<Receipt> storedReceipts = new ArrayList<>();
    
    public static void storeReceipt(Receipt receipt) {
        storedReceipts.add(receipt);
    }
    public static void printReceipts() {
        for (Receipt receipt : storedReceipts) {
            System.out.println(((Receipt) receipt).toJson());
        }
    }
    public static List<Receipt> getStoredReceipts() {
        return storedReceipts;
    }

    public static void removeReceipt(Integer index) {
        storedReceipts.remove(storedReceipts.get(index));
    }

    public static void updateDrug(Integer index, String newDrug, Integer drugIndex) {
        Receipt receiptToUpdate = storedReceipts.get(index);
        receiptToUpdate.setDrugName(newDrug);
        receiptToUpdate.setAPrice(ReceiptHandling.getDrugPriceByIndex(drugIndex));
        storedReceipts.set(index, receiptToUpdate);
    }
    public static void updateQuantity(Integer index, Integer newQuantity) {
        Receipt receiptToUpdate = storedReceipts.get(index);
        receiptToUpdate.setAmount(newQuantity);
        storedReceipts.set(index, receiptToUpdate); 
    }
    public static void exportAllAsJson(String recDirectory) {
        String savePath1 = "";
        for (Receipt rec : storedReceipts) {
            String date = rec.getDateTime();
            String drug = rec.getDrugName();
            String filename = drug + " - " + date;
            savePath1 = rec.jsonExporter(rec, filename, recDirectory);
        }
            System.out.println("Files saved to " + savePath1);
    }
    public static void exportAllAsCSV(String recDirectory) {
        String savePath2 = "";
        for (Receipt rec : storedReceipts) {
            String date = rec.getDateTime();
            String drug = rec.getDrugName();
            String filename = drug + " - " + date;
            savePath2 = rec.CSVExporter(rec, filename, recDirectory);
        }
        System.out.println("Files saved to " + savePath2);
    }
}
