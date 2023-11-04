package org.lab5.com.sb224sc.classes;

import java.io.FileWriter;
import java.io.IOException;
import java.util.List;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.opencsv.CSVWriter;

@SuppressWarnings("java:S106")
public class ExportPrescriptions {
    private ExportPrescriptions() {
        throw new IllegalStateException("Utility class.");
    }

    /**
     * Exports the given list of prescriptions as JSON to the specified file path.
     *
     * @param prescriptions the list of prescriptions to be exported
     * @param filePath      the file path where the JSON file will be exported
     */
    public static void exportPrescriptionsAsJSON(List<Prescriptions> prescriptions, String filePath) {
        try (FileWriter fileWriter = new FileWriter(filePath + "export.json")) {
            Gson gson = new GsonBuilder()
                    .setPrettyPrinting()
                    .create();

            gson.toJson(prescriptions, fileWriter);
            System.out.println("Prescriptions exported to JSON successfully.\n");
        } catch (IOException e) {
            System.err.println("Error exporting prescriptions to JSON: " + e.getMessage());
        }
    }

    /**
     * Exports a list of prescriptions as a CSV file.
     *
     * @param prescriptions the list of prescriptions to export
     * @param filePath      the path to the file where the CSV should be saved
     */
    public static void exportPrescriptionsAsCSV(List<Prescriptions> prescriptions, String filePath) {
        try (CSVWriter csvWriter = new CSVWriter(new FileWriter(filePath + "export.csv"))) {
            String[] header = { "ID", "Date and Time", "Drug Name", "Quantity", "Price per Package", "Total Cost" };
            csvWriter.writeNext(header);

            for (Prescriptions prescription : prescriptions) {
                String[] data = {
                        String.valueOf(prescription.getId()),
                        prescription.getDateTime(),
                        prescription.getDrugName(),
                        String.valueOf(prescription.getQuantity()),
                        String.valueOf(prescription.getPricePerPackage()),
                        String.valueOf(prescription.getTotalCost())
                };
                csvWriter.writeNext(data);
            }

            System.out.println("Prescriptions exported to CSV successfully.\n");
        } catch (IOException e) {
            System.err.println("Error exporting prescriptions to CSV: " + e.getMessage());
        }
    }
}
