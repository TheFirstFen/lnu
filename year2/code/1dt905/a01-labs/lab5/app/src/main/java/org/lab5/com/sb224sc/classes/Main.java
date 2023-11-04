package org.lab5.com.sb224sc.classes;

import java.io.FileReader;
import java.io.IOException;

import com.google.gson.Gson;
import com.google.gson.JsonElement;
import com.google.gson.JsonParser;

@SuppressWarnings("java:S106")
public class Main {
    private String configPath = "./config/";

    /**
     * Runs the pharmacy application.
     */
    public void run() {
        PharmacyConfig config = readConfigFromJson(configPath);

        if (config == null) {
            System.err.println("Failed to read config file");
            return;
        }

        String pharmacyName = config.getPharmacyName();
        String loadPath = config.getImportPath();
        String jsonPath = config.getExportJSONPath();
        String csvPath = config.getExportCSVPath();

        PharmacyMenu pharmacyApp = new PharmacyMenu(pharmacyName, loadPath, jsonPath, csvPath);

        pharmacyApp.menu();
    }

    /**
     * Reads the configuration from a JSON file.
     *
     * @param configPath the path to the configuration file
     * @return the PharmacyConfig object containing the parsed configuration
     */
    private static PharmacyConfig readConfigFromJson(String configPath) {
        try (FileReader fileReader = new FileReader(configPath + "config.json")) {
            JsonElement jsonElement = JsonParser.parseReader(fileReader);

            return new Gson().fromJson(jsonElement, PharmacyConfig.class);
        } catch (IOException e) {
            e.getMessage();
            return null;
        }
    }
}
