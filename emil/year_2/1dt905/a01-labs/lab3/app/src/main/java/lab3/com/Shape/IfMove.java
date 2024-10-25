package lab3.com.Shape;

import java.util.List;
import java.util.Scanner;


/**
 * A class that provieds a method on moving the shapes in a list
 */
public class IfMove {
    /**
     * Allows the user to choose shapes from the list, specify what type of move and preform it
     * @param scanner User inputs
     * @param allShapes The collection of shapes
     */
    public static void moveLoop(Scanner scanner, AllShapes allShapes) {
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


            System.out.print("Enter the position of the shape to remove (0-" + (length - 1) + "): ");
            int shapeToMove = scanner.nextInt();
            scanner.nextLine();

            if (shapeToMove>=0 && shapeToMove < length) {
                AbstractShape shapeToMoveObj = shapes.get(shapeToMove);
                if (shapeToMoveObj.isMoveable()) {
                    System.out.println("Choose how to move the shape:");
                    System.out.println("1. Move Absolute");
                    System.out.println("2. Move Relative");
                    System.out.print("Enter your choice (1/2): ");
                    int moveChoice = scanner.nextInt();
                    scanner.nextLine();

                    Position newPos;
                    if (moveChoice == 1) {
                        System.out.println("Enter the new absolute position (x, y): ");
                        int newX = scanner.nextInt();
                        int newY = scanner.nextInt();
                        newPos = new Position(newX, newY);
                        scanner.nextLine();
                        shapeToMoveObj.moveAbsolue(newPos);
                    }
                    else if (moveChoice == 2) {
                        System.out.println("Enter the new relative movement (dx, dy): ");
                        int dx = scanner.nextInt();
                        int dy = scanner.nextInt();
                        Position delta = new Position(dx, dy);
                        scanner.nextLine();
                        shapeToMoveObj.moveRelative(delta);
                    }
                    else {
                        System.out.println("Invalid choice. No movement preformed");
                        return;
                    }

                    System.out.println("Shape has been moved to " + shapeToMoveObj.getPosition());
                }
                else {
                    System.out.println("Shape is not moveable.");
                }
            }
            else {
                System.out.println("Invalid input, no shape was removed");
            }
        }
    }
}