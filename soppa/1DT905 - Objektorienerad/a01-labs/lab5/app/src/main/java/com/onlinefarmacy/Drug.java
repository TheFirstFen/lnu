package com.onlinefarmacy;


public class Drug {
    private String drugName;
    private Double drugPrice;


    public void setDrug(String name, Double price) {
        drugName = name;
        drugPrice = price;
    }

    public String getName() {
        return drugName;
    }
    public Double getPrice() {
        return drugPrice;
    }
}
