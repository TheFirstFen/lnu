package lab3.com.Shape;

import static lab3.com.Shape.RandomShape.randomLoop;
import java.util.Scanner;


/**
 * A class providing a menu for shape interactions
 */
public class Menu {
    /**
     * Displays the menu and handels user inputs 
     */
    public void menuLoop() {
        AllShapes allShapes = new AllShapes();


        while (true) {
            Scanner scanner = new Scanner(System.in);
            System.out.println("# Shapes");

            System.out.println("1. Select a shape and create it with a position and size");
            System.out.println("2. Insert a random shape with a random position and size");
            System.out.println("3. Move a shape (if it supports it)");
            System.out.println("4. Remove a shape");
            System.out.println("5. Print all shapes with its type, position and size");
            System.out.println("6. Print all details on all shapes, including the area and circumference");
            System.out.println("7. Print all details on the shapes in a JSON format");
            System.out.println("q. Quit");
            String choice = scanner.nextLine();

            if (choice.equals("1")){
                SelectShape selectshape = new SelectShape();
                selectshape.selectLoop(scanner, allShapes);
            }

            else if (choice.equals("2")){
                randomLoop(allShapes);
            }

            else if (choice.equals("3")) {
                IfMove.moveLoop(scanner, allShapes);
            }

            else if (choice.equals("4")) {
                ShapeRemove shaperemove = new ShapeRemove();
                shaperemove.shapeLoop(scanner, allShapes);
            }

            else if (choice.equals("5")) {
                ShowAllShape showshape = new ShowAllShape();
                showshape.showLoop(allShapes);
            }

            else if (choice.equals("6")) {
                ShowAllShapes showshapes = new ShowAllShapes();
                showshapes.showLoop(allShapes);
            }

            else if (choice.equals("7")) {
                Json json = new Json();
                json.jsonLoop(allShapes);
            }

            else if (choice.equals("q")) {
                System.out.println("Quiting");
                scanner.close();
                break;
            }

            else {
                System.out.println("Wrong input try again");
            }
        
        }
    }
}
