package lab3.com.Shape;

import java.util.List;
import java.util.Scanner;

/**
 * A class that allows the user to remove a shape from the collection
 */
public class ShapeRemove {
    /**
     * Shows all shaps, asks user which to remove and removes it
     * @param scanner Scanner object for user input
     * @param allShapes Collection of shapes from which a shape is removed
     */
    public void shapeLoop(Scanner scanner, AllShapes allShapes) {
        List<AbstractShape> shapes = allShapes.getAllShapes();
        int length = shapes.size();
        if (length == 0){
            System.out.println("The list of shapes is empty.");
        }
        else {
            System.out.println("The list contains: ");
            for (int i = 0; i < length; i++) {
                Shape shape = shapes.get(i);
                System.out.println("Shape at position " + i + ":");
                System.out.println(shape);
            }
        }
        System.out.print("Enter the position of the shape to remove (0-" + (length - 1) + "): ");
        int positionToRemove = scanner.nextInt();
        scanner.nextLine();

        if (positionToRemove>=0 && positionToRemove < length) {
            AbstractShape shapeToRemove = shapes.get(positionToRemove);
            allShapes.removeShape(shapeToRemove);
            System.out.println("Shape at position " + positionToRemove + "has been removed");
        }
        else {
            System.out.println("Invalid input, no shape was removed");
        }
        
    }
}
