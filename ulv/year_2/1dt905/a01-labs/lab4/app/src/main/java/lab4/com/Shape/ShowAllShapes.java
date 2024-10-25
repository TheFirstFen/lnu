package lab4.com.Shape;

import java.util.List;

/**
 * A class that shows info on shapes in the collection
 */
public class ShowAllShapes {
    /**
     * Show the shapes information from the collection and thier area, circumference
     * @param allShapes The collection of shapes to be shown
     */
    public void showLoop(AllShapes allShapes) {
        List<AbstractShape> shapes = allShapes.getAllShapes();

        for (Shape shape : shapes) {
            System.out.println(shape);
            System.out.println("Area: " +shape.area());
            System.out.println("Circumference: " + shape.circumference());
        }

    }
}
