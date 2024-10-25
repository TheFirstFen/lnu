package lab5.com.drugs;

import java.io.*;
import java.util.*;
import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import java.lang.reflect.Type;

public class Pharmacy {
    private String receiptDirectory;
    private List<Receipt> receipts;
    private int nextReceiptId;

    public Pharmacy(String name, String receiptDirectory) {
        this.receiptDirectory = receiptDirectory;
        this.receipts = new ArrayList<>();
        this.nextReceiptId = 1;
    }

    public void addReceipt(Receipt receipt){
        receipt.setId(nextReceiptId++);
        receipts.add(receipt);
        saveReceipt(receipt);
    }

    public void uppdateReceipt(Receipt updatedReceipt) {
        for (int i = 0; i < receipts.size(); i++) {
            Receipt receipt = receipts.get(i);
            if (receipt.getId() == updatedReceipt.getId()) {
                receipts.set(i, updatedReceipt);
                saveReceipt(updatedReceipt);
                return;
            }
        }
    }

    public void removeReceipt(int receiptId) {
        receipts.removeIf(r -> r.getId() == receiptId);
        deleteReceiptFile(receiptId);
    }

    public Receipt getReceipt(int receiptId) {
        for (Receipt receipt : receipts) {
            if (receipt.getId() == receiptId) {
                return receipt;
            }
        }
        return null;
    }

    public List<Receipt> getAllReceipts() {
        return receipts;
    }

    public void exportAllReceiptsAsJSON() {
        try {
            Gson gson = new Gson();
            String json = gson.toJson(receipts);
            String fileName = receiptDirectory + "receipts.json";
            FileWriter writer = new FileWriter(fileName);
            writer.write(json);
            writer.close();
            System.out.println("Receipts exported as JSON to: " + fileName);
        }catch (IOException e) { 
            System.err.println("Error exporting receipts as JSON: " + e.getMessage());
        }
    }

    public void exportAllReceiptsAsCVS() {
        try {
            String fileName = receiptDirectory + "receipts.csv";
            FileWriter writer = new FileWriter(fileName);
            writer.write("ID,Date,Drug Name,Number of Packages,Price Per Package,Total Cost\n");
            for (Receipt receipt : receipts) {
                writer.write(receipt.getId() + "," +
                receipt.getDate() + "," +
                receipt.getDrugName() + "," +
                receipt.getNumPackages() + "," +
                receipt.getPricePerPackage() + "," +
                receipt.getTotalCost() + "\n");
            }
            writer.close();
            System.out.println("Receipts exported as CSV to: " + fileName);
        }catch (IOException e) { 
            System.err.println("Error exporting receipts as CVS: " + e.getMessage());
        }
    }

    private void saveReceipt(Receipt receipt) {
        try{
            Gson gson = new Gson();
            String json = gson.toJson(receipt);
            String fileName = receiptDirectory + "receipts_"+ receipt.getId() + ".json";
            FileWriter writer = new FileWriter(fileName);
            writer.write(json);
            writer.close();
            System.out.println("Receipt saved to: " + fileName);
        }catch(IOException e) {
            System.err.println("Error saving receipt: " + e.getMessage());
        }
    }

    private void deleteReceiptFile(int receiptId) {
        String fileName = receiptDirectory + "receipts_" + receiptId + ".json";
        File file = new File(fileName);
        if (file.exists() && file.delete()) {
            System.out.println("Receipt deleted: " + fileName);
        }
    }

    public void loadReceiptsFromJSON(String receiptDirectory) {
        try {
            Gson gson = new Gson();
            Type receiptListType = new TypeToken<List<Receipt>>() {}.getType();

            BufferedReader reader = new BufferedReader(new FileReader(receiptDirectory));
            List<Receipt> loadedReceipts = gson.fromJson(reader, receiptListType);
            reader.close();

            for (Receipt receipt : loadedReceipts) {
                addReceipt(receipt);
            }

        } catch (IOException e) {
            System.err.println("Error loading receipts from JSON: " + e.getMessage());
        }
    }
    
}
