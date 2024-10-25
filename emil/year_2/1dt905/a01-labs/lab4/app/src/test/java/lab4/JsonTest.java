package lab4;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.AfterEach;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import lab4.com.Shape.*;

public class JsonTest {
    private final ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
    private final PrintStream originalOut = System.out;

    @BeforeEach
    public void setUp() {
        System.setOut(new PrintStream(outputStream));
    }

    @AfterEach
    public void tearDown() {
        System.setOut(originalOut);
    }

    @Test
    public void testJsonLoopWithEmptyList() {
        AllShapes allShapes = new AllShapes();

        Json json = new Json();
        json.jsonLoop(allShapes);

        String expectedOutput = "The list of shapes is empty.\r\n";
        assertEquals(expectedOutput, outputStream.toString());
    }

    @Test
    public void testJsonLoopWithShapes() {
        AllShapes allShapes = new AllShapes();

        allShapes.addShape(new Point(1, 1));
        allShapes.addShape(new Square(3, 2, 2));

        Json json = new Json();
        json.jsonLoop(allShapes);

        String expectedOutput = "The list contains: \r\n" + 
        "{\"name\":\"Point\",\"pos\":{\"x\":1,\"y\":1},\"isMoveable\":true}\r\n" + "\r\n" +
        "{\"width\":3.0,\"height\":3.0,\"name\":\"Square\",\"pos\":{\"x\":2,\"y\":2},\"isMoveable\":false}"
        + "\r\n" + "\r\n";

        assertEquals(expectedOutput, outputStream.toString());
    }

}
