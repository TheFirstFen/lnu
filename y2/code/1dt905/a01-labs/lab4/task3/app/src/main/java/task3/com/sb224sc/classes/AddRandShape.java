package task3.com.sb224sc.classes;

import java.util.Random;

public class AddRandShape {
    private static Random rand = new Random();
    private static int fixedRandomChoice = -1; // Used for testing

    /**
     * Adds a random shape with random position and size to the list of shapes.
     */
    public static void addRandShape() {
        int randomChoice;

        if (fixedRandomChoice != -1) {
            randomChoice = fixedRandomChoice;
        } else {
            randomChoice = rand.nextInt(4) + 1;
        }

        AbstractShape randomShape = null;

        switch (randomChoice) {
            case 1:
                randomShape = new Point();
                break;
            case 2:
                randomShape = new Line();
                break;
            case 3:
                double randomWidth = rand.nextDouble() * 10;
                double randomHeight = rand.nextDouble() * 10;
                randomShape = new Rectangle(randomWidth, randomHeight);
                break;
            case 4:
                double randomSquareWidth = rand.nextDouble() * 10;
                randomShape = new Square(randomSquareWidth);
                break;
        }

        if (randomShape != null) {
            int randomX = rand.nextInt(50);
            int randomY = rand.nextInt(50);
            randomShape.moveAbsolute(new Position(randomX, randomY));
            PrintAllShapes.addShape(randomShape);
            System.out.println("Random shape created: " + randomShape);
        }
    }

    // Method for setting a fixed randomChoice value for testing
    public static void setFixedRandomChoice(int choice) {
        fixedRandomChoice = choice;
    }
}
