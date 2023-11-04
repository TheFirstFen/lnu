package task3.com.sb224sc.classes;

import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class PrintAllDetailsTest {
    private final static PrintAllDetails printAllDetails = new PrintAllDetails();
    private final ByteArrayOutputStream outContent = new ByteArrayOutputStream();
    private final PrintStream originalOut = System.out;

    @BeforeEach
    public void setUpStreams() {
        System.setOut(new PrintStream(outContent));
    }

    @Test
    public void testPrintAllDetails() {
        PrintAllShapes.clearShapes();
        PrintAllShapes.shapeList.add(new Point());
        PrintAllShapes.shapeList.add(new Line());
        PrintAllShapes.shapeList.add(new Square(1));
        PrintAllShapes.shapeList.add(new Rectangle(1, 2));

        PrintAllDetails.printAllDetails();

        String expectedOutput = "All details on all shapes:\n" +
                "Point (0, 0)\n" +
                "Area: NaN\n" +
                "Circumference: NaN\n\n" +
                "Line (0, 0)-(0, 0)\n" +
                "Area: NaN\n" +
                "Circumference: NaN\n\n" +
                "Square (0, 0) w:1.0 h:1.0\n" +
                "Area: 1.0\n" +
                "Circumference: 4.0\n\n" +
                "Rectangle (0, 0) w:1.0 h:2.0\n" +
                "Area: 2.0\n" +
                "Circumference: 6.0\n\n";
        assertEquals(expectedOutput, outContent.toString());
    }

    @Test
    public void testPrintAllDetailsJson() {
        PrintAllShapes.clearShapes();
        PrintAllShapes.shapeList.add(new Point());
        PrintAllShapes.shapeList.add(new Line());
        PrintAllShapes.shapeList.add(new Square(1));
        PrintAllShapes.shapeList.add(new Rectangle(1, 2));

        PrintAllDetails.printAllDetailsJson();

        String expectedOutput = "All details on all shapes in JSON format:\n" +
                "Shape details in JSON: {\"name\":\"Point\",\"pos\":{\"x\":0,\"y\":0}," +
                "\"moveable\":true}\n\n" +
                "Shape details in JSON: {\"pos2\":{\"x\":0,\"y\":0},\"name\":\"Line\"," +
                "\"pos\":{\"x\":0,\"y\":0},\"moveable\":false}\n\n" +
                "Shape details in JSON: {\"width\":1.0,\"height\":1.0," +
                "\"name\":\"Square\",\"pos\":{\"x\":0,\"y\":0},\"moveable\":true}\n\n" +
                "Shape details in JSON: {\"width\":1.0,\"height\":2.0," +
                "\"name\":\"Rectangle\",\"pos\":{\"x\":0,\"y\":0},\"moveable\":false}\n\n";
        assertEquals(expectedOutput, outContent.toString());
    }

    @AfterEach
    public void restoreStreams() {
        System.setOut(originalOut);
    }

    @AfterAll
    public static void tearDownAfterClass() {
        printAllDetails.hashCode();
    }
}
