package task3.com.sb224sc.classes;

import java.util.InputMismatchException;
import java.util.List;
import java.util.Scanner;

public class RemoveShape {
    /**
     * Removes a shape from the list of shapes.
     *
     * @param sc        Scanner object for input.
     * @param shapeList List of shapes to get the shapes.
     */
    public static void removeShape(Scanner sc, List<AbstractShape> shapeList) {
        if (shapeList.isEmpty()) {
            System.out.println("No shapes available to remove.");
            return;
        }

        System.out.println("Shapes to Remove:");
        for (int i = 0; i < shapeList.size(); i++) {
            System.out.println(i + 1 + ". " + shapeList.get(i));
        }

        int choice = getShapeChoice(sc, shapeList.size());

        AbstractShape removedShape = shapeList.remove(choice - 1);
        System.out.println("Shape removed: " + removedShape);
    }

    /**
     * Removes a shape from the list of shapes.
     *
     * @param sc        Scanner object for input.
     * @param maxChoice Size of the list of shapes.
     * @return User choice of the shape to remove.
     */
    protected static int getShapeChoice(Scanner sc, int maxChoice) {
        while (true) {
            try {
                System.out.print("Select a shape to remove (1-" + maxChoice + "): ");
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
