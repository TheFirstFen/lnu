package lab4;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import lab4.com.Shape.AllShapes;
import lab4.com.Shape.Rectangle;
import lab4.com.Shape.ShowAllShape;
import lab4.com.Shape.Point;

import org.junit.jupiter.api.AfterEach;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;


public class ShowAllShapeTest {
    private final ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
    private final PrintStream originalOut = System.out;

    @BeforeEach
    public void setUp() {
        System.setOut(new PrintStream(outputStream));
    }

    @AfterEach
    public void breackDown() {
        System.setOut(originalOut);
    }

    @Test
    public void testShowLoop() {
        AllShapes allShapes = new AllShapes();
        allShapes.addShape(new Point(2, 0));
        allShapes.addShape(new Rectangle(2, 2, 2, 2));

        ShowAllShape showAllShape = new ShowAllShape();
        showAllShape.showLoop(allShapes);

        String expectedOutput = "Point (2, 0)\r\n" +
                "Rectangle (2, 2) w:2.0 h:2.0\r\n";
        assertEquals(expectedOutput, outputStream.toString());
    }

}
