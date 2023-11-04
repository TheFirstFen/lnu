package org.lab5.com.sb224sc.classes;

import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.List;
import java.util.regex.Pattern;

import com.google.gson.Gson;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonParser;

@SuppressWarnings("java:S106")
public class LoadStorage {
    private LoadStorage() {
        throw new IllegalStateException("Utility class.");
    }

    /**
     * Loads prescriptions from JSON files in a specified directory.
     *
     * @param prescriptions the list to store the loaded prescriptions
     * @param dirPath       the path to the directory containing the JSON files
     */
    public static void loadPrescriptionsFromJSON(List<Prescriptions> prescriptions,
            String dirPath) {
        Pattern jsonPattern = Pattern.compile(".*\\.json$");

        File directory = new File(dirPath);
        File[] files = directory.listFiles();

        if (files != null) {
            for (File file : files) {
                if (jsonPattern.matcher(file.getName()).matches()) {
                    try (FileReader fileReader = new FileReader(file)) {
                        JsonArray jsonArray = JsonParser.parseReader(fileReader).getAsJsonArray();

                        for (JsonElement jsonElement : jsonArray) {
                            Prescriptions prescription = new Gson().fromJson(jsonElement, Prescriptions.class);
                            prescription.setTotalCost();
                            prescriptions.add(prescription);
                        }
                    } catch (IOException e) {
                        System.err.println("Error loading JSON files: " + e.getMessage());
                    }
                }
            }
        }
    }
}
