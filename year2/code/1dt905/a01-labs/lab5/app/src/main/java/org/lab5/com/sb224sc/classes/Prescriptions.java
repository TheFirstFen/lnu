package org.lab5.com.sb224sc.classes;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class Prescriptions {
    private int id;
    private String dateTime;
    private String drugName;
    private int quantity;
    private double pricePerPackage;
    private double totalCost;

    public Prescriptions(int id, String dateTime, String drugName, int quantity, double pricePerPackage) {
        this.id = id;
        this.dateTime = dateTime;
        this.drugName = drugName;
        this.quantity = quantity;
        this.pricePerPackage = pricePerPackage;
    }

    /**
     * Retrieves the total cost.
     *
     * @return the total cost
     */
    public double getTotalCost() {
        return totalCost;
    }

    /**
     * Calculates the total cost by multiplying the quantity of packages by the
     * price per package.
     */
    public void setTotalCost() {
        this.totalCost = this.quantity * this.pricePerPackage;
    }

    /**
     * Retrieves the ID of the object.
     *
     * @return the ID of the object.
     */
    public int getId() {
        return id;
    }

    /**
     * Sets the ID of the object.
     *
     * @param id the new ID for the object
     */
    public void setId(int id) {
        this.id = id; // * Testing only!
    }

    /**
     * Retrieves the current date and time as a string.
     *
     * @return the current date and time as a string
     */
    public String getDateTime() {
        return dateTime;
    }

    /**
     * Sets the value of the dateTime field.
     *
     * @param dateTime the new value for the dateTime field
     */
    public void setDateTime(String dateTime) {
        this.dateTime = dateTime; // * Testing only!
    }

    /**
     * Sets the value of the dateTime variable to the current date and time.
     */
    public void setDateTime() {
        DateTimeFormatter timeFormat = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        String now = LocalDateTime.now().format(timeFormat);
        this.dateTime = now;
    }

    /**
     * Retrieves the drug name.
     *
     * @return the drug name
     */
    public String getDrugName() {
        return drugName;
    }

    /**
     * Sets the drug name.
     *
     * @param drugName the name of the drug
     */
    public void setDrugName(String drugName) {
        this.drugName = drugName;
    }

    /**
     * Gets the quantity.
     *
     * @return the quantity
     */
    public int getQuantity() {
        return quantity;
    }

    /**
     * Sets the quantity of the object.
     *
     * @param quantity the new quantity to be set
     */
    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    /**
     * Retrieves the price per package.
     *
     * @return the price per package
     */
    public double getPricePerPackage() {
        return pricePerPackage;
    }

    /**
     * Sets the price per package.
     *
     * @param pricePerPackage the price per package to be set
     */
    public void setPricePerPackage(double pricePerPackage) {
        this.pricePerPackage = pricePerPackage;
    }

    /**
     * Returns a string representation of the Prescription object.
     *
     * @return A string containing the prescription ID, date and time, drug name,
     *         quantity,
     *         price per package, and total cost.
     */
    @Override
    public String toString() {
        return "Prescription ID: " + id +
                "\nDate and Time: " + dateTime +
                "\nDrug Name: " + drugName +
                "\nQuantity: " + quantity +
                "\nPrice per Package: sek " + pricePerPackage +
                "\nTotal cost: sek " + getTotalCost();
    }
}
