package org.lab5.com.sb224sc.classes;

import java.util.ArrayList;
import java.util.List;

public class Pharmacy {
    protected List<Prescriptions> prescriptions = new ArrayList<>();
    protected String pharmacyName;

    public Pharmacy() {
        this.prescriptions.clear();
    }

    public Pharmacy(String pharmacyName, String loadPath) {
        try {
            LoadStorage.loadPrescriptionsFromJSON(this.prescriptions, loadPath);
            this.pharmacyName = pharmacyName;
        } catch (Exception e) {
            e.getMessage();
        }
    }

    /**
     * Returns the list of prescriptions.
     *
     * @return the list of prescriptions
     */
    public List<Prescriptions> getPrescriptionsList() {
        return prescriptions;
    }

    /**
     * Adds a prescription to the list of prescriptions.
     *
     * @param prescription the prescription to be added
     */
    public void addPrescription(Prescriptions prescription) {
        prescription.setTotalCost();
        prescriptions.add(prescription);
    }

    /**
     * Returns the next prescription ID.
     *
     * @return the next prescription ID
     */
    public int getNextPrescriptionId() {
        if (prescriptions.isEmpty()) {
            return 0;
        } else {
            int lastIndex = prescriptions.size() - 1;
            return prescriptions.get(lastIndex).getId() + 1;
        }
    }
}
