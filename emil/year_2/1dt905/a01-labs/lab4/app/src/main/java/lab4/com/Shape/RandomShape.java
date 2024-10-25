package lab4.com.Shape;
import java.util.Random;

/**
 * A class that generates random shapes and adds them to the collection
 */
public class RandomShape {
    /**
     * Generates a random shape and adds it to the collection of shapes
     * @param allShapes The collection of shapes where the random shape is to be added
     */
    public static void randomLoop(AllShapes allShapes) {
        Random random = new Random();

        int shape = random.nextInt(1, 5);



        if (shape == 1) {
            int x = random.nextInt(100);
            int y = random.nextInt(100);
            OneDimension point = new Point(x,y);
            System.out.println(point);
            allShapes.addShape(point);

        }
        else if (shape == 2) {
            int x = random.nextInt(100);
            int y = random.nextInt(100);

            OneDimension line = new Line(x, y);
            System.out.println(line);
            allShapes.addShape(line);
        }
        else if (shape == 3) {
            int x = random.nextInt(100);
            int y = random.nextInt(100);
            Quadrilateral rect = new Rectangle(5, 5, x,  y);
            System.out.println(rect);
            allShapes.addShape(rect);
        }

        else{
            int x = random.nextInt(100);
            int y = random.nextInt(100);
            Quadrilateral square = new Square(5, x, y);
            System.out.println(square);
            allShapes.addShape(square);
        }
    }
}

