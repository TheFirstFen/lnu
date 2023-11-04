package task2.com.sb224sc.classes;

import com.google.gson.Gson;

public class PrintAllDetails {
    /**
     * Prints details of all shapes, including area and circumference.
     */
    public static void printAllDetails() {
        System.out.println("All details on all shapes:");
        for (AbstractShape shape : PrintAllShapes.shapeList) {
            System.out.println(shape);
            System.out.println("Area: " + shape.area());
            System.out.println("Circumference: " + shape.circumference());
            System.out.println();
        }
    }

    /**
     * Prints details of all shapes in JSON format.
     */
    public static void printAllDetailsJson() {
        System.out.println("All details on all shapes in JSON format:");
        Gson gson = new Gson();
        for (AbstractShape shape : PrintAllShapes.shapeList) {
            String json = gson.toJson(shape);
            System.out.println("Shape details in JSON: " + json);
            System.out.println();
        }
    }
}
