package task2.com.sb224sc.classes;

import java.util.Random;

public class AddRandShape {
    /**
     * Adds a random shape with random position and size to the list of shapes.
     */
    public static void addRandShape() {
        Random rand = new Random();
        int randomX = rand.nextInt(100);
        int randomY = rand.nextInt(100);

        int randomChoice = rand.nextInt(4) + 1;
        AbstractShape randomShape = null;

        switch (randomChoice) {
            case 1:
                randomShape = new Point();
                break;
            case 2:
                randomShape = new Line();
                break;
            case 3:
                double randomWidth = rand.nextDouble() * 100;
                double randomHeight = rand.nextDouble() * 100;
                randomShape = new Rectangle(randomWidth, randomHeight);
                break;
            case 4:
                double randomSquareWidth = rand.nextDouble() * 100;
                randomShape = new Square(randomSquareWidth);
                break;
        }
        if (randomShape != null) {
            randomShape.moveAbsolute(new Position(randomX, randomY));
            PrintAllShapes.addShape(randomShape);
            System.out.println("Random shape created: " + randomShape);
        }
    }
}
