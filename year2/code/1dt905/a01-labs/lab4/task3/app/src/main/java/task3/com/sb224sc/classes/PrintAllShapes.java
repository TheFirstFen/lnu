package task3.com.sb224sc.classes;

import java.util.ArrayList;
import java.util.List;

public class PrintAllShapes {
    public static List<AbstractShape> shapeList = new ArrayList<>();

    /**
     * Adds an abstract shape to the list.
     *
     * @param shape The abstract shape to add.
     */
    public static void addShape(AbstractShape shape) {
        shapeList.add(shape);
    }

    /**
     * Get the last added shape from the list.
     *
     * @return The last added shape, or null if the list is empty.
     */
    public static AbstractShape getLastAddedShape() {
        int size = shapeList.size();
        if (size > 0) {
            return shapeList.get(size - 1);
        } else {
            return null;
        }
    }

    /**
     * Clear the list of shapes.
     */
    public static void clearShapes() {
        shapeList.clear();
    }

    /**
     * Prints information about all shapes in the list, including their types.
     */
    public static void printAllShapes() {
        System.out.println("All shapes:");
        for (AbstractShape shape : shapeList) {
            System.out.println("Type: " + shape);
            System.out.println();
        }
    }
}
