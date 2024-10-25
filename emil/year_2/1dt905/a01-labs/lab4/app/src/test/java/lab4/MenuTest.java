package lab4;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.InputStream;
import java.io.PrintStream;

import lab4.com.Shape.*;

public class MenuTest {
    private final ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
    private final PrintStream originalOut = System.out;
    private final InputStream originalIn = System.in;

    private Menu menu;

    @BeforeEach
    public void setUp() {
        menu = new Menu();
        
        // Redirect System.out to capture the output
        System.setOut(new PrintStream(outputStream));
    }

    @AfterEach
    public void tearDown() {
        // Restore the original System.out and System.in streams
        System.setOut(originalOut);
        System.setIn(originalIn);
    }

    @Test
    public void testSelectShape() {
        
    }

    @Test
    public void testRandomShape() {

    }


    @Test
    public void testMoveShapeOption() {

    }

    @Test
    public void testRemoveShapeOption() {

    }

    @Test
    public void testShowShapesOption() {

    }

    @Test
    public void testShowAllShapesOption() {

    }

    @Test
    public void testJsonOption() {

    }


    @Test 
    public void testQuit() {
        System.setIn(new ByteArrayInputStream("q\n".getBytes()));

        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outputStream));
        menu.menuLoop();
        String expectedOutput = "# Shapes\r\n" +
        "1. Select a shape and create it with a position and size\r\n" +
        "2. Insert a random shape with a random position and size\r\n" +
        "3. Move a shape (if it supports it)\r\n" +
        "4. Remove a shape\r\n" +
        "5. Print all shapes with its type, position and size\r\n" +
        "6. Print all details on all shapes, including the area and circumference\r\n" +
        "7. Print all details on the shapes in a JSON format\r\n" +
        "q. Quit\r\n" +
        "Quiting\r\n";
         
        assertEquals(expectedOutput, outputStream.toString());
    }

    @Test
    public void testMenuLoop() {

    }

}
