package com.onlinefarmacy;

import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import java.io.FileReader;

public class Config {
    public static JsonObject loadConfig(String configFilePath) {
        try (FileReader reader = new FileReader(configFilePath)) {
            return JsonParser.parseReader(reader).getAsJsonObject();
        } catch (Exception e) {
            System.err.println(e.toString());
            return null; 
        }
    }
}