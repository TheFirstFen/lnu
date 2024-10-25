package lab5.com.drugs;

import java.util.*;

public class Receipt {
    private int id;
    private Date date;
    private String drugName;
    private int numPackages;
    private double pricePerPackage;

    public Receipt(int id, Date date, String drugName, int numPackages, double pricePerPackage) {
        this.id = id;
        this.date = date;
        this.drugName = drugName;
        this.numPackages = numPackages;
        this.pricePerPackage = pricePerPackage;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Date getDate() {
        return date;
    }

    public String getDrugName() {
        return drugName;
    }

    public int getNumPackages() {
        return numPackages;
    }

    public double getPricePerPackage() {
        return pricePerPackage;
    }

    public double getTotalCost() {
        return numPackages * pricePerPackage;
    }

    public void setDate(Date newDate) {
        this.date = newDate;
    }

    public void setDrugName(String newDrugName) {
        this.drugName = newDrugName;
    }

    public void setNumPackages(int newNumPackages) {
        this.numPackages = newNumPackages;
    }

    public void setPricePerPackage(double newPricePerPackage) {
        this.pricePerPackage = newPricePerPackage;
    }
}
