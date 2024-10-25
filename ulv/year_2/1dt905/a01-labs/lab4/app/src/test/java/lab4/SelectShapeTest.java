package lab4;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import lab4.com.Shape.*;

import java.io.ByteArrayInputStream;
import java.io.InputStream;
import java.util.Scanner;

public class SelectShapeTest {
    private SelectShape selectShape;
    private AllShapes allShapes;

    @BeforeEach
    void setUp() {
        selectShape = new SelectShape();
        allShapes = new AllShapes();
    }

    @Test
    public void testSelectPoint() {
        String input = "1\n5\n10\n";
        InputStream inputStream = new ByteArrayInputStream(input.getBytes());
        System.setIn(inputStream);

        selectShape.selectLoop(new Scanner(System.in), allShapes);

        assertEquals(1, allShapes.getAllShapes().size());
        assertTrue(allShapes.getAllShapes().get(0) instanceof Point);
    }

    @Test
    public void testSelectLine() {
        String input = "2\n5\n10\n";
        InputStream inputStream = new ByteArrayInputStream(input.getBytes());
        System.setIn(inputStream);

        selectShape.selectLoop(new Scanner(System.in), allShapes);

        assertEquals(1, allShapes.getAllShapes().size());
        assertTrue(allShapes.getAllShapes().get(0) instanceof Line);
    }

    @Test
    void testSelectRectangle() {
        String input = "3\n5\n10\n20\n30\n2\n";
        InputStream inputStream = new ByteArrayInputStream(input.getBytes());
        System.setIn(inputStream);

        selectShape.selectLoop(new Scanner(System.in), allShapes);

        assertEquals(1, allShapes.getAllShapes().size());
        assertTrue(allShapes.getAllShapes().get(0) instanceof Rectangle);
    }

    @Test
    void testSelectSquare() {
        String input = "4\n5\n10\n20\n";
        InputStream inputStream = new ByteArrayInputStream(input.getBytes());
        System.setIn(inputStream);

        selectShape.selectLoop(new Scanner(System.in), allShapes);

        assertEquals(1, allShapes.getAllShapes().size());
        assertTrue(allShapes.getAllShapes().get(0) instanceof Square);
    }

    @Test
    void testSelectInvalidInput() {
        String input = "5\n";
        InputStream inputStream = new ByteArrayInputStream(input.getBytes());
        System.setIn(inputStream);

        selectShape.selectLoop(new Scanner(System.in), allShapes);

        assertEquals(0, allShapes.getAllShapes().size());
        assertNotNull(allShapes);
    }

}
