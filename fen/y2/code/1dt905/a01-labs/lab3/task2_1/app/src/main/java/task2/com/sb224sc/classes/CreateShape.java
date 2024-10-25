package task2.com.sb224sc.classes;

import java.util.InputMismatchException;
import java.util.Scanner;

public class CreateShape {
    /**
     * Creates a shape based on user input.
     *
     * @param sc    Scanner object for input.
     * @param shape Existing shape object to modify or null to create a new one.
     * @return The created or modified shape object, or null if an error occurs.
     */
    public static AbstractShape createShape(Scanner sc, AbstractShape shape) {
        try {
            System.out.print("Enter shape type (Point, Line, Rectangle, Square): ");
            sc.nextLine();
            String shapeType = sc.nextLine();

            if ("Point".equalsIgnoreCase(shapeType)) {
                shape = new Point();
            } else if ("Line".equalsIgnoreCase(shapeType)) {
                shape = new Line();
            } else if ("Rectangle".equalsIgnoreCase(shapeType)) {
                System.out.print("Enter width: ");
                double width = getDoubleInput(sc);
                System.out.print("Enter height: ");
                double height = getDoubleInput(sc);
                shape = new Rectangle(width, height);
            } else if ("Square".equalsIgnoreCase(shapeType)) {
                System.out.print("Enter width: ");
                double width = getDoubleInput(sc);
                shape = new Square(width);
            } else {
                System.out.println("Invalid shape type.");
            }

            if (shape != null) {
                System.out.print("Enter X position: ");
                int x = getIntInput(sc);
                System.out.print("Enter Y position: ");
                int y = getIntInput(sc);
                shape.moveAbsolute(new Position(x, y));
                System.out.println("Shape created: " + shape);
                PrintAllShapes.addShape(shape);
                return shape;
            } else {
                return null;
            }
        } catch (Exception e) {
            System.out.println("An error occurred: " + e.getMessage());
            return null;
        }
    }

    /**
     * Prompts the user for an integer input and handles exceptions.
     *
     * @param sc Scanner object for input.
     * @return Integer input provided by the user.
     */
    private static int getIntInput(Scanner sc) {
        while (true) {
            try {
                return sc.nextInt();
            } catch (InputMismatchException e) {
                System.out.println("Invalid input. Please enter a valid number.");
                sc.nextLine();
            }
        }
    }

    /**
     * Prompts the user for a double input and handles exceptions.
     *
     * @param sc Scanner object for input.
     * @return Double input provided by the user.
     */
    private static double getDoubleInput(Scanner sc) {
        while (true) {
            try {
                return sc.nextDouble();
            } catch (InputMismatchException e) {
                System.out.println("Invalid input. Please enter a valid number.");
                sc.nextLine();
            }
        }
    }
}
