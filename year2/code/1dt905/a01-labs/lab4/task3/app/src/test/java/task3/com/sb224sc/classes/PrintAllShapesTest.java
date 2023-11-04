package task3.com.sb224sc.classes;

import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class PrintAllShapesTest {
    private final static PrintAllShapes printAllShapes = new PrintAllShapes();
    private final ByteArrayOutputStream outContent = new ByteArrayOutputStream();

    @BeforeEach
    public void setUpStreams() {
        System.setOut(new PrintStream(outContent));
    }

    @Test
    public void addShape() {
        AbstractShape shape = new Square(5.0);
        PrintAllShapes.addShape(shape);

        List<AbstractShape> shapeList = PrintAllShapes.shapeList;
        assertTrue(shapeList.contains(shape));
    }

    @Test
    public void getLastAddedShape() {
        AbstractShape shape1 = new Square(5.0);
        AbstractShape shape2 = new Rectangle(3.0, 4.0);

        PrintAllShapes.addShape(shape1);
        PrintAllShapes.addShape(shape2);

        assertEquals(shape2, PrintAllShapes.getLastAddedShape());
    }

    @Test
    public void getLastAddedShapeEmptyList() {
        PrintAllShapes.clearShapes();
        assertNull(PrintAllShapes.getLastAddedShape());
    }

    @Test
    public void clearShapes() {
        AbstractShape shape1 = new Square(5.0);
        AbstractShape shape2 = new Rectangle(3.0, 4.0);

        PrintAllShapes.addShape(shape1);
        PrintAllShapes.addShape(shape2);

        PrintAllShapes.clearShapes();

        assertTrue(PrintAllShapes.shapeList.isEmpty());
    }

    @Test
    public void printAllShapesAsOutput() {
        AbstractShape shape1 = new Square(5.0);
        shape1.moveAbsolute(new Position(0, 0));
        AbstractShape shape2 = new Rectangle(3.0, 4.0);
        shape2.moveAbsolute(new Position(0, 0));

        PrintAllShapes.clearShapes();

        PrintAllShapes.addShape(shape1);
        PrintAllShapes.addShape(shape2);

        PrintAllShapes.printAllShapes();
        String expectedOutput = "All shapes:\n" +
                "Type: Square (0, 0) w:5.0 h:5.0\n" +
                "\n" +
                "Type: Rectangle (0, 0) w:3.0 h:4.0\n" +
                "\n";

        assertEquals(expectedOutput, outContent.toString());
    }

    @AfterAll
    public static void tearDownAfterClass() {
        printAllShapes.toString();
    }
}
