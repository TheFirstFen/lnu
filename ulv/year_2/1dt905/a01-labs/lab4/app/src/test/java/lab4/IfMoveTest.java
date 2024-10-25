package lab4;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.util.Scanner;

import lab4.com.Shape.*;

public class IfMoveTest {
    private AllShapes allShapes;
    //private TestInputOutput testIO;

    @BeforeEach
    public void setUp() {
        allShapes = new AllShapes();
    }

    @Test
    public void testMoveLoopWithEmptyList() {
        String input = "0\n";
        System.setIn(new ByteArrayInputStream(input.getBytes()));

        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outputStream));

        IfMove.moveLoop(new Scanner(System.in), allShapes);

        String expectedOutput = "The list of shapes is empty.\r\n";
        assertEquals(expectedOutput, outputStream.toString());
    }

    @Test
    public void testMoveLoopWithAbsMoveableShape() {
        AbstractShape moveableShape = new Point(2, 2);

        allShapes.addShape(moveableShape);

        String input = "0\n1\n2\n3\n";
        System.setIn(new ByteArrayInputStream(input.getBytes()));

        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outputStream));

        IfMove.moveLoop(new Scanner(System.in), allShapes);

        String expectedOutput = "The list contains: \r\n" + 
                "Shape at position 0:\r\n" + //
                "Point (2, 2)\r\n" + //
                "Enter the position of the shape to remove (0-0): Choose how to move the shape:\r\n" + //
                "1. Move Absolute\r\n" + //
                "2. Move Relative\r\n" + //
                "Enter your choice (1/2): Enter the new absolute position (x, y): \r\n" + //
                "Shape has been moved to (2, 3)\r\n";
        assertEquals(expectedOutput, outputStream.toString());
    }

    @Test
    public void testMoveLoopWithMoveableShape() {
        AbstractShape moveableShape = new Point(2, 2);

        allShapes.addShape(moveableShape);

        String input = "0\n2\n2\n3\n";
        System.setIn(new ByteArrayInputStream(input.getBytes()));

        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outputStream));

        IfMove.moveLoop(new Scanner(System.in), allShapes);

        String expectedOutput = "The list contains: \r\n" + 
                "Shape at position 0:\r\n" + //
                "Point (2, 2)\r\n" + //
                "Enter the position of the shape to remove (0-0): Choose how to move the shape:\r\n" + //
                "1. Move Absolute\r\n" + //
                "2. Move Relative\r\n" + //
                "Enter your choice (1/2): Enter the new relative movement (dx, dy): \r\n" + //
                "Shape has been moved to (4, 5)\r\n";
        assertEquals(expectedOutput, outputStream.toString());
    }

    @Test
    public void testMoveLoopWithNonMoveableShape() {
        AbstractShape moveableShape = new Line(2, 2);

        allShapes.addShape(moveableShape);

        String input = "0\n";
        System.setIn(new ByteArrayInputStream(input.getBytes()));

        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outputStream));

        IfMove.moveLoop(new Scanner(System.in), allShapes);

        String expectedOutput = "The list contains: \r\n" + 
                "Shape at position 0:\r\n" + //
                "Line (2, 2)-(0, 0)\r\n" + //
                "Enter the position of the shape to remove (0-0): Shape is not moveable.\r\n";
        assertEquals(expectedOutput, outputStream.toString());
    }
    
}
