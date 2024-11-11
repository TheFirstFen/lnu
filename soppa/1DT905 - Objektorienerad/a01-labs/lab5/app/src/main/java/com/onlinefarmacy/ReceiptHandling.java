 package com.onlinefarmacy;

import java.util.ArrayList;
import java.util.List;

public class ReceiptHandling {
    private static Integer uniqueId = 999;
    private static List<String> drugNames = new ArrayList<>();
    private static List<Double> drugPrices = new ArrayList<>();

    public static void setDrugNamesList(Drug alvedon, Drug ipren, Drug desloratadine, Drug brikanyl, Drug morifin) {
        // Gives drugs "Values" 0-alvedon 1-ipren ands so on
        drugNames.add(alvedon.getName());
        drugNames.add(ipren.getName());
        drugNames.add(desloratadine.getName());
        drugNames.add(brikanyl.getName());
        drugNames.add(morifin.getName());
    }
    public static void setDrugPriceList(Drug alvedon, Drug ipren, Drug desloratadine, Drug brikanyl, Drug morifin) {
        // Gives drugs "Values" 0-alvedon 1-ipren ands so on
        drugPrices.add(alvedon.getPrice());
        drugPrices.add(ipren.getPrice());
        drugPrices.add(desloratadine.getPrice());
        drugPrices.add(brikanyl.getPrice());
        drugPrices.add(morifin.getPrice());
    }

    public static void createReceipt(Integer choice, Integer amount) {
        uniqueId += 1;
        Receipt newReceipt = new Receipt();
        newReceipt.setDateTime();
        newReceipt.setUniqueId(uniqueId);
        newReceipt.setDrugName(drugNames.get(choice));
        newReceipt.setAPrice(drugPrices.get(choice));
        newReceipt.setAmount(amount);
        ReceiptStorage.storeReceipt(newReceipt);
    }
    public static String getDrugNameByIndex(Integer index) {
        return drugNames.get(index);
    }
    public static Double getDrugPriceByIndex(Integer index) {
        return drugPrices.get(index);
    }
}