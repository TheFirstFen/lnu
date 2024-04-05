import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import java.io.FileWriter;
import java.io.IOException;

import java.util.List;

public class WriteJSON {
    public static void writeToJSON(List<List<Double>> toJSON, String fileName) {
        Gson gson = new GsonBuilder().setPrettyPrinting().create();
        String json = gson.toJson(toJSON);

        try (FileWriter writer = new FileWriter("./data/" + fileName + ".json")) {
            writer.write(json);
        } catch (IOException e) {
            e.getMessage();
        }
    }

    public static void writeJSON(List<Double> toJSON, String fileName) {
        Gson gson = new GsonBuilder().setPrettyPrinting().create();
        String json = gson.toJson(toJSON);

        try (FileWriter writer = new FileWriter("./data/" + fileName + ".json")) {
            writer.write(json);
        } catch (IOException e) {
            e.getMessage();
        }
    }
}
