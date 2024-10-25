package lab4;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import lab4.com.Shape.AbstractShape;
import lab4.com.Shape.AllShapes;
import lab4.com.Shape.Line;
import lab4.com.Shape.Point;
import lab4.com.Shape.Rectangle;
import lab4.com.Shape.ShapeRemove;

import java.io.ByteArrayInputStream;
import java.io.InputStream;
import java.util.List;
import java.util.Scanner;

public class ShapeRemoveTest {
    private ShapeRemove shapeRemove;
    private AllShapes allShapes;

    @BeforeEach
    void setUp() {
        shapeRemove = new ShapeRemove();
        allShapes = new AllShapes();
    }

    @Test
    public void testRemoveShape() {
        allShapes.addShape(new Point(1, 2));
        allShapes.addShape(new Line(3, 4));
        allShapes.addShape(new Rectangle(5, 6, 7, 8));

        String input = "0\n";
        InputStream inputStream = new ByteArrayInputStream(input.getBytes());
        System.setIn(inputStream);

        shapeRemove.shapeLoop(new Scanner(System.in), allShapes);

        List<AbstractShape> shapes = allShapes.getAllShapes();
        assertEquals(2, shapes.size());
        assertTrue(shapes.get(0) instanceof Line);
        assertTrue(shapes.get(1) instanceof Rectangle);
    }

    @Test 
    public void testEmptyList(){
        String input = "0\n";
        InputStream inputStream = new ByteArrayInputStream(input.getBytes());
        System.setIn(inputStream);

        shapeRemove.shapeLoop(new Scanner(System.in), allShapes);

        List<AbstractShape> shapes = allShapes.getAllShapes();
        assertEquals(0, shapes.size());
    }

    @Test
    public void testInvalidInput() {
        allShapes.addShape(new Point(1, 2));
        allShapes.addShape(new Line(3, 4));
        allShapes.addShape(new Rectangle(5, 6, 7, 8));

        String input = "3\n";
        InputStream inputStream = new ByteArrayInputStream(input.getBytes());
        System.setIn(inputStream);

        shapeRemove.shapeLoop(new Scanner(System.in), allShapes);

        List<AbstractShape> shapes = allShapes.getAllShapes();
        assertEquals(3, shapes.size());
        assertTrue(shapes.get(0) instanceof Point);
        assertTrue(shapes.get(1) instanceof Line);
        assertTrue(shapes.get(2) instanceof Rectangle);
    }

    @Test
    public void testInvalidNegativInput() {
        allShapes.addShape(new Point(1, 2));
        allShapes.addShape(new Line(3, 4));
        allShapes.addShape(new Rectangle(5, 6, 7, 8));

        String input = "-1\n";
        InputStream inputStream = new ByteArrayInputStream(input.getBytes());
        System.setIn(inputStream);

        shapeRemove.shapeLoop(new Scanner(System.in), allShapes);

        List<AbstractShape> shapes = allShapes.getAllShapes();
        assertEquals(3, shapes.size());
        assertTrue(shapes.get(0) instanceof Point);
        assertTrue(shapes.get(1) instanceof Line);
        assertTrue(shapes.get(2) instanceof Rectangle);
    }



}