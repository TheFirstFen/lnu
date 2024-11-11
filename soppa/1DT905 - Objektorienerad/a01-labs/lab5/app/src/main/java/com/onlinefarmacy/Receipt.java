package com.onlinefarmacy;

import java.io.File;
import java.io.FileWriter;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

public class Receipt {
    private String dateTime;
    private Integer uniqueId;
    private String drugName;
    private Double aPrice;
    private Integer amount = 0;
    private Double totSum;
    
    public void setDateTime() {
        LocalDateTime currentDateTime = LocalDateTime.now();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        String fixedTime = currentDateTime.format(formatter);
        this.dateTime = fixedTime;
    }
    public void setUniqueId(Integer Id) {
        this.uniqueId = Id;
    }
    public void setDrugName(String drug) {
        this.drugName = drug;
    }
    public void setAPrice(Double price) {
        this.aPrice = price;
        setTotSum();
    }
    public void setAmount(Integer amount) {
        this.amount = amount;
        setTotSum();
    }
    public void setTotSum() {
        this.totSum = this.amount * this.aPrice;
    }
    public String toJson() {
        Gson gson = new GsonBuilder().setPrettyPrinting().create();
        return gson.toJson(this);
    }
    public String getDateTime() {
        return dateTime;
    }
    public Integer getUniqueId() {
        return uniqueId;
    }
    public String getDrugName() {
        return drugName;
    }
    public Double getTotSum() {
        return totSum;
    }
    public double getaAPrice() {
        return aPrice;
    }
    public Integer getAmount() {
        return amount;
    }
    
    public String getJsonFilePath() {
        return "JsonExports/" + drugName + " - " + dateTime;
    }

    public String getCSVFilePath() {
        return "CSVExports/" + drugName + " - " + dateTime;
    }
    
    public String jsonExporter(Receipt receipt, String fileName, String recDirectory) {
        try {
            String cwd = System.getProperty("user.dir");
            String filePath = recDirectory + "/JsonExports/" + fileName + ".json";
            String json = toJson();
            File directory = new File(recDirectory + "/JsonExports");
            if (!directory.exists()) {
                directory.mkdirs();
            }
            File file = new File(filePath);
            file.createNewFile();
            try (FileWriter writer = new FileWriter(filePath)) {
                writer.write(json);
            }
            System.out.println("Receipt exported as " + fileName);
            return cwd + "/" + recDirectory + "/JsonExports";
        } catch (Exception e) {
            String error = e.toString();
            return error;
        }
    }
    public String CSVExporter(Receipt receipt, String fileName, String recDirectory) {
        try {
            String cwd = System.getProperty("user.dir");
            String filePath = recDirectory + "/CSVExports/" + fileName + ".csv";
            File directory = new File(recDirectory + "/CSVExports");
            if (!directory.exists()) {
                directory.mkdirs();
            }
            File file = new File(filePath);
            file.createNewFile();
            StringBuilder csvData = new StringBuilder();
            csvData.append("DateTime: " + dateTime + "\n");
            csvData.append("UniqueId: " + uniqueId + "\n");
            csvData.append("DrugName: " + drugName + "\n");
            csvData.append("Price: " + aPrice + "\n");
            csvData.append("Amount: " + amount + "\n");
            csvData.append("TotalSum: " + totSum + "\n");
            try (FileWriter writer = new FileWriter(filePath)) {
                writer.write(csvData.toString());
            }
            System.out.println("Receipt exported as " + fileName);
            return cwd + "/" + recDirectory + "/CSVExports";
        } catch (Exception e) {
            String error = e.toString();
            return error;
        }
    }

}
