package task3.com.sb224sc.classes;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import java.io.ByteArrayInputStream;
import java.io.InputStream;
import java.util.Scanner;

import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;

public class CreateShapeTest {
    private final static CreateShape createShape = new CreateShape();

    private InputStream originalSystemIn;
    private Scanner sc;

    @BeforeEach
    public void setUp() {
        originalSystemIn = System.in;
    }

    @Test
    public void testCreatePointShape() {
        String input = "Point\nPoint\n1\n1\n";
        System.setIn(new ByteArrayInputStream(input.getBytes()));
        sc = new Scanner(System.in);

        AbstractShape shape = CreateShape.createShape(sc, null);

        assertNotNull(shape);
        assertTrue(shape instanceof Point);
    }

    @Test
    public void testCreateLineShape() {
        String input = "Line\nLine\n4.5\n1\n2\n";
        System.setIn(new ByteArrayInputStream(input.getBytes()));
        sc = new Scanner(System.in);

        AbstractShape shape = CreateShape.createShape(sc, null);

        assertNotNull(shape);
        assertTrue(shape instanceof Line);
    }

    @Test
    public void testCreateRectangleShape() {
        String input = "Rectangle\nRectangle\n2.5\n3.5\n1\n2\n";
        System.setIn(new ByteArrayInputStream(input.getBytes()));
        sc = new Scanner(System.in);

        AbstractShape shape = CreateShape.createShape(sc, null);

        assertNotNull(shape);
        assertTrue(shape instanceof Rectangle);
    }

    @Test
    public void testCreateSquareShape() {
        String input = "Square\nSquare\n4.5\n1\n2\n";
        System.setIn(new ByteArrayInputStream(input.getBytes()));
        sc = new Scanner(System.in);

        AbstractShape shape = CreateShape.createShape(sc, null);

        assertNotNull(shape);
        assertTrue(shape instanceof Square);
    }

    @Test
    public void testInvalidShapeType() {
        String input = "Invalid\n";
        System.setIn(new ByteArrayInputStream(input.getBytes()));
        sc = new Scanner(System.in);

        AbstractShape shape = CreateShape.createShape(sc, null);

        assertNull(shape);
    }

    @Test
    public void testInputMismatchException() {
        String input = "Point\ninvalid\n2\n3\n4\n";
        System.setIn(new ByteArrayInputStream(input.getBytes()));
        sc = new Scanner(System.in);

        AbstractShape shape = CreateShape.createShape(sc, null);

        assertNull(shape);
    }

    @Test
    public void testNoSuchElementException() {
        String input = "Point\n1\n2\n";
        System.setIn(new ByteArrayInputStream(input.getBytes()));
        sc = new Scanner(System.in);

        AbstractShape shape = CreateShape.createShape(sc, null);

        assertNull(shape);
    }

    @Test
    public void testGetDoubleInputException() {
        String input = "invalid\ninvalid\n1\n";
        System.setIn(new ByteArrayInputStream(input.getBytes()));
        sc = new Scanner(System.in);

        double value = CreateShape.getDoubleInput(sc);
        assertEquals(1, value);
    }

    @AfterEach
    public void tearDown() {
        System.setIn(originalSystemIn);
        if (sc != null) {
            sc.close();
        }
    }

    @AfterAll
    public static void tearDownAfterClass() {
        createShape.toString();
    }
}
