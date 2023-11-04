package org.lab5.com.sb224sc.classes;

public class PharmacyConfig {
    private String pharmacyName;
    private String importPath;
    private String exportJSONPath;
    private String exportCSVPath;

    public PharmacyConfig(String pharmacyName, String importPath, String exportJSONPath, String exportCSVPath) {
        this.pharmacyName = pharmacyName;
        this.importPath = importPath;
        this.exportJSONPath = exportJSONPath;
        this.exportCSVPath = exportCSVPath;
    }

    /**
     * Returns the name of the pharmacy.
     *
     * @return the name of the pharmacy
     */
    public String getPharmacyName() {
        return pharmacyName;
    }

    /**
     * Sets the pharmacy name.
     *
     * @param pharmacyName the new name of the pharmacy
     */
    public void setPharmacyName(String pharmacyName) {
        this.pharmacyName = pharmacyName;
    }

    /**
     * Returns the import path of the Java function.
     *
     * @return the import path of the Java function
     */
    public String getImportPath() {
        return importPath;
    }

    /**
     * Sets the import path.
     *
     * @param importPath the import path to be set
     */
    public void setImportPath(String importPath) {
        this.importPath = importPath;
    }

    /**
     * Retrieves the path of the JSON file to be exported.
     *
     * @return the path of the JSON file to be exported
     */
    public String getExportJSONPath() {
        return exportJSONPath;
    }

    /**
     * Sets the export JSON path.
     *
     * @param exportJSONPath the path to export JSON
     */
    public void setExportJSONPath(String exportJSONPath) {
        this.exportJSONPath = exportJSONPath;
    }

    /**
     * Retrieves the path of the exported CSV file.
     *
     * @return the path of the exported CSV file
     */
    public String getExportCSVPath() {
        return exportCSVPath;
    }

    /**
     * Sets the export CSV path.
     *
     * @param exportCSVPath the path where the CSV file will be exported to
     */
    public void setExportCSVPath(String exportCSVPath) {
        this.exportCSVPath = exportCSVPath;
    }
}
