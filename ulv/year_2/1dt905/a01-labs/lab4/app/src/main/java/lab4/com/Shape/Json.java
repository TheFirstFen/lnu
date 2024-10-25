package lab4.com.Shape;

import java.util.List;
import com.google.gson.Gson;


/**
 * A class that converts and prints shapes in Json format
 */
public class Json {

    /**
     * Converts shapes in the collection to Json and prints them
     * @param allShapes The collection of shapes to be converted
     */
    public void jsonLoop(AllShapes allShapes) {
        List<AbstractShape> shapes = allShapes.getAllShapes();

        if (shapes.isEmpty()) {
            System.out.println("The list of shapes is empty.");
        } 
        else {
            Gson gson = new Gson();
            System.out.println("The list contains: ");

            for (int i = 0; i < shapes.size(); i++) {
                Shape shape = shapes.get(i);
                String shapeJson = gson.toJson(shape);

                System.out.println(shapeJson);
                System.out.println();
            }
        }
    }
}
