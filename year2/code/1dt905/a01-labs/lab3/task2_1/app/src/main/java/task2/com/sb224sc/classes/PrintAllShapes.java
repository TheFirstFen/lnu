package task2.com.sb224sc.classes;

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
