package task3.com.sb224sc.classes;

import static org.junit.jupiter.api.Assertions.*;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.InputStream;
import java.io.PrintStream;
import java.util.Scanner;

import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class RemoveShapeTest {
    private final static RemoveShape removeShape = new RemoveShape();
    private final InputStream originalIn = System.in;
    private final PrintStream originalOut = System.out;
    private final ByteArrayOutputStream outContent = new ByteArrayOutputStream();

    @BeforeEach
    public void setUpStreams() {
        System.setOut(new PrintStream(outContent));
    }

    @Test
    public void testRemoveShapeWithEmptyList() {
        PrintAllShapes.clearShapes();
        Scanner sc = new Scanner(System.in);
        ByteArrayInputStream in = new ByteArrayInputStream("1\n".getBytes());
        System.setIn(in);

        RemoveShape.removeShape(sc, PrintAllShapes.shapeList);

        String expectedOutput = "No shapes available to remove.\n";

        assertEquals(expectedOutput, outContent.toString());
    }

    @Test
    public void testGetShapeChoiceWithValidInput() {
        Scanner sc = new Scanner(new ByteArrayInputStream("2\n".getBytes()));
        int choice = RemoveShape.getShapeChoice(sc, 3);
        assertEquals(2, choice);
    }

    @Test
    public void testGetShapeChoiceWithInvalidInput() {
        Scanner sc = new Scanner(new ByteArrayInputStream("invalid\n0\n-1\n4\n3\n".getBytes()));
        int choice = RemoveShape.getShapeChoice(sc, 3);
        assertEquals(3, choice);
    }

    @AfterEach
    public void restoreStreams() {
        System.setIn(originalIn);
        System.setOut(originalOut);
    }

    @AfterAll
    public static void tearDownAfterClass() {
        removeShape.toString();
    }
}
