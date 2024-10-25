package lab4;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import lab4.com.Shape.AbstractShape;
import lab4.com.Shape.AllShapes;
import lab4.com.Shape.Point;

import java.util.List;

public class AllShapesTest {
    private AllShapes allShapes;

    @BeforeEach
    public void setUp() {
        allShapes =  new AllShapes();
    }

    @Test
    public void testAddShapes() {
        Point point = new Point(5, 5);
        allShapes.addShape(point);
        List<AbstractShape> shapes = allShapes.getAllShapes();
        assertTrue(shapes.contains(point));
    }

    @Test
    public void testRemoveShapes() {
        Point point = new Point(0, 0);
        allShapes.addShape(point);
        allShapes.removeShape(point);
        List<AbstractShape> shapes = allShapes.getAllShapes();
        assertFalse(shapes.contains(point));
    }
    
}
