package Algoritmer;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class ReadData {
    public static String[][] readData(String filePath) {
        List<String[]> data = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] courses = line.split(";");
                if (courses.length == 2) {
                    //System.out.println(courses[1] + " -> " + courses[0]);
                    data.add(courses);
                } else {
                    System.err.println("Invalid data format: " + line);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        String[][] info = new String[data.size()][];
        data.toArray(info);

        return info;
    }
}
