package task2.com.sb224sc.classes.menu;

import java.util.InputMismatchException;
import java.util.Scanner;

import task2.com.sb224sc.classes.*;

public class Menu {
    private AbstractShape shape = null;

    /**
     * Runs the menu loop to interact with shapes.
     */
    public void menuLoop() {
        try (Scanner sc = new Scanner(System.in)) {
            while (true) {
                printMenuOptions();

                int choice = getIntInput(sc);

                switch (choice) {
                    case 1:
                        shape = CreateShape.createShape(sc, shape);
                        break;
                    case 2:
                        AddRandShape.addRandShape();
                        break;
                    case 3:
                        MoveShape.moveShape(sc, PrintAllShapes.shapeList);
                        break;
                    case 4:
                        RemoveShape.removeShape(sc, PrintAllShapes.shapeList);
                        break;
                    case 5:
                        PrintAllShapes.printAllShapes();
                        break;
                    case 6:
                        PrintAllDetails.printAllDetails();
                        break;
                    case 7:
                        PrintAllDetails.printAllDetailsJson();
                        break;
                    default:
                        System.out.println("Please provide a valid option (1-7).");
                        break;
                }
            }
        } catch (Exception e) {
            System.out.println("An error occurred: " + e.getMessage());
        }
    }

    /**
     * Prints the available menu options.
     */
    private void printMenuOptions() {
        System.out.println("1. Select a shape and create it with a position and size");
        System.out.println("2. Insert a random shape with a random position and size");
        System.out.println("3. Move a shape (if it supports it)");
        System.out.println("4. Remove a shape");
        System.out.println("5. Print all shapes with its type, position, and size");
        System.out.println("6. Print all details on all shapes, including the area and circumference");
        System.out.println("7. Print all details on the shapes in JSON format");
    }

    /**
     * Gets an integer input from the user.
     *
     * @param sc Scanner object for input.
     * @return Integer input provided by the user.
     */
    private int getIntInput(Scanner sc) {
        while (true) {
            try {
                System.out.print("Enter your choice: ");
                return sc.nextInt();
            } catch (InputMismatchException e) {
                System.out.println("Invalid input. Please enter a valid number.");
                sc.nextLine();
            }
        }
    }
}