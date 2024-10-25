package lab3.com.Shape;

import java.util.Scanner;

/**
 * A class that allows the user to select and create preselected shapes
 */
public class SelectShape {
    /**
     * Shows a menu with the different shape options, prompts the user to select 
     * one and createts it
     * @param scanner Scanner object for user input
     * @param allShapes Collection where the choosen shape is to be added
     */
    public void selectLoop(Scanner scanner, AllShapes allShapes) {

        System.out.println("What shape would you like to select out of the following: ");
        System.out.println("1. Point");
        System.out.println("2. Line");
        System.out.println("3. Rectangle");
        System.out.println("4. Square"); 

        String choice = scanner.nextLine();

        if (choice.equals("1")){
            System.out.println("Enter a x value for the point ");
            int x = scanner.nextInt();
            System.out.println("Enter a y value for the point ");
            int y =scanner.nextInt();
            OneDimension point = new Point(x, y);
            System.out.println(point);
            allShapes.addShape(point);
        }
        else if (choice.equals("2")) {
            System.out.println("Enter the x value the line starts on");
            int x =scanner.nextInt();
            System.out.println("Enter a y value the line starts on ");
            int y =scanner.nextInt();
            OneDimension line = new Line(x, y);
            System.out.println(line);
            allShapes.addShape(line);
        }

        else if (choice.equals("3")) {
            System.out.println("Enter the width of the rectangle ");
            int width =scanner.nextInt();
            System.out.println("Enter the height of the rectangle");
            int height =scanner.nextInt();
            System.out.println("Enter the x starting point of the rectangle");
            int x =scanner.nextInt();
            System.out.println("Enter the y starting point of the recangle");
            int y =scanner.nextInt();
            Quadrilateral rect = new Rectangle(width, height, x, y);
            System.out.println(rect);
            allShapes.addShape(rect);
        }

        else if (choice.equals("4")) {
            System.out.println("Enter the width/height of the square");
            int width =scanner.nextInt();
            System.out.println("Enter the x starting point of the square");
            int x =scanner.nextInt();
            System.out.println("Enter the y starting point of the square");
            int y =scanner.nextInt();

            Quadrilateral square = new Square(width, x, y);
            System.out.println(square);
            allShapes.addShape(square);
        }
        
    }
}
