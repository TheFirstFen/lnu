package task3.com.sb224sc.classes;

import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.List;
import java.util.Scanner;

public class MoveShape {
    /**
     * Moves a movable shape from the list of shapes to a new position.
     *
     * @param sc        Scanner object for input.
     * @param shapeList List of shapes.
     */
    public static void moveShape(Scanner sc, List<AbstractShape> shapeList) {
        List<AbstractShape> movableShapes = getMovableShapes(shapeList);

        if (movableShapes.isEmpty()) {
            System.out.println("No movable shapes available.");
            return;
        }

        System.out.println("Movable Shapes:");
        for (int i = 0; i < movableShapes.size(); i++) {
            System.out.println(i + 1 + ". " + movableShapes.get(i));
        }
        try {
            int choice = getShapeChoice(sc, movableShapes.size());

            AbstractShape selectedShape = movableShapes.get(choice - 1);

            System.out.print("Enter X position to move: ");
            int moveX = sc.nextInt();
            System.out.print("Enter Y position to move: ");
            int moveY = sc.nextInt();

            selectedShape.moveAbsolute(new Position(moveX, moveY));
            System.out.println("Shape moved: " + selectedShape);
        } catch (Exception e) {
            System.out.println("An error occurred: " + e.getMessage());
        }
    }

    /**
     * Retrieves a list of the movable shapes from the given list of shapes.
     *
     * @param shapeList List of shapes to filter.
     * @return List containing only the movable shapes.
     */
    protected static List<AbstractShape> getMovableShapes(List<AbstractShape> shapeList) {
        List<AbstractShape> movableShapes = new ArrayList<>();

        for (AbstractShape shape : shapeList) {
            if (shape.isMoveable()) {
                movableShapes.add(shape);
            } else {
                System.out.println("Shape is not movable." + shape.toString());
            }
        }

        return movableShapes;
    }

    /**
     * Retrieves the users choice of a movable shape.
     *
     * @param sc        Scanner object for input.
     * @param maxChoice Maximum valid choice/How many movable shapes there are in
     *                  the list of movable shapes.
     * @return The users choice of shape to move.
     */
    protected static int getShapeChoice(Scanner sc, int maxChoice) {
        while (true) {
            try {
                System.out.print("Select a movable shape (1-" + maxChoice + "): ");
                int choice = sc.nextInt();
                if (choice >= 1 && choice <= maxChoice) {
                    return choice;
                } else {
                    System.out.println("Invalid choice. Please enter a valid number.");
                }
            } catch (InputMismatchException e) {
                System.out.println("Invalid input. Please enter a valid number.");
                sc.nextLine();
            }
        }
    }
}
