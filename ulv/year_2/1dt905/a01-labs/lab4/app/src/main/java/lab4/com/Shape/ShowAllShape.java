package lab4.com.Shape;

import java.util.List;
/**
 * A class that shows info on shapes in the collection
 */
public class ShowAllShape {
    /**
     * Show the shapes information from the collection
     * @param allShapes The collection of shapes to be shown
     */
    public void showLoop(AllShapes allShapes) {
        List<AbstractShape> shapes = allShapes.getAllShapes();

        for (Shape shape : shapes) {
            System.out.println(shape);
        }
    }
}
